import math
import random

def sigmoid(x, theta):
    return 1 / (1 + math.exp(-(x - theta)))
    
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
            print("Iteration " + str(p))
        
            x[2] = x1[i] * weights[0][2] + x2[i] * weights[1][2]
            y[2] = sigmoid(x[2], thetas[2])
            
            x[3] = x1[i] * weights[0][3] + x2[i] * weights[1][3]
            y[3] = sigmoid(x[3], thetas[3])
            
            x[4] = x1[i] * weights[0][4] + x2[i] * weights[1][4]
            y[4] = sigmoid(x[4], thetas[4])
            
            e[4] = yd5[i] - y[4];
            delta[4] = y[4] * (1 - y[4]) * e[4]
            wcurrent[2][4] = weights[2][4]
            wcurrent[3][4] = weights[3][4]
            weights[2][4] += alpha * y[2] * delta[4]
            weights[3][4] += alpha * y[3] * delta[4]
            thetas[4] += alpha * -1 * delta[4]

            delta[2] = y[2] * (1 - y[2]) * delta[4] * wcurrent[2][4]
            weights[0][2] += alpha * x1[i] * delta[2]
            weights[1][2] += alpha * x1[i] * delta[2]
            thetas[2] += alpha * -1 * delta[2]

            delta[3] = y[3] * (1 - y[3]) * delta[3] * wcurrent[3][4]
            weights[0][3] += alpha * x1[i] * delta[3]
            weights[1][3] += alpha * x2[i] * delta[3]
            thetas[3] += alpha * -1 * delta[3]
            
            tx[2] = x1[i] * weights[0][2] + x2[i] * weights[1][2];
            ty[2] = 1 / (1 + (math.exp(1)) ** (-(tx[2] - thetas[2])));
            
            tx[3] = x1[i] * weights[0][3] + x2[i] * weights[1][3];
            ty[3] = 1 / (1 + (math.exp(1)) ** (-(tx[3] - thetas[3])));
            
            tx[4] = x1[i] * weights[0][4] + x2[i] * weights[1][4];
            ty[4] = 1 / (1 + (math.exp(1)) ** (-(tx[4] - thetas[4])));
            
            tx[4] = yd5[i] - ty[4]

            epoc_sum_error += te[4] ** 2
            p += 1
            
            print("Y3: " + str(y[2]) + " Y4: " + str(y[3]) + " Y5: " + str(y[4]))
            
            
singlelayer()
input()
multilayer()
input()