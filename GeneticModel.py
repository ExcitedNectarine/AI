import random

mutation_rate = 0.01
population = 8
desired_fitness = 16
chromosome_length = 16

def create_bits(size):
	return ["1" if random.random() <= 0.5 else "0" for i in range(size)]
	
def get_fitness(bits):
	value = 0
	for i in bits:
		value += int(i)
	return value
	
def wheel_spin(generation, total_fitness):
	fitness_sum = 0
	choice = random.random()
	for chromosome in generation:
		if choice >= fitness_sum and choice <= fitness_sum + (get_fitness(chromosome) / total_fitness):
			return chromosome
		fitness_sum += get_fitness(chromosome) / total_fitness
		
def main():
	random.seed()
	
	final = None
	old_generation = [create_bits(chromosome_length) for i in range(population)]
	iter = 0
	
	while final is None:
		iter += 1
		print(iter)
		
		total_fitness = 0
		for chromosome in old_generation:
			if get_fitness(chromosome) == desired_fitness:
				final = chromosome
			total_fitness += get_fitness(chromosome)
		
		new_generation = [["0"] * chromosome_length for i in range(population)]
		for i in range(population):
			choice1 = wheel_spin(old_generation, total_fitness)
			choice2 = wheel_spin(old_generation, total_fitness)
			
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
	
main()