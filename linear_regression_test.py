import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

print "{0}".format(loansData['Interest.Rate'][0:5])
print "\n{0}".format(loansData['Loan.Length'][0:5])
print "\n{0}".format(loansData['FICO.Range'][0:5])
print "\n--------------"

loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]
print "\n{0}".format(loansData['FICO.Range'][0:5])
print "\n{0}".format(loansData['FICO.Score'][0:5])
print "\n--------------"

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))


loansData['Interest.Rate'] = cleanInterestRate
loansData['Loan.Length'] = cleanLoanLength
loansData['FICO.Range'] = cleanFICORange

print "\n{0}".format(cleanInterestRate[0:5])
print "\n{0}".format(cleanLoanLength[0:5])
print "\n{0}".format(cleanFICORange[0:5])
print "\n--------------"

plt.figure()
p = loansData['FICO.Score'].hist()
#p = cleanFICORange.values[0][0]
print "\n{0}".format(cleanFICORange[:0])
plt.savefig("Fico_Score.png")

plt.figure()
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
plt.savefig("Scatter_Plot.png")

plt.figure()
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.savefig("Scatter_Plot_hist.png")
