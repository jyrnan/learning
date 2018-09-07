def jc(n):
	result = 1
	if n ==	 1:
		result = 1
	else:
		result = n * jc(n-1)
	return result
	
print(jc(5))
