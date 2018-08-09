'''
Roll No.       : 16EE30025
Name 	       : Siddhant Haldar
Assignment No. : 1

Instructions:
To run the code, type the following command in the terminal
	
	python assignment_1.py --file "path to data1.csv"

'''

import argparse

#Parse command line arguements
parser = argparse.ArgumentParser(description='Assignment 1')
parser.add_argument("--file", required=True, help='File containing training data')

arg = parser.parse_args()

file_name = arg.file

data = []  #to store data from csv file

#read data from csv
with open(file_name,"r") as csv_data:
	data = csv_data.read().split('\n')

x = []		# train data
y = []		# result			

for i in range(len(data) - 1):
	x.append(data[i].split(',')[0:8])
	y.append(data[i].split(',')[8])

dim = len(x[0])  # num of attributes in each training data

# initialize hypothesis to null
h = []    
for i in range(dim):
	h.append(-1)

# In this code -1 denotes NULL and -2 denotes DON'T CARE	

# Update hypothesis depending on training data
for i in range(len(x)):
	data = x[i]
	res = int(y[i])
	if res == 1:	
		for l in range(len(data)):
			if h[l] == -1:
				h[l] = int(data[l])	

			elif int(data[l]) != h[l] and h[l] != -2 :
				h[l] = -2

# Print string in prescribed output format
res_string = str(0)
for i in range(len(h)):
	if h[i]!=-2:
		res_string = res_string[:0] + str(int(res_string[0])+1) + res_string[1:]
		if(h[i] == 1):
			res_string += "," + str(i+1)
		else:
			res_string += ",-" + str(i+1)

print(res_string)
