'''
Roll No.       : 16EE30025
Name 	       : Siddhant Haldar
Assignment No. : 7
Instructions:
To run the code, type the following command in the terminal
	
	python 16EE30025_7.py 

'''

import math
import numpy as np 
import random

train_file = "data7.csv"
k = 2
		
class kmeans_classifier:
	def __init__(self,k):
		self.k = k
		self.iterations = 1000

	def read_train_data(self, filename):
		self.train_data = np.genfromtxt(train_file, delimiter=',')

	def dist(self, a, b):
	 return np.linalg.norm(a-b)

	def kmeans2(self):
		c_index = []
		c_old = np.zeros((self.k,8))
		for i in range(self.k):
	 		a = random.randint(0, self.train_data.shape[0]-1)
	 		while a in c_index:
				a = random.randint(0, self.train_data.shape[0]-1)
			c_index.append(a)
			c_old[i] = self.train_data[a]
		c = np.zeros(c_old.shape)

		error = self.dist(c, c_old)

		while error > 0.001:
			c = c_old
			self.segments = []
			self.segment_add = []
			for i in range(k):
				self.segments.append([])		

			for i in self.train_data:
				min_dist = 9999
				seg_num = -1				
				for j in range(c_old.shape[0]):	
					dist = self.dist(i,c_old[j])
					if dist<min_dist:
						min_dist = dist
						seg_num = j		
				self.segment_add.append(seg_num)
				self.segments[seg_num].append(i)

			for i in range(self.k):
				point = np.zeros(8)
				for j in self.segments[i]:
					point += j
				c[i] = point/(len(self.segments[i]))

			error = self.dist(c, c_old)
			c_old = c


	def print_segments(self):			
		output_str = ""
		for i in self.segment_add:
			output_str += str(i) + " "
		
		print(output_str)
		#Write to output file
		f = open("16EE30025_7.out",'w')
		f.write(output_str)
		f.close()
		

if __name__ == "__main__":
	a = kmeans_classifier(k)
	a.read_train_data(train_file)
	a.kmeans2()
	a.print_segments()

