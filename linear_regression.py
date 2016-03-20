import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

# Linear Model is:    InterestRate = b + a1(FICOScore) + a2(LoanAmount)
#     in our program: InterestRate = y + x1(FICOScore) + x2(LoanAmount)

# Data source
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Clean up data
loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]
cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')), 4))
loansData['Interest.Rate'] = cleanInterestRate

# Extract columes we want to work with
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# Reshape the data
# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# Put the two columns together to create an input matrix 
x = np.column_stack([x1,x2])

# Create the linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

# Print the Model
print "\n{0}".format(f.summary())

# Charts gnerated from first part of exercise
plt.figure()
p = loansData['FICO.Score'].hist()
plt.savefig("Fico_Score.png")

plt.figure()
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
plt.savefig("Scatter_Plot.png")

plt.figure()
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.savefig("Scatter_Plot_hist.png")
