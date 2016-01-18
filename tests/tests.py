from myPackage import myModule

def test_fahr2Kelv():
	'''
	test nominal behaviour of fahr2Kelv
	'''

	assert myModule.Fahr2Kelvin(32) == 273.15
