import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np


loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]
cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')), 4))
loansData['Interest.Rate'] = cleanInterestRate

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print "\n{0}".format(f.summary())

plt.figure()
p = loansData['FICO.Score'].hist()
plt.savefig("Fico_Score.png")

plt.figure()
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
plt.savefig("Scatter_Plot.png")

plt.figure()
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.savefig("Scatter_Plot_hist.png")
