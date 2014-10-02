import csv
import os
import random

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

def GetFilePath(file_name):
	current_dir = os.getcwd();
	file_path = os.path.join(current_dir, file_name);
	return file_path;

path = GetFilePath('crabs.csv');	

def ReadCsvFile(filepath):
	with open(filepath, 'rU') as csvfile:
		reader = csv.reader(csvfile);
		for attr in reader:
			print (attr[0], attr[1], attr[3], attr[4], attr[5], attr[6], attr[7], attr[8]);



ReadCsvFile(path);



