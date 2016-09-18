import numpy as np

##main
n = 100
#open file

f = open('triangle.dat', 'r')

#instantiate list, read from file
list = []
i = 0
for line in f:
	list.append(float(line))
#	print "current reading line: ", i
#	i+=1

#append to an actually useful 2d array
phi = np.zeros((6*n+1,6*n+1))
i=0
for x in range(1,6*n):
	for y in range(1,6*n):
		phi[x,y] = list[i]
		i+=1

del list


for y in range(1,6*n,2):
	
	if y > 1:
		print '\n',
	for x in range(1,6*n,2):
		print phi[x,y] * 1.25,
