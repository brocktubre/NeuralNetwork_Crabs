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

# List instantiation 
weights = []
FLs = []
CLs = []
SEXs = []
weights = [0.1, 0.2, 0.3, 0.4, 0.5]
# Picks a random crab as input
random_crab = random.randint(1, 199)
# Picks a random weight to use
random_weight = random.randint(0, 4)
weight = weights[random_weight] 

random_factor = random.randint(-5, 5)
while random_factor == 0:
	random_factor = random.randint(-5, 5)

# Reads in CSV file and stores input values
def ReadCsvFile():
	with open('crabs.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			fl = row[4]
			cl = row[6]
			sex = row[2]
			FLs.append(fl)
			CLs.append(cl)
			SEXs.append(sex)
		print(SEXs)

# Reads CSV file and stores Frontal lobe size, carapace length, and sex		
ReadCsvFile()	

FL = float(FLs[random_crab])
CL = float(CLs[random_crab])
Sex = SEXs[random_crab]
		

sys.stdout.write("Crab ID = ")
print(random_crab)
sys.stdout.write("Frontal lobe size = ")
print(FL)
sys.stdout.write("Carapace length = ")
print(CL)
print("\n")

function = (((weight * FL + weight * CL) * random_factor) / 2)
print(function)
MFoutput = math.tanh(function)


if MFoutput > 1:
	print("Guess = M")
	sys.stdout.write("Actual sex = ")
	print(Sex)
else:
	print("Guess = F")
	sys.stdout.write("Actual sex = ")
	print(Sex)


sys.stdout.write("Weight factor = ")
print(weight)











