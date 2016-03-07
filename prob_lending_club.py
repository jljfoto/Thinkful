import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# Read the data from the file into a panda
loansData = pd.read_csv('/Users/jonathon/Thinkful/loansData.csv')

# Remove rows wil null values
loansData.dropna(inplace=True)

# Check out the data visually
loansData.boxplot(column='Amount.Requested',return_type='axes')
plt.savefig("lc_boxplot_Amount_Requested.png")

# Geenerate a histogram of the loan data
loansData.hist(column='Amount.Requested')
plt.savefig("lc_hist_Amount_Requested.png")

# Generate a QQ plot of the loan data
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("lc_qq_Amount_Requested.png")
