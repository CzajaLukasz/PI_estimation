import random
import math

if __name__ == '__main__':
    R = 100000
    DRAWSPOWER = 7
    NUMBEROFDRAWS = 10**DRAWSPOWER
    PI = math.pi
    ITERATIONS = 10
    errors = dict.fromkeys((10 ** i for i in range(1, DRAWSPOWER + 1)), 0)
    worstEstimation = 0.0
    biggestDifference = 0.0
    for j in range(ITERATIONS):
        print("\rIt's Iteration number: " + str(j), end="")
        pointsInsideCircle = 0
        checkPoint = 10
        for i in range(1, NUMBEROFDRAWS + 1):
            drawnX = random.randint(0, R)
            drawnY = random.randint(0, R)
            if drawnX**2 + drawnY**2 <= R**2:
                pointsInsideCircle += 1
            if i == checkPoint:
                estimated_pi = 4 * pointsInsideCircle / i
                errors[i] += (PI - estimated_pi) ** 2
                checkPoint *= 10
                if i == NUMBEROFDRAWS and abs(PI - estimated_pi) > biggestDifference:
                    biggestDifference = abs(PI - estimated_pi)
                    worstEstimation = estimated_pi
    print("\r", end="")
    for key in errors.keys():
        print("Average error for " + str(key) + " draws is: " + str((errors[key] / ITERATIONS)**(1/2)))
    print()
    print("For " + str(NUMBEROFDRAWS) + " points the worst estimation was: " + str(worstEstimation)
          + " with " + str(biggestDifference) + " difference from the exact value, but average error was: "
          + str(errors[NUMBEROFDRAWS]**(1/2) / ITERATIONS))

