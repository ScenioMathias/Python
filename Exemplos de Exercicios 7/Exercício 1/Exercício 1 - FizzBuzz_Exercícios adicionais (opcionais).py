def fizzbuzz(x):
	if (x % 3 == 0) and (x % 5 !=0):
		return ('Fizz')
	elif (x % 5 == 0) and (x % 3 !=0):
		return ('Buzz')
	else:
		if (x % 3 == 0) and (x % 5 == 0):
			return ('FizzBuzz')
		else:
			return (x)
