with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv','rU') as inputFile:
    for line in inputFile:
        line = line.rstrip().split(',')
        print(line)

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv','rU') as inputFile:
    for line in inputFile:
        line = line.rstrip().split(',')
        print(len(line))

