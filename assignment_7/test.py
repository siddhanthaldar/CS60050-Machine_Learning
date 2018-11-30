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
		# print(c_old)

		error = self.dist(c, c_old)

		count = 0
		while error > 0.005:
			# if count>=1000:
			# 	break
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
					# print(j,dist)
					if dist<min_dist:
						min_dist = dist
						seg_num = j		
				self.segment_add.append(seg_num)
				self.segments[seg_num].append(i)
				# print(seg_num)
			# for i in range(self.k):
			# 	if len(self.segments[i]) == 0:
			# 		return	

			# print(self.segments)
			for i in range(self.k):
				point = np.zeros(8)
				for j in self.segments[i]:
					# print(j.shape)
					point += j
				c[i] = point/(len(self.segments[i]))
				# print(c[i])

			error = self.dist(c, c_old)
			c_old = c
			count += 1
			# print(error)


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

		# print(c_old)
		error = self.dist(c, c_old)
		
		count = 0
		while error != 0:
			c = c_old
			self.segments = []
			self.segment_add = []
			for i in range(k):
				self.segments.append([])		

			min_dist = 9999
			seg_num = -1				
			for i in self.train_data:
				for j in range(c_old.shape[0]):	
					dist = self.dist(i,c_old[j])
					if dist<min_dist:
						min_dist = dist
						seg_num = j		
				self.segment_add.append(seg_num)
				self.segments[seg_num].append(i)
				# print(seg_num)

			for i in range(self.k):
				if len(self.segments[i]) == 0:
					return	

			for i in range(self.k):
				point = np.zeros(8)
				for j in self.segments[i]:
					# print(j.shape)
					point += j
				c[i] = point/(len(self.segments[i]))
			# print(c)
			# print(c_old)

			error = self.dist(c, c_old)
			c_old = c
			# print(c)
			# print(c_old)

			count += 1
			# print(str(count)+"    Error : "+ str(error))
			# if count >3:
			#  break		
						
	# def kmeans(self):
	# 	self.segments = []
	# 	self.centroid_coords = []
	# 	self.centroids_old = []
	# 	random.seed(1)
	# 	for i in range(k):
	# 		# self.segments.append([])
	# 		a = random.randint(0, self.train_data.shape[0]-1)
	# 		while a in self.centroid_coords:
	# 			a = random.randint(0, self.train_data.shape[0]-1)
				
	# 		self.centroid_coords.append(a)
	# 		# self.segments[i].append(self.train_data[a])
	# 		self.centroids_old.append(self.train_data[a])
	# 	self.centroids = self.centroids_old

	# 	for i in range(iterations):
	# 		print(i)
	# 		self.segments = []
	# 		for i in range(k):
	# 			self.segments.append([])
	# 			self.segments[i].append(self.centroids_old[i])
	# 		self.segment_add = []

	# 		for i in range(self.train_data.shape[0]):
	# 			# if self.train_data[i].all()==self.centroids_old[0].all() or self.train_data[i].all()==self.centroids_old[1].all() :
	# 			# 	continue

	# 			dist = []

	# 			for j in range(len(self.centroids)):
	# 				dist.append(np.linalg.norm(self.centroids_old[j] - self.train_data[j]))
	# 				print(dist[j])
	# 			segment_num = dist.index(min(dist))
	# 			self.segments[segment_num].append(self.train_data[i])	
	# 			c = np.zeros(self.train_data[i].shape) 	
	# 			for j in range(len(self.segments[segment_num])):
	# 				c += self.segments[segment_num][j]

	# 			self.centroids[segment_num] = c / j

	# 			self.segment_add.append(segment_num)
	# 			print("abc")

	# 		c_dist = 0
	# 		for j in range(len(self.centroids)):
	# 			c_dist += np.linalg.norm(self.centroids_old[j] - self.centroids[j])
	# 		print(c_dist)		
	# 		if c_dist == 0:
	# 			break
	# 		self.centroids_old = self.centroids	

				
	# def kmeans(self):
	# 	self.segments = []
	# 	self.centroid_coords = []
	# 	self.centroids = []
	# 	random.seed(1)
	# 	for i in range(k):
	# 		self.segments.append([])
	# 		a = random.randint(0, self.train_data.shape[0]-1)
	# 		while a in self.centroid_coords:
	# 			a = random.randint(0, self.train_data.shape[0]-1)
				
	# 		self.centroid_coords.append(a)
	# 		self.segments[i].append(self.train_data[a])
	# 		self.centroids.append(self.train_data[a])

	# 	self.segment_add = []

	# 	for i in range(self.train_data.shape[0]):
	# 		# if i in self.centroid_coords:
	# 		# 	continue

	# 		dist = []

	# 		for j in range(len(self.centroid_coords)):
	# 			dist.append(np.linalg.norm(self.centroids[j] - self.train_data[j]))
	# 			# print(dist[j])
	# 		segment_num = dist.index(min(dist))
	# 		self.segments[segment_num].append(self.train_data[i])	
	# 		c = np.zeros(self.train_data[i].shape) 	
	# 		for j in range(len(self.segments[segment_num])):
	# 			c += self.segments[segment_num][j]

	# 		self.centroids[segment_num] = c / j

	# 		self.segment_add.append(segment_num)


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

