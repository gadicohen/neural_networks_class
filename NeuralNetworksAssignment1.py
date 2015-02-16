import random
import math
import numpy as np
import matplotlib.pyplot as plt


#Question 1

#Histogram of bins of random 100,000 numbers
x=[]

for i in range(0,1000000):
	rand=random.random()
	x.append(rand)

print np.std(np.array(x)) 

#STANDARD DEVIATION = .2887 which is ~.2886, the stand dev of uniform distribution

bins=[]
for i in range(0,10):
	bins.append([])
for i in range(0,100000):
	bins[int(math.floor(10*x[i]))].append(x[i])

plt.hist(x)
plt.title("Problem 1: Uniform Distribution")
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.show()


#Question 2
#

norm=[]

def polar():
	def gets():
		u1=random.random()
		u2=random.random()
		v1=2*u1-1
		v2=2*u2-1
		s=v1**2+v2**2
		if s>=1:
			v1,v2,s=gets()
		return v1,v2,s

	v1,v2,s=gets()

	if s<1:
		x1=v1*math.sqrt((-2*math.log(s))/s)
		x2=v2*math.sqrt((-2*math.log(s))/s)
		return x1,x2

for i in range(0,50000):
	polartuple=polar()
	norm.append(polartuple[0])
	norm.append(polartuple[1])

plt.hist(norm)
plt.title("Problem 2: Normal Distribution")
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.show()

#Question 3
#Generate normalized random vectors with elements taken from a distribution of mean 0

def make_rand_vector(dims):
    vec = [random.uniform(-1,1) for i in range(dims)] #gauss: distribution of mean 0, standev 1
    mag = sum(x**2 for x in vec) ** .5 #find the magnitude of vector (sqrt of sum of squares of vector values)
    return [x/mag for x in vec] #normalize (/mag)

dotprods=[]
for i in range(0,10000):
	vec1=make_rand_vector(2)
	vec2=make_rand_vector(2)
	dotprods.append(np.inner(vec1,vec2))

print np.mean(np.array(dotprods)),np.std(np.array(dotprods)) 
#mean=-.012245, std=.70488

plt.hist(dotprods)
plt.title("Problem 3: Dot Products Dimension 2")
plt.xlabel("Inner Prod")
plt.ylabel("Frequency")
plt.show()

for a in (10,20,50,100,250,500,1000,20000):
	dotprods=[]
	for i in range(0,10000):
		vec1=make_rand_vector(a)
		vec2=make_rand_vector(a)
		dotprods.append(np.inner(vec1,vec2))
	print a, np.mean(np.array(dotprods)),np.std(np.array(dotprods)) 
	if a<1000:
		plt.hist(dotprods)
		plt.title("Problem 3: Dot Products Dimension "+str(a))
		plt.xlabel("Inner Prod")
		plt.ylabel("Frequency")
		plt.show()

#the dot product of 2 unit vectors on a euclidean plane is the cosine of the angle between them


