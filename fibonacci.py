def F(n):
    if n < 2:
        return n
    else:
        ret_val= F(n-2) + F(n-1)
	print "entered with {0} returning {1}".format(n,ret_val)
	return ret_val

num = input("Enter the fib num: ")
print "The fibonacci of {0} is {1}".format(num,F(num))
