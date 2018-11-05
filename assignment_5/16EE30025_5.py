'''
Roll No.       : 16EE30025
Name 	       : Siddhant Haldar
Assignment No. : 4
Instructions:
To run the code, type the following command in the terminal
	
	python 16EE30025_4.py 
'''

import math
import numpy as np 

data = "spambase.data"

def read_train_data(filename):
	train_data = []  
	test_data = []

	#read data from csv
	with open(filename,"r") as csv_data:
		data = csv_data.read().split('\n')

	train_len = 0.7 * len(data)
	for i in range(len(data)-1):	
		row = data[i].split(',')
		for i in range(len(row)):
			row[i] = float(row[i])

		if i < train_len:
			train_data.append(row)
		else:
			test_data.append(row)
			
	return np.asarray(train_data), np.asarray(test_data)

# def train	

if __name__ =="__main__":
	train_data, test_data = read_train_data(data)
	print(train_data.shape)

