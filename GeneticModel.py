import random
import numpy

population = 10
desired_value = 32
final = None

def create_bits(size):
	bits = []
	for i in range(size):
		bits += ["1"] if random.random() <= 0.5 else ["0"]
	return bits
	
def get_value(bits):
	value = 0
	for i in bits:
		value += int(i)
	return value
	
total_value = 0
starting_bits = [create_bits(desired_value) for i in range(population)]
for i in starting_bits:
	total_value += get_value(i)
	if get_value(i) == desired_value:
		final = i

probabilities = []
for i in starting_bits:
	probabilities.append(get_value(i) / total_value)

if final is not None:
	print(get_value(final))
else:
	old_generation = starting_bits
	while final is None:
		new_generation = [["0"] * desired_value for i in range(population)]
		for i in old_generation:
			choice1 = numpy.random.choice(old_generation, 1, probabilities).tolist()
			choice2 = numpy.random.choice(old_generation, 1, probabilities).tolist()
			
			print("1: " + str(len(choice1)))
			print("2: " + str(len(choice1)))
			
			for j in choice1:
				if random.random() <= 0.5:
					i[random.randint(0, desired_value - 1)] = j
				
			for j in choice2:
				if random.random() <= 0.5:
					i[random.randint(0, desired_value - 1)] = j
					
		old_generation = new_generation
		for i in old_generation:
			print(len(i))
		
		input()
	
input()