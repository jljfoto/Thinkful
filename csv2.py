import csv

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv','r') as inputFile:
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        print("Len {0}: {1}".format(len(line),line))
