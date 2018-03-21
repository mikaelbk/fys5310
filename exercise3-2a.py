from math import *

me = 9.10938215E-31	#electron mass
e = 1.60217657E-19	#elementary charge
c = 299792458		#speed of light
A = me*c**2/e		#common factor ~0.5MeV
r = 

def lor(v):
	return 1.0 / (sqrt(1-((v/float(c))**2)))

def v(u):
	return c*(sqrt( 1-(A/(u+A))**2 ))

def b(r,v):
	return me*v/(r*e)

for i in [60E3,100E3,200E3,300E3]:
	print(lor(v(i)))