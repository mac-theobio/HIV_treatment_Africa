
import cPickle as pickle
from sys import argv
import numpy as np

import csv 
import os

# Pickle files
script, target, pin = argv
pout =  target.replace("txt", "pkl")
csv_file = target.replace("txt", "csv")

fields =['PMID','FAU','JT','TI','AB'] # selected keys or items from the search result. The reason for choosing some items is 1) to only download items of interest. 2) some articles have different details. Example an article may have 20 items including 'PMID','FAU','JT','TI','AB'. Whereas, another article may have less or more than 20 items. By doing this we make the number of items constant. ['PMID','FAU','JT','TI','AB' are items found for every article]. 

# PMID: 	is the unique identifier number used in PubMed
# FAU:	Full names of the Author(s)
# JT: 	Journal Type
# TI: 	Title of the article
# AB: 	Abstract of the article 

## Make the pickle: "rb" is read binary
records = pickle.load(open( pin, "rb" ) )
print len(records), "records read"


# Make a dictionary with selected fields
dict=[None]*len(records) # creating an empty list
fields=['PMID','TI','JT']  
for n in range(len(records)):
	dict[n]={} # creating empty dictionary
	for m in range(len(fields)):
		if  str(fields[m]) in records[n]:
			dict[n][str(fields[m])]= records[n][str(fields[m])]
		else:
			dict[n][str(fields[m])]= 'None'

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
dict_data=dict
csv_columns =fields  # the header of the table

WriteDictToCSV(csv_file,csv_columns,dict_data)  # the output will be saved automatically in csv folder

print "Wrote to csv file", csv_file
