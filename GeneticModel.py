import random
import numpy

desired_value = 32
final = None

class Bits:
	bits = ""

	def __init__(self, size):
		for i in range(size):
			self.bits += '1' if random.random() >= 0.5 else '0'
		
	def get_value(self):
		value = 0
		for i in self.bits:
			value += int(i)
		return value
	
total_value = 0
starting_bits = [Bits(32) for i in range(50)]
for i in starting_bits:
	total_value += i.get_value()
	if i.get_value() == desired_value:
		final = i
		
print(total_value)

probabilities = []
for i in starting_bits:
	probabilities.append(i.get_value() / total_value)

if final is not None:
	print(final.get_value())
else:
	for i in range(100):
		print(numpy.random.choice(starting_bits, 1, probabilities)[0])
	while final is None:
		choice1 = numpy.random.choice(starting_bits, 1, probabilities)[0]
		choice2 = numpy.random.choice(starting_bits, 1, probabilities)[0]
	
input()