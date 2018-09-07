step = []
def hanoi(n, x, y, z):
	global step
	if n == 1:
		step.append(x+'>'+z)
		#print(str(x), ' > ', str(z))
	else:
		hanoi((n-1), x, z, y)
		step.append(x+'>'+z)
		#print(str(x), ' > ', str(z))
		hanoi((n-1), y, x, z)
		
	return step
step = hanoi(25, 'x', 'y', 'z')
print(len(step))

