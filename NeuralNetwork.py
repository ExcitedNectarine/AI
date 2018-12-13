import math
import random

def sigmoid(x, theta):
	return 1 / (1 + math.exp(1) ** (-(x - theta)))
	
def step(x, theta):
	return 1 if x >= theta else 0
	
def sign(x, theta):
	return 1 if x >= theta else -1
	
def linear(x, theta):
	return x - theta
	
def singlelayer():
	w1 = random.uniform(-1, 1)
	w2 = random.uniform(-1, 1)
	theta = 0.5
	alpha = 0.1

	x1 = [0, 0, 1, 1]
	x2 = [0, 1, 0, 1]
	y = [0, 0, 0, 1]

	for i in range(100):
		j = i % 4
		x = (x1[j] * w1) + (x2[j] * w2)
		
		Y = step(x, theta)
		e = y[j] - Y
		
		w1 += alpha * x1[j] * e
		w2 += alpha * x2[j] * e
		
	print(step((0 * w1) + (0 * w2), theta))
	print(step((0 * w1) + (1 * w2), theta))
	print(step((1 * w1) + (0 * w2), theta))
	print(step((1 * w1) + (1 * w2), theta))
	
def multilayer():
	iterations = 10000
	weights = [[random.uniform(-1, 1) for i in range(5)] for i in range(5)]
	weights[0][2] = 0.5;
	weights[1][2] = 0.4;
	weights[0][3] = 0.9;
	weights[1][3] = 1.0;
	weights[2][4] = -1.2;
	weights[3][4] = 1.1;
	thetas = [0, 0, 0.8, -0.1, 0.3]
	alpha = 0.1
	x1 = [1, 0, 1, 0]
	x2 = [1, 1, 0, 0]
	yd5 = [0, 1, 1, 0]
	x = [0] * 5
	e = [0] * 5
	y = [0] * 5
	tx = [0] * 5
	ty = [0] * 5
	te = [0] * 5
	delta = [0] * 5
	wcurrent = [ ([0] * 5) for i in range(5) ]

	p = 1
	while p <= iterations - 4:
		epoc_sum_error = 0
		for i in range(4):
			# Calculate output of neurons before adjusting weights
			x[2] = x1[i] * weights[0][2] + x2[i] * weights[1][2]
			y[2] = sigmoid(x[2], thetas[2])
			x[3] = x1[i] * weights[0][3] + x2[i] * weights[1][3]
			y[3] = sigmoid(x[3], thetas[3])
			x[4] = y[2] * weights[2][4] + y[3] * weights[3][4]
			y[4] = sigmoid(x[4], thetas[4])
			e[4] = yd5[i] - y[4];
			
			# Adjust weights for neurons, starting at the 5th (output layer)
			delta[4] = y[4] * (1 - y[4]) * e[4]
			wcurrent[2][4] = weights[2][4]
			wcurrent[3][4] = weights[3][4]
			weights[2][4] += alpha * y[2] * delta[4]
			weights[3][4] += alpha * y[3] * delta[4]
			thetas[4] += alpha * (-1) * delta[4]
			
			# Adjust weights for 3rd neuron
			delta[2] = y[2] * (1 - y[2]) * delta[4] * wcurrent[2][4]
			weights[0][2] += alpha * x1[i] * delta[2]
			weights[1][2] += alpha * x1[i] * delta[2]
			thetas[2] += alpha * (-1) * delta[2]

			# Adjust weights for 4th neuron
			delta[3] = y[3] * (1 - y[3]) * delta[3] * wcurrent[3][4]
			weights[0][3] += alpha * x1[i] * delta[3]
			weights[1][3] += alpha * x2[i] * delta[3]
			thetas[3] += alpha * (-1) * delta[3]
			
			# Calculate output of neurons after adjusting weights, and use to adjust epoc_sum_error
			tx[2] = x1[i] * weights[0][2] + x2[i] * weights[1][2];
			ty[2] = sigmoid(tx[2], thetas[2])
			tx[3] = x1[i] * weights[0][3] + x2[i] * weights[1][3];
			ty[3] = sigmoid(tx[3], thetas[3])
			tx[4] = ty[2] * weights[2][4] + ty[3] * weights[3][4]
			ty[4] = sigmoid(tx[3], thetas[3])
			te[4] = yd5[i] - ty[4]
			
			print(str(p) + " =======================")
			print("W13: " + str(weights[0][2]))
			print("W14: " + str(weights[1][2]))
			print("W23: " + str(weights[0][3]))
			print("W24: " + str(weights[1][2]))
			print("W35: " + str(weights[2][4]))
			print("W45: " + str(weights[3][4]))
			print("T3: " + str(thetas[2]))
			print("T4: " + str(thetas[3]))
			print("T5: " + str(thetas[4]))
			print("Y3: " + str(y[2]))
			print("Y3: " + str(y[3]))
			print("Y3: " + str(y[4]))

			epoc_sum_error += te[4] ** 2
			p += 1
			
		if epoc_sum_error < 0.001:
			input("DONE")
			break
			
if __name__ == "__main__":
	singlelayer()
	input()
	multilayer()
	input()