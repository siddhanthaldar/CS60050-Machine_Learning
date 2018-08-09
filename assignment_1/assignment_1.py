'''
Roll No.       : 16EE30025
Name 	       : Siddhant Haldar
Assignment No. : 1
'''

data = []  #to store data from csv file

#read data from csv
with open('data1.csv',"r") as csv_data:
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




# count = 0		
# final_attributes = []

# for i in range(len(h)):
# 	if h[i]!=-2:
# 		count += 1
# 		final_attributes.append(i+1)

# res_string = str(count)

# for x in final_attributes:
# 	if(h[x-1] == 1):
# 		res_string += "," + str(x)
# 	else:
# 		res_string += ",-" + str(x)

# print(res_string)			
