import pandas as pd
import statsmodels.api as sm
import numpy as np

# Linear Model is:    InterestRate = b + a1(FICOScore) + a2(LoanAmount)
#     in our program: InterestRate = y + x1(FICOScore) + x2(LoanAmount)

# Data source
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

def logistic_functioni():
    

# Clean up data
loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]
cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')), 4))
loansData['Interest.Rate'] = cleanInterestRate

# http://stackoverflow.com/questions/12555323/adding-new-column-to-existing-dataframe-in-python-pandas
# http://stackoverflow.com/questions/15772617/conditional-statement-in-a-one-line-lambda-function-in-python
loansData['IR_TF'] = loansData['Interest.Rate'].map(lambda x: 1 if x >= 12 else 0)

loansData['Intercept'] = 1.0


ind_vars = loansData.columns
additional = pd.DataFrame({'ind_vars': ind_vars})
new = pd.concat([loansData, additional], axis=1)
#print "\nnew={0}\n\n\n".format(new['ind_vars'])
#print "\nn{0}\n\n\n".format(list(new.columns.values))

#print "\n{0}\n{1}\n{2}\n{3}".format(loansData['IR_TF'][0:5], loansData['Interest.Rate'][0:5],loansData['Intercept'][0:5],loansData['ind_vars'][0:5])

#print "\nIndexes={0}\nColumns={1}".format(loansData.index, loansData.column)
loansData.to_csv('loansData_clean.csv', header=True, index=False)

logit = sm.Logit(loansData['IR_TF'], new['ind_vars'])
result = logit.fit()
coeff = result.params
print(coeff)
