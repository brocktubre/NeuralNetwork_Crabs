import csv
import os
import random
import math
import sys


print("\n*********************************************************************************");
print("program_crabs.py")
sys.stdout.write("Directory ")
print(os.getcwd())
print("Created by Brock Tubre on 09/02/14")
print("")
print("The problem at hand is to identify the sex of a crab given the observed values for each of these physical characteristics. You are expected to feed previously recorded inputs to a Neural Network and then tuning it to produce the desired target outputs.");
print("Compile & run $: python3 program_crabs.py")
print("*********************************************************************************\n");

# int1 = 5;
# int2 = 10;
# int3 = int1 + int2;

# print(int3);
#current_dir = os.getcwd();
#file_name = 'crabs.csv';
#file_path = os.path.join(current_dir, file_name);

# Finds the sign of the number math.copysign(x,y) x should be 1 and y should be input;
#y = some final input;
#sign = math.copysign(1, y);
#print(sign);


weights = []
FLs = []
CLs = []
SEXs = []
weights = [0.1, 0.2, 0.3, 0.4, 0.5]
random_crab = random.randint(1, 199)
random_weight = random.randint(0, 4)
weight = weights[random_weight]

random_factor = random.randint(-5, 5)
while random_factor == 0:
	random_factor = random.randint(-5, 5)

with open('crabs.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		fl = row[4]
		cl = row[6]
		sex = row[2]
		FLs.append(fl)
		CLs.append(cl)
		SEXs.append(sex)

FL = 	float(FLs[random_crab])
CL = float(CLs[random_crab])
Sex = SEXs[random_crab]

#def GetFilePath(file_name):
	#current_dir = os.getcwd()
	#file_path = os.path.join(current_dir, file_name)
	#return file_path

#path = GetFilePath('crabs.csv')	

#def ReadCsvFile(filepath):
	#with open(filepath, 'rU') as csvfile:
	#csvfile = open(filepath, "rb")
		#reader = csv.reader(csvfile)
		#for attr in reader:
			#print (attr[0], attr[1], attr[3], attr[4], attr[5], attr[6], attr[7], attr[8]);

#ReadCsvFile(path)
sys.stdout.write("Crab ID = ")
print(random_crab)
sys.stdout.write("Frontal lobe size = ")
print(FL)
sys.stdout.write("Carapace length = ")
print(CL)
print("\n")

# random_weight =  {0.0, 0.1, 0.2, 0.3, 0.4, 0.5}
# random_factor = {-5, 5}
#function = (((weight * FL) + (weight * CL) * random_factor) / 2)
function = (((weight * FL + weight * CL) * random_factor) / 2)
print(function)
MFoutput = math.copysign(function, function)


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











