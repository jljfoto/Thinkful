import collections
population_dict = collections.defaultdict(int)

# get the data from the file
with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    Total2010pop=0
    Total2100pop=0
    for line in inputFile:
	line = line.rstrip().split(',')
        line[5] = int(line[5])
        line[6] = float(line[6])
	if line[1] == 'Total National Population':
           Total2010pop += line[5]
           Total2100pop += line[6]
    print "Total 2010 Populattion was {0}".format(Total2010pop)
    print "Total 2100 Populattion was {0}".format(Total2100pop)
    print "Difference in population between 2010 and 2100 is {0}".format(Total2100pop-Total2010pop)
