import pandas as pd

input_dataframe = pd.read_csv('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv')

print(input_dataframe)
#print(input_dataframe['Africa'][0])
print(input_dataframe[10:40])
