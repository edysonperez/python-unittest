def	valid(intro = 0):
	CORRECTO = True
	while CORRECTO == True:
		intro = raw_input("Ingrese un numero")
		if intet(intro) == True:
			CORRECTO = False
		else:
			print "Ingrese Valido"
			CORRECTO = True
	multi (int(intro))
	return intro

def intet(intro):
	try:
		intro = int(intro)
		return True
 	except ValueError:
		return False
	
def multi(num = 0):
	for mul in range(1,11):
		total = num * mul
		if __name__ == "__main__":
			print str(num) + " * " + str(mul) + " = " + str(total)  
	return total

if __name__ == "__main__":
	valid()
	
		
