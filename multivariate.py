import pandas as pd
import statsmodels.api as sm
import numpy as np
import statsmodels.formula.api as smf

# Data source
df = pd.read_csv('https://raw.githubusercontent.com/Thinkful-Ed/curric-data-001-data-sets/master/loans/loansData.csv')
df['Interest.Rate']  = df['Interest.Rate'].map(lambda x: round(float(x.rstrip('%'))/100, 4))
df['annual_inc'] = df['Monthly.Income'] * 12
df['Intercept'] = 1.0
df['Interest_Rate'] = df['Interest.Rate']
df['Home_Ownership'] = df['Home.Ownership'] == "MORTGAGE"

#print df['annual_inc'].head(), df['Interest.Rate'].head(), df['Home.Ownership'].head(), df['Intercept'].head(), df['Home_Owner'].head()

# annual income and Interest Rate
est = smf.ols(formula='annual_inc ~ Interest_Rate', data=df).fit()
print est.summary()

# annual income to Interest Rate and Home Ownership
est = smf.ols(formula='annual_inc ~ Interest_Rate + Home_Ownership', data=df).fit()
print est.summary()

# annual income to Home Ownership
est = smf.ols(formula='annual_inc ~ Home_Ownership', data=df).fit()
print est.summary()
