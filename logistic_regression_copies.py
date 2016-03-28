from scipy import stats
import numpy as np
import pandas as pd 
import collections
import matplotlib.pyplot as plt
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
#loansData = loansData.to_csv('loansData_clean.csv', header=True, index=False)

## cleaning the file
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x:  round(float(x.rstrip('%')) / 100, 4))


loanlength = loansData['Loan.Length'].map(lambda x: x.strip('months'))
loansData['FICO.Range'] = loansData['FICO.Range'].map(lambda x: x.split('-'))
loansData['FICO.Range'] = loansData['FICO.Range'].map(lambda x: int(x[0]))
loansData['FICO.Score'] = loansData['FICO.Range']

#add interest rate less than column and populate
## we only care about interest rates less than 12%
loansData['IR_TF'] = pd.Series('', index=loansData.index)
#loansData['IR_TF'] = loansData['Interest.Rate'].map(lambda x: True if x < 12 else False)
loansData['IR_TF'] = loansData['Interest.Rate'] < 0.12

#create intercept column
loansData['Intercept'] = pd.Series(1.0, index=loansData.index)

# create list of ind var col names
ind_vars = ['FICO.Score', 'Amount.Requested', 'Intercept'] 

#define logistic regression
logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])

#fit the model
result = logit.fit()

#get fitted coef
coeff = result.params

print coeff
