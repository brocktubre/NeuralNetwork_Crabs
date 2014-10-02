import csv
import os
import random
import math
import sys


print("\n***************************");
print("The problem at hand is to identify the sex of a crab given the observed values for each of these physical characteristics. You are expected to feed previously recorded inputs to a Neural Network and then tuning it to produce the desired target outputs.");
print("***************************\n\n");

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
weights = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
random_factor = random.randint(-5, 5)
random_crab = random.randint(1, 199)
random_weight = random.randint(0, 5)
weight = weights[random_weight]

with open('crabs.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		fl = row[4]
		cl = row[6]
		FLs.append(fl)
		CLs.append(cl)

FL = 	float(FLs[random_crab])
CL = float(Ls[random_crab])

def GetFilePath(file_name):
	current_dir = os.getcwd()
	file_path = os.path.join(current_dir, file_name)
	return file_path

path = GetFilePath('crabs.csv')	

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
print("\n")
print("\n")
print(x+y)

# random_weight =  {0.0, 0.1, 0.2, 0.3, 0.4, 0.5}
# random_factor = {-5, 5}
function = (((weight * float(FLs[random_crab])) + (weight * float(CLs[random_crab])) * random_factor) / 2
MFoutput = math.copysign(1, function)


if MFoutput > 1:
	print("Male")
else:
	print("Female")









