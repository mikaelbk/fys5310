from numpy import *
from matplotlib.pyplot import *
from numpy import *

def get_data(txtfile):
	with open(txtfile,"r") as infile:
		lines = infile.readlines()
		#filling array
		matrix = zeros([len(lines),4])
		for i in range(len(lines)):
			for j in range(4):
				matrix[i][j] = float(lines[i].split()[j])
	return matrix

def intens(atoms,dk): #atoms is a nested list with form [[Z],[x],[y],[z]]
	I = 0
	for i in range(len(atoms)):
		#print("looping %.i times" % (len(atoms)))
		Z = atoms[i][0]
		I = I + Z*e**(-2*pi*1j*dot(dk,atoms[i][1:]))
	I = (abs(I))**2
	return I

atoms = get_data("fcc")
n = 200
ri = 0
rf = 10
grid = linspace(ri,rf,n)
#xx, yy = meshgrid(linspace(0,0.9,n),linspace(0,0.9,n))
kLattice = zeros([n,n])
for i in range(n):
	for j in range(n):
		kLattice[i][j] = intens(atoms,[grid[i],grid[j],0.5])

#plotting
imshow(kLattice,interpolation="nearest",extent=[ri,rf,ri,rf])
colorbar()
show()