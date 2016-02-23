import collections
population_dict = collections.defaultdict(int)

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    Total2010pop=0
    for line in inputFile:
	line = line.rstrip().split(',')
        line[5] = float(line[5])
        line[7] = float(line[7])
	if line[1] == 'Total National Population':
	   population_dict[line[0]] += line[5]/line[7]
           print "Country-> {0}  Population-> {1}  Landarea-> {2}  Density-> {3}".format(line[0],line[5],line[7],float(line[5]/line[7]))

with open('national_population_density.csv','w') as outputFile:
    outputFile.write('continent,2010_population\n')
    for k,v in population_dict.iteritems():
        outputFile.write(k + ',' + str(v) + '\n')
