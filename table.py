from Bio import Entrez   # biopython module for searching on Entrez
from Bio import Medline

import cPickle as pickle
from sys import argv

# Pickle files
script, target, pin = argv
pout =  target.replace("txt", "pkl")

fields =['PMID','FAU','JT','TI','AB'] 

# PMID: 	is the unique identifier number used in PubMed
# FAU:	Full names of the Author(s)
# JT: 	Journal Type
# TI: 	Title of the article
# AB: 	Abstract of the article 

print len(records)

FinalList=[None]*len(records) # creating an empty list

for n in range(len(records)):
	FinalList[n]={} # creating empty dictionary
	for m in range(len(HeaderOutPut)):
		if  str(HeaderOutPut[m]) in records[n]:
			FinalList[n][str(HeaderOutPut[m])]= records[n][str(HeaderOutPut[m])]
		else:
			FinalList[n][str(HeaderOutPut[m])]= 'None'

# for some reason I don't know, it was complaining about 'FAU' for some articles, and hence used if ... else function above. 

print FinalList

# using WriteDictToCSV function to convert the records (now as dictionaries) into csv file
def WriteDictToCSV(csv_file,csv_columns,dict_data):
   try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))    
    return            

# using WriteDictToCSV function defined above 
dict_data=FinalList
csv_columns =HeaderOutPut  # the header of the table

currentPath = os.getcwd()
csv_file = currentPath + "/SystematicSearch.csv"

WriteDictToCSV(csv_file,csv_columns,dict_data)  # the output will be saved automatically in csv folder
