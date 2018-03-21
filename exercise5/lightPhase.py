#Make a plot of the phase velocity of light as a function of refractive indexes n between 1 and 10
from numpy import *
from matplotlib.pyplot import *

n = linspace(1,10,1e3)

def phase(n):
	return 299792458.0/n


plot(n,phase(n))
title('Phase velocity of light as a function of refractive index')
xlabel('$n$')
ylabel('$v_p = \\frac{c}{n}$',rotation=0)
show()