import pandas as pd
import matplotlib.pyplot as plt


loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

print "{0}".format(loansData['Interest.Rate'][0:5])
print "\n{0}".format(loansData['Loan.Length'][0:5])
print "\n{0}".format(loansData['FICO.Range'][0:5])

def f(x):
    '''This function takes x as a parameter and returns x squared'''
    return x**2

print "\n{0}".format(f(9))
g = lambda x: x**2
print "\n{0}".format(g(9))


l = lambda y: map(int, y.split())
x = loansData['Interest.Rate'][0:5].values[1]
print "\n{0} {1}".format(l(loansData['FICO.Range'][1]))
print "\n{0}".format(x)

