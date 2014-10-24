import csv
import os
import random
import math
import sys


print("\n*********************************************************************************");
print("program_crabs.py")
sys.stdout.write("Directory ")
print(os.getcwd())
print("Created by Brock Tubre on 10/24/14 -- CSC475")
print("")
print("Using the crab’s dataset, build a classifier that can identify the sex of a crab from its physical measurements.");
print("Five physical measurements of a crab considered are: frontal lobe size (FLB), rear width (RW), length (CL), width (CW), and depth (BD).");
print("This program uses a Batch Gradient Descnes Algorithm")
print("Compile & run $: python3 program_crabs2.py")
print("*********************************************************************************\n");

# Random number from 1 to 199. Is used as the index for a specific crab 
random_crab_index = random.randint(1, 199)

# Fills a list
weights_list = []

for i in range(5):
	random_weight = round(random.uniform(0.1, 0.5), 10)
	weights_list.append(random_weight)

# Fills weight list with specific weights
weights_list[0] = 0.0001
weights_list[1] = 0.01
weights_list[2] = 0.0001
weights_list[3] = 0.01
weights_list[4] = 0.0001

# Initializes list to slore all of the Sexs, Front lob sizes, rear widths..
SEXs = []
FLBs = []
RWs = []
CLs = []
CWs = []
DBs = []

learning_rate = 0.0001
batch_size = 10
iterations = 1000

# Reads in CSV file and stores input values
def ReadCsvFile():
	with open('crabs.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			sex = row[2]
			flb = row[4]
			rw =	row[5]
			cl = row[6]
			cw = row[7]
			db = row[8]
			SEXs.append(sex)
			FLBs.append(flb)
			RWs.append(rw)
			CLs.append(cl)
			CWs.append(cw)
			DBs.append(db)
			
# Chooses a random crab and inputs its 
def BatchLoopFunc(Sex, FLB, RW, CL, CW, DB):
	total = 0
	for i in range(batch_size):
		random_crab_index = random.randint(1, 199)
		FLB = float(FLBs[random_crab_index])
		RW = float(RWs[random_crab_index])
		CL = float(CLs[random_crab_index])
		CW = float(CWs[random_crab_index])
		DB = float(DBs[random_crab_index])
		s = HypothesisFunc(FLB, RW, CL, CW, DB)
		expected = ExpectedOutputFunc(s)
		total += (expected - 0.5)**2
	total /= batch_size

	# adjust weights
	weights_list[0] = weights_list[0] + learning_rate * total * FLB
	weights_list[1] = weights_list[1] + learning_rate * total * RW
	weights_list[2] = weights_list[2] + learning_rate * total * CL
	weights_list[3] = weights_list[3] + learning_rate * total * CW
	weights_list[4] = weights_list[4] + learning_rate * total * DB

def HypothesisFunc(flb, rw, cl, cw, db):
	w_sum = flb*weights_list[0] + rw*weights_list[1] + cl*weights_list[2] + cw*weights_list[3] + db*weights_list[4]
	w_sum *= -1
	return(w_sum)

def ExpectedOutputFunc(s):
	expected_output = 1/(1 + math.exp(s))
	return (expected_output)	

def TestingFunc():
		random_crab_index = random.randint(1, 199)
		Sex = SEXs[random_crab_index]
		FLB = float(FLBs[random_crab_index])
		RW = float(RWs[random_crab_index])
		CL = float(CLs[random_crab_index])
		CW = float(CWs[random_crab_index])
		DB = float(DBs[random_crab_index])
		s = HypothesisFunc(FLB, RW, CL, CW, DB)
		expected = ExpectedOutputFunc(s)
		#sys.stdout.write("Expected: ")
		sys.stdout.write("%s" %expected)
		sys.stdout.write(",")
		sys.stdout.write("%s" %Sex)
		sys.stdout.write("\n")
		#sys.stdout.write(" Sex: ")
		#print(Sex)
		#print(expected)
		return(Sex)

# The add one function keeps up witht the number of correct of incorrect guesses in the testing funciton
def AddOne():
	global plus_one_male
	plus_one_male = plus_one + 1
	return (plus_one)

def AddOne():
	global plus_one_female
	plus_one_female = plus_one_female + 1
	return (plus_one_female)	
	
# Reads CSV file and stores Sexs, Frontal lobe sizes, carapace lengths...	
ReadCsvFile()

# Learns the data 
for i in range(iterations):
	# Runs through the BatchLoopFunc with 10 iterations trainging
	BatchLoopFunc(SEXs, FLBs, RWs, CLs, CWs, DBs)
	learning_rate /= 1.03

# Test the data with learned data
for i in range(iterations):
	sex = TestingFunc()
	if(sex == "M"):
		count_male = AddOneMale()
		print(count)
	else:
		count_female = AddOneFemail()	











