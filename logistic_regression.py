import pandas as pd
import statsmodels.api as sm
import numpy as np

# Linear Model is:    InterestRate = b + a1(FICOScore) + a2(LoanAmount)
#     in our program: InterestRate = y + x1(FICOScore) + x2(LoanAmount)

def logistic_function(FICOScore,LoanAmount,coeff):
	p = 1/(1+math.exp(coeff[0]+coeff[2]*FICOScore+coeff[1]*LoanAmount))
	return p

# Data source
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Clean up data
loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]
loansData['Interest.Rate']  = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%'))/100, 4))

# http://stackoverflow.com/questions/12555323/adding-new-column-to-existing-dataframe-in-python-pandas
# http://stackoverflow.com/questions/15772617/conditional-statement-in-a-one-line-lambda-function-in-python
# http://stackoverflow.com/questions/34668868/unable-to-run-logistic-regression-due-to-perfect-separation-error
loansData['IR_TF'] = loansData['Interest.Rate'] > .12
loansData['Intercept'] = 1.0

ind_vars = ['FICO.Score', 'Amount.Requested', 'Intercept']

# http://blog.yhat.com/posts/logistic-regression-and-python.html
logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])
result = logit.fit()
print result.summary()
coeff = result.params

loansData.to_csv('loansData_clean.csv', header=True, index=False)
print(coeff)
