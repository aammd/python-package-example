kelvinFreezing = 273.15

def Fahr2Kelvin(temp):
	''' 
	take fahr temperature and return it as kelvin
	'''

	kelvin = 5./9.*(temp - 32) + kelvinFreezing

	return kelvin