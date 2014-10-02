import csv

with open('crabs.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')

	IDs = []
	SEXs = []	

	for row in readCSV:
		i_d = row[0]
		sex = row [2]

		IDs.append(i_d)
		SEXs.append(sex) 

	print(IDs)
	print(SEXs)	