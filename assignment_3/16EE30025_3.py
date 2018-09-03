'''
Roll No.       : 16EE30025
Name 	       : Siddhant Haldar
Assignment No. : 3
Instructions:
To run the code, type the following command in the terminal
	
	python 16EE30025_3.py 
'''

import math
import numpy as np 

train_file = "data3.csv"
test_file = "test3.csv"

def read_train_data(filename):
	train_data = []  #to store training data from csv file
	data = []

	#read data from csv
	with open(filename,"r") as csv_data:
		data = csv_data.read().split('\n')

	for i in range(len(data)-1):	
		row = data[i].split(',')
		for i in range(len(row)):
			row[i] = int(row[i])
		train_data.append(row)
	return np.asarray(train_data)

def read_test_data(filename):
	test_data = []  #to store training data from csv file
	data = []

	#read data from csv
	with open(filename,"r") as csv_data:
		data = csv_data.read().split('\n')

	for i in range(len(data)-1):	
		row = data[i].split(',')
		for i in range(len(row)):
			row[i] = int(row[i])
		test_data.append(row)
	return np.asarray(test_data)	


def create_frequency_map(train_att,label):
	freq_map = np.ones((train_att.shape[1], 2, 2))   #(attribute, att=0/1, result=0/1)
	total_prob = np.zeros((2))  #(prob_yes, prob_no)

	for i in range(train_att.shape[0]):
		total_prob[label[i]] += 1
		for j in range(train_att.shape[1]):
			freq_map[j][train_att[i][j]][label[i]] += 1

	total_prob /= label.shape[0]
	for j in range(train_att.shape[1]):
		freq_map[j,:,0] /= np.sum(freq_map[j,:,0])
		freq_map[j,:,1] /= np.sum(freq_map[j,:,1])

	return total_prob, freq_map	

def predict(test_data, freq_map, total_prob):
	output_str = ""
	for i in range(test_data.shape[0]):
		prob_no = float(total_prob[0])
		prob_yes = float(total_prob[1])

		for j in range(test_data.shape[1]):
			prob_no *= freq_map[j][test_data[i][j]][0]
			prob_yes *= freq_map[j][test_data[i][j]][1]

		sum_prob = prob_yes + prob_no
		prob_yes /= sum_prob
		prob_no /= sum_prob	

		if prob_yes > prob_no:
			output_str += str(1)+" "
		else:
			output_str += str(0)+" "	

	print(output_str)

	#Write to output file
	f = open("16EE30025_3.out",'w')
	f.write(output_str)
	f.close()

if __name__ == "__main__":
	train_data = read_train_data(train_file)
	# train attributes and labels
	train_att = []
	label = []

	for i in range(len(train_data)):
		train_att.append(train_data[i][:8])
		label.append(train_data[i][8])

	train_att = np.asarray(train_att)
	label = np.asarray(label)

	total_prob, freq_map = create_frequency_map(train_att, label)

	# Test
	test_data = read_test_data(test_file)

	predict(test_data, freq_map, total_prob)

