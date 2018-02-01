from numpy import *
from matplotlib.pyplot import *
from numpy import *

def get_data(txtfile):
	with open(txtfile,"r") as infile:
		lines = infile.readlines()
		data = zeros([len(lines),len(lines[0])])
		for i in range(len(data)):
			data[i][::] = lines[i].split()

		"""data = {}
		identifiers = infile.readline().split()
		for identifier in identifiers:
			data[identifier] = []

		lines = infile.readlines()
		for line in lines: 
			values = line.split()
			for identifier,value in zip(identifiers,values):
				data[identifier].append(float(value))
		for identifier in identifiers:
			data[identifier] = array(data[identifier])
		"""
	return data

def dotProd(u,v):
	prod = 0
	for i in range(len(u)):
		prod = prod + u[i] * v[i]
	return prod

def intens(atoms,dk): #atoms is a nested list with form [[Z],[x],[y],[z]]
	I = 0
	for i in range(len(atoms)):
		#print("looping %.i times" % (len(atoms)))
		Z = atoms[i][0]
		I = I + Z*e**(-2*pi*1j*dotProd(dk,atoms[i][1:]))
		I = (abs(I))**2
	return I
lattice = array([ [2,1,1,1] ])
x = intens(lattice,[1,1,1])

y = get_data("fcc")
print(y)