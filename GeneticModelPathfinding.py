import random

mutation_rate = 0.01
population = 8
desired_fitness = 16
chromosome_length = 16

class Map:
	width = 0
	height = 0
	start = (0, 0)
	end = (0, 0)
	map = None

	def __init__(self, file):
		# Open map file and read data
		with open(file, 'r', encoding="utf-16") as f:
			data = f.read().split(' ')
			
		# Get width and height of map
		self.width = int(data[0])
		del data[0]
		self.height = int(data[0])
		del data[0]
		
		# Put map tiles into 2D array, and get the start and end
		self.map = [[0 for i in range(self.width)] for i in range(self.height)]
		for y in range(self.height):
			for x in range(self.width):
				self.map[y][x] = data[x + y * self.width]
				if self.map[y][x] == '2':
					self.start = (x, y)
				elif self.map[y][x] == '3':
					self.end = (x, y)
					
		print("START: " + str(self.start[0]) + " - " + str(self.start[1]))
		print("END: " + str(self.end[0]) + " - " + str(self.end[1]))
		
	def run(self, chromosome):
		# Set start position
		x, y = self.start
		
		# Go through each move in the chromosome
		for i in range(0, chromosome_length, 2):
			pair = chromosome[i] + chromosome[i + 1]
			if pair == "00":
				if y - 1 >= 0 and self.map[y - 1][x] != "1":
					y -= 1
			elif pair == "01":
				if x - 1 >= 0 and self.map[y][x - 1] != "1":
					x -= 1
			elif pair == "10":
				if y + 1 < self.height and self.map[y + 1][x] != "1":
					y += 1
			elif pair == "11":
				if x + 1 < self.width and self.map[y][x + 1] != "1":
					x += 1
		
		# Return the distance away from the end point
		return (self.end[0] - x, self.end[1] - y)

def create_chromosome(size):
	return ["1" if random.random() <= 0.5 else "0" for i in range(size)]
	
def get_fitness(map, chromosome):
	dx, dy = map.run(chromosome)
	return 1 / (dx + dy + 1)
	
def wheel_spin(map, generation, total_fitness):
	fitness_sum = 0
	choice = random.random()
	for chromosome in generation:
		if choice >= fitness_sum and choice <= fitness_sum + (get_fitness(map, chromosome) / total_fitness):
			return chromosome
		fitness_sum += get_fitness(map, chromosome) / total_fitness
		
def main():
	random.seed()
	
	final = None
	old_generation = [create_chromosome(chromosome_length) for i in range(population)]
	iter = 0
	
	map = Map("Labs15and16TerrainFile1.txt")
	
	while final is None:
		iter += 1
		print(iter)
		
		total_fitness = 0
		for chromosome in old_generation:
			if get_fitness(map, chromosome) == 1:
				final = chromosome
			total_fitness += get_fitness(map, chromosome)
		
		new_generation = [["0"] * chromosome_length for i in range(population)]
		for i in range(population):
			choice1 = wheel_spin(map, old_generation, total_fitness)
			choice2 = wheel_spin(map, old_generation, total_fitness)
			
			# Get the halfs of 
			first_half = choice1[:int(len(choice1) / 2)]
			second_half = choice2[int(len(choice2) / 2):]
			
			new_chromosome = first_half + second_half
			for j in range(len(new_chromosome)):
				if random.random() <= mutation_rate:
					new_chromosome[j] = str(int(not int(new_chromosome[j])))
			
			print(''.join(new_chromosome))
			new_generation[i] = new_chromosome
			
		old_generation = new_generation
		
	input("FINAL: " + ''.join(final))
	
if __name__ == "__main__":
	main()