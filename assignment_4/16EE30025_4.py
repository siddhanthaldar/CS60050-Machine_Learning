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

train_file = "data4.csv"
test_file = "test4.csv"
k = 5 

def read_train_data(filename):
	train_data = []  #to store training data from csv file
	data = []

	#read data from csv
	with open(filename,"r") as csv_data:
		data = csv_data.read().split('\n')

	for i in range(len(data)):	
		row = data[i].split(',')
		for i in range(len(row)):
			row[i] = float(row[i])
		train_data.append(row)
	return np.asarray(train_data)

def read_test_data(filename):
	test_data = []  #to store training data from csv file
	data = []

	#read data from csv
	with open(filename,"r") as csv_data:
		data = csv_data.read().split('\n')

	for i in range(len(data)):	
		row = data[i].split(',')
		for i in range(len(row)):
			row[i] = float(row[i])
		test_data.append(row)
	return np.asarray(test_data)	



def distance(sample, train_data):
	return np.sqrt(np.sum(np.square(sample - train_data)))

def get_nearest_neighbours(sample, train_att):
	idx = []
	dist = []

	for i in range(len(train_att)):
		idx.append(i)
		dist.append(distance(sample, train_att[i]))

	for i in range(len(train_att)):	
		for j in range(len(train_att)-1-i):
			if dist[j] > dist[j+1]:
				temp = dist[j]
				dist[j] = dist[j+1]
				dist[j+1] = temp

				temp = idx[j]
				idx[j] = idx[j+1]
				idx[j+1] = temp

	return np.asarray(idx[:k])			

def get_output(test_data, train_att, label):
	output = []

	for i in range(test_data.shape[0]):
		nearest_neighbours = get_nearest_neighbours(test_data[i], train_att)

		label_nn = []
		for j in nearest_neighbours:
			label_nn.append(label[j])

		output.append(1 if np.mean(label_nn)>=0.5 else 0)

	return output	

if __name__ == "__main__":
	train_data = read_train_data(train_file)
	# train attributes and labels
	train_att = []
	label = []

	for i in range(len(train_data)):
		train_att.append(train_data[i][:-1])
		label.append(train_data[i][-1])

	train_att = np.asarray(train_att)
	label = np.asarray(label)	

	#Test data
	test_data = read_test_data(test_file)

	output = get_output(test_data,train_att,label) 

	output_str = ""

	for i in range(len(test_data)):
		if output[i]:
			output_str += str(1) + " "
		else:
			output_str += str(0) + " "

	print(output_str)	

	#Write to output file
	f = open("16EE30025_4.out",'w')
	f.write(output_str)
	f.close()