# fact

def fact(n):
   if n<=1:
      return 1
   else: 
     return n * fact(n-1)

n = input("Enter the fact num: ")
print "The factorial of {0} is {1}".format(n,fact(n))
