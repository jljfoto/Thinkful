def F(n):
    if n < 2:
        return n
    else:
        ret_val= F(n-2) + F(n-1)
#	print "entered with {0} returning {1}".format(n,ret_val)
	return ret_val

# num = input("Enter the fib num: ")
for n in range(1,30):
        fib_result=F(n)
        if ((fib_result % 3 == 0) and (fib_result % 5 == 0)):
           FizzBuzz="FizzBuzz"
	elif (fib_result % 3 == 0):
	   FizzBuzz="Fizz"
	elif (fib_result % 5 == 0):
           FizzBuzz="Buzz"
        else:
           FizzBuzz=""
	print "The fibonacci of {0} is {1}: {2}".format(n,fib_result, FizzBuzz)
