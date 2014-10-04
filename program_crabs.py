import csv
import os
import random
import math
import sys


print("\n*********************************************************************************");
print("program_crabs.py")
sys.stdout.write("Directory ")
print(os.getcwd())
print("Created by Brock Tubre on 09/02/14 -- CSC475")
print("")
print("The problem at hand is to identify the sex of a crab given the observed values for each of these physical characteristics. You are expected to feed previously recorded inputs to a Neural Network and then tuning it to produce the desired target outputs.");
print("Compile & run $: python3 program_crabs.py")
print("*********************************************************************************\n");

# Picks a random crab as input
random_weight1 = random.randint(1, 5)
random_weight2 = random.randint(1, 5)
random_crab = random.randint(1, 199)
# List instantiation
iterations = 100
weights = []
FLs = []
CWs = []
SEXs = []
weights = [random_weight1, random_weight2, 1]
bias = weights[2]
alpha = 0.001
num_right = 0


# Reads in CSV file and stores input values
def ReadCsvFile():
	with open('crabs.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			fl = row[4]
			cw = row[7]
			sex = row[2]
			FLs.append(fl)
			CWs.append(cw)
			SEXs.append(sex)

def LearningFunc(fl, cw, sex, alpha):
	guess = GuessFunc(fl, cw)
	if guess and sex == 'M':
		error = -2
	elif not guess and sex == 'F':
		error = 2
	else:
		error = 0	

	weights[0] = weights[0] + error * fl * alpha
	weights[1] = weights[1] + error * cw * alpha
	#print(weights[0])
	#print(weights[1])

def TestingFunc(fl, cw, sex, weightFL, weightCL):
	guess = GuessFunc(fl, cw)
	if guess and sex == 'M':
		#print("Right!")
		AddOne()
	elif not guess and sex == 'F':
		#print("Right!")
		AddOne()


def GuessFunc(fl, cw):
	myguess = fl * weights[0] + cw * weights[1] + bias
	return(myguess > 0)

def AddOne():
	global num_right
	num_right = num_right + 1

# Reads CSV file and stores Frontal lobe size, carapace length, and sex		
ReadCsvFile()

for i in range(iterations):
	random_crab = random.randint(1, 199)
	FL = float(FLs[random_crab])
	CW = float(CWs[random_crab])
	Sex = SEXs[random_crab]
	LearningFunc(FL, CW, Sex, alpha)
	alpha = alpha / 1.05
	
for i in range(iterations):
	random_crab = random.randint(1, 199)
	FL = float(FLs[random_crab])
	CW = float(CWs[random_crab])
	Sex = SEXs[random_crab]
	TestingFunc(FL, CW, Sex, weights[0], weights[1])

sys.stdout.write("Number of learning/test cases: ")
print(iterations)
sys.stdout.write("Number of correct guesses: ")
print(num_right)
sys.stdout.write("Number of incorrect guesses: ")
print(iterations - num_right)
print("")
sys.stdout.write("Percent right: ")
print(num_right/iterations) 
print("")











