'''
Roll No.       : 16EE30025
Name 	       : Siddhant Haldar
Assignment No. : 2
Instructions:
To run the code, type the following command in the terminal
	
	python 16EE30025_2.py 
'''

import math
import numpy as np 

train_file = "data2.csv"
test_file = "test2.csv"
global att_used
att_used = []

class Node:

	def __init__(self, train_att, label):
		self.left = None        # for zero
		self.right = None       # for one

		if entropy(label) == 0:
			if label[0] == 1:
				self.att_num = 'Y'   # attribute to be compare at this node
			elif label[0] == 0:
				self.att_num = 'N'	

		else:
			self.att_num = max_info_gain(train_att, label)	
			att_used.append(self.att_num)
		

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


def entropy(labels):
	size = len(labels)
	if size == 0: 
		return 0

	prob_one = 0
	prob_zero = 0

	for i in labels:
		if i == 1:
			prob_one += 1

		elif i == 0:
			prob_zero += 1

	prob_one = float(prob_one)/size
	prob_zero = float(prob_zero)/size

	if prob_zero == 0 or prob_one == 0:
		entropy = 0

	else:
		entropy = -prob_zero*math.log(prob_zero,2) - prob_one*math.log(prob_one,2)

	return entropy

def info_gain(train_data,label,att_idx):
	total_entropy = entropy(label)
	att = []
	for i in range(len(train_data)):	
		att.append(train_data[i][att_idx])

	att_one = []
	att_zero = []
	att_one_count = 0
	att_zero_count = 0
		
	for i in range(len(train_data)):
		if train_data[i][att_idx] == 0:
			att_zero_count += 1
			att_zero.append(label[i])

		elif train_data[i][att_idx] == 1:
			att_one_count += 1
			att_one.append(label[i])

	gain = total_entropy - (float(att_zero_count)/len(label))*entropy(att_zero) - (float(att_one_count)/len(label))*entropy(att_one)

	return gain

def max_info_gain(train_att,label):  # att_used : list of attributes already considered
	idx = -1
	max_gain = -1
	att_idx = []  #list of attributes to be considered

	for i in range(len(train_att[0])):
		if i not in att_used:
			att_idx.append(i)

	for i in att_idx:
		gain = info_gain(train_att,label,i)
		if gain > max_gain:
			max_gain = gain
			idx = i
	
	return idx         #return attribute column index	

def create_tree(node, train_att, label):
	if len(att_used) >= len(train_att[0]):
		return

	elif node.att_num == 'Y' or node.att_num == 'N':
		return	

	else:	
		left_data = np.reshape(np.extract(np.repeat(np.expand_dims((train_att[:,node.att_num] == 0), axis=1), len(train_att[0]), axis=1), train_att), [-1,train_att.shape[1]])
		left_label = np.reshape(np.extract(train_att[:,node.att_num] == 0, label), [-1,1])
		right_data = np.reshape(np.extract(np.repeat(np.expand_dims((train_att[:,node.att_num] == 1), axis=1), len(train_att[0]), axis=1), train_att), [-1,train_att.shape[1]])
		right_label = np.reshape(np.extract(train_att[:,node.att_num] == 1, label), [-1,1])		

	node.left = Node(left_data, left_label)
	node.right = Node(right_data, right_label)
	create_tree(node.left, left_data, left_data)
	create_tree(node.right, right_data, right_label)

	return node

def predict(root, test_sample):
	node = root
	while(node.att_num != 'Y' and node.att_num != 'N'):
		if(test_sample[node.att_num] == 0):
			node = node.left
		else: 
			node = node.right

	# print(node.att_num)			
	return node.att_num


if __name__=="__main__":
	train_data = read_train_data(train_file)
	train_att = []
	label = []

	for i in range(len(train_data)):
		train_att.append(train_data[i][:8])
		label.append(train_data[i][8])

	train_att = np.asarray(train_att)
	label = np.asarray(label)	

	root = Node(train_att, label)
	root = create_tree(root, train_att, label)


	# predict(root, train_data[21])
	
	# Test
	test_data = read_test_data(test_file)
	output_str = ""

	for i in range(len(test_data)):
		if predict(root, test_data[i]) == 'N':
			output_str += str(0) + " "
		else:
			output_str += str(1) + " "

	print(output_str)	

	#Write to output file
	f = open("16EE30025_2.out",'w')
	f.write(output_str)
	f.close()