# The critical acceleration voltage is defined as the voltage giving an electron velocity equal to the phase velocity of a material with refractive index n. Make a plot of the critical acceleration voltage as a function of n.

from numpy import *
from matplotlib.pyplot import *

n = linspace(1,10,1e3)

def phase(n):
	return 299792458.0/n

