from Bio import Entrez   
from Bio import Medline
import numpy as np
from sys import argv

import csv
import os

Entrez.email = "jdushoff@gmail.com"  

script, filename = argv

txt = open(filename)

SearchTerm = txt.read()

# Get Pubmed IDs matching SearchTerm
handle = Entrez.esearch(db="pubmed", term=SearchTerm, retmax=1000) 

## ADD a warning if retmax articles are returned

record = Entrez.read(handle)

idlist = record["IdList"]
print idlist

# This returns a python list containing all of the PubMed IDs of articles related to the search concepts. i.e. it will display as [18680603', '18665331', '18661158', '18627489' ... ]

# ===========  ======================= 

# Now that we've got the PubMed IDs, 
# The following commands will give us the corresponding Medline records and extract the information from them. Here, we'll download the Medline records in the Medline flat-file format, and use the Bio.Medline module to parse them:

handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",retmode="text")
records = Medline.parse(handle)

records = list(records)
#print records

np.savetxt('SystematicSearch.txt', records, fmt="%s") # this saves in a text format

# manupilating dictionaries 

HeaderOutPut=['PMID','FAU','JT','TI','AB']  # selected keys or items from the search result. The reason for choosing some items is 1) to only download items of interest. 2) some articles have different details. Example an article may have 20 items including 'PMID','FAU','JT','TI','AB'. Whereas, another article may have less or more than 20 items. By doing this we make the number of items constant. ['PMID','FAU','JT','TI','AB' are items found for every article]. 

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
