import pandas as pd
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

# variable = something if condition else something_else
#x = 40
#y = 1 if x>200 else 0
#print "\n\n\n\n{0}".format(y)

# http://stackoverflow.com/questions/12555323/adding-new-column-to-existing-dataframe-in-python-pandas
# http://stackoverflow.com/questions/15772617/conditional-statement-in-a-one-line-lambda-function-in-python
loansData['IR_TF'] = loansData['Interest.Rate'].map(lambda x: 1 if x >= 12 else 0)

loansData['Intercept'] = 1.0
loansData['ind_vars'] = loansData.columns

print "\n{0}\n{1}\n{2}\n{3}".format(loansData['IR_TF'][0:5], loansData['Interest.Rate'][0:5],loansData['Intercept'][0:5],ind_vars)

#print "\nIndexes={0}\nColumns={1}".format(loansData.index, loansData.column)
loansData.to_csv('loansData_clean.csv', header=True, index=False)

logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])
result = logit.fit()
coeff = result.params
print(coeff)
