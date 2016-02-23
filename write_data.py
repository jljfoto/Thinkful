import collections
population_dict = collections.defaultdict(int)
with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    Total2010pop=0
    for line in inputFile:
	line = line.rstrip().split(',')
        line[5] = int(line[5])
	if line[1] == 'Total National Population':
	   population_dict[line[0]] += line[5]
           Total2010pop += line[5]
           print "{0}  {1}".format(line[0],line[5])
    print "Total 2010 Populattion was {0}".format(Total2010pop)
with open('national_population.csv','w') as outputFile:
    outputFile.write('continent,2010_population\n')
    for k,v in population_dict.iteritems():
        outputFile.write(k + ',' + str(v) + '\n')
