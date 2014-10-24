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
print("Output is in .csv run$: python3 program_crabs2.py > output.csv")
print("This will output a .csv to the cwd with the columns deltaFLB, deltaRW, deltaCL, deltaCW, deltaDB, deltaERROR" )
print("*********************************************************************************\n");

# Random number from 1 to 199. Is used as the index for a specific crab 
random_crab_index = random.randint(1, 199)
count_male = 0
count_female = 0
plus_one_male = 0 
plus_one_female = 0
expected_sum = 0

## Initializes lists and fills a list to store weights into ##
# Stores weights
weights_list = []
# Stores all of the Sexs, Front lob sizes, rear widths..
SEXs = []
FLBs = []
RWs = []
CLs = []
CWs = []
DBs = []
# Stores the delta weights for each iteration
delta_flb_list = []
delta_rw_list = []
delta_cl_list = []
delta_cw_list = []
delta_db_list =[]
delta_error_list = []

# Fills weight list with specific weights
weights_list.append(0.0001)
weights_list.append(0.01)
weights_list.append(0.0001)
weights_list.append(0.01)
weights_list.append(0.0001)

# Initiales other varibles 
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
			
# Chooses a random crab and inputs its characteristics. Runs batch_sizes at a time and adjust weights accordingly 
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

	# adjust weights, and stores delta weights for each chracteristics
	weights_list[0] = weights_list[0] + learning_rate * total * FLB
	weights_list[1] = weights_list[1] + learning_rate * total * RW
	weights_list[2] = weights_list[2] + learning_rate * total * CL
	weights_list[3] = weights_list[3] + learning_rate * total * CW
	weights_list[4] = weights_list[4] + learning_rate * total * DB
	delta_flb = Compare((weights_list[0] - learning_rate * total * FLB), weights_list[0])
	delta_rw = Compare((weights_list[1] - learning_rate * total * RW), weights_list[1])
	delta_cl = Compare((weights_list[2] - learning_rate * total * CL), weights_list[2])
	delta_cw = Compare((weights_list[3] - learning_rate * total * CW), weights_list[3])
	delta_db = Compare((weights_list[4] - learning_rate * total * DB), weights_list[4])
	delta_flb_list.append(delta_flb)
	delta_rw_list.append(delta_rw)
	delta_db_list.append(delta_db)
	delta_cl_list.append(delta_cl)
	delta_cw_list.append(delta_cw)

# Hypothesis function takes in each chracteristics and sums the weights * chracteristics, then output the negation of the sum
def HypothesisFunc(flb, rw, cl, cw, db):
	w_sum = flb*weights_list[0] + rw*weights_list[1] + cl*weights_list[2] + cw*weights_list[3] + db*weights_list[4]
	w_sum *= -1
	return(w_sum)

# Expected output function is our E(x)
def ExpectedOutputFunc(s):
	expected_output = 1/(1 + math.exp(s))
	return (expected_output)	

# Testing function test the data after the batch loop has ran iteration times
def TestingFunc():
		random_crab_index = random.randint(1, 199)
		FLB = float(FLBs[random_crab_index])
		RW = float(RWs[random_crab_index])
		CL = float(CLs[random_crab_index])
		CW = float(CWs[random_crab_index])
		DB = float(DBs[random_crab_index])
		s = HypothesisFunc(FLB, RW, CL, CW, DB)
		expected = ExpectedOutputFunc(s)
		return(expected)

# # The add one function keeps up witht the number of correct of incorrect guesses in the testing funciton
# def AddOneMale():
# 	global plus_one_male
# 	plus_one_male = plus_one_male + 1
# 	return (plus_one_male)

# def AddOneFemale():
# 	global plus_one_female
# 	plus_one_female = plus_one_female + 1
# 	return (plus_one_female)

def Compare(old_weight, new_weight):
	delta_weight = old_weight - new_weight	
	return(delta_weight)	
	
# Reads CSV file and stores Sexs, Frontal lobe sizes, carapace lengths...	
ReadCsvFile()

# Learns the data 
for i in range(iterations):
	# Runs through the BatchLoopFunc with 10 iterations trainging
	BatchLoopFunc(SEXs, FLBs, RWs, CLs, CWs, DBs)
	learning_rate /= 1.03

# print delta weights for each input in .csv format
print("deltaFLB, deltaRW, deltaCL, deltaCW, deltaDB, deltaERROR")

# Test and prints the data .in csv format
for i in range(iterations):
	sex = TestingFunc()
	delta_error_list.append(sex)
	sys.stdout.write("%s" %delta_flb_list[i])
	sys.stdout.write(",")
	sys.stdout.write("%s" %delta_rw_list[i])
	sys.stdout.write(",")
	sys.stdout.write("%s" %delta_cl_list[i])
	sys.stdout.write(",")
	sys.stdout.write("%s" %delta_cw_list[i])
	sys.stdout.write(",")
	sys.stdout.write("%s" %delta_db_list[i])
	sys.stdout.write(",")
	sys.stdout.write("%s" %delta_error_list[i])
	sys.stdout.write("\n")












