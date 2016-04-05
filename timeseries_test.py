import pandas as pd
import statsmodels.api as sm
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf, pacf

# Data source
df = pd.read_csv('https://raw.githubusercontent.com/Thinkful-Ed/curric-data-001-data-sets/master/loans/loansData.csv')
df['Interest.Rate']  = df['Interest.Rate'].map(lambda x: round(float(x.rstrip('%'))/100, 4))
df['annual_inc'] = df['Monthly.Income'] * 12
df['Intercept'] = 1.0
df['Interest_Rate'] = df['Interest.Rate']
df['Home_Ownership'] = df['Home.Ownership'] == "MORTGAGE"

# http://statsmodels.sourceforge.net/devel/_modules/statsmodels/graphics/tsaplots.html


