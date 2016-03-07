# Using the search strategies indicated above, we first check how many of such articles there are:

# adopted from http://biopython.org/DIST/docs/tutorial/Tutorial.html

from Bio import Entrez   # biopython module for searching on Entrez
from Bio import Medline
import numpy as np
# import pandas as pd  # will help to save the array in CSV format


import csv
import os
Entrez.email = "bewketu.bekele@gmail.com"   # put your email address

# below are four different search concepts (using boolean arguments). Uncomment only one of them to see the output of the search. 

SearchTerm="((Human+immunodeficiency+virus[tiab] OR acquired+immunodeficiency+syndrome[tiab] OR HIV[tiab] OR AIDS[tiab] OR HIV/AIDS[tiab]) AND (Swaziland[tiab] OR Botswana[tiab] OR Lesotho[tiab] OR South+Africa[tiab] OR Zimbabwe[tiab] OR Namibia[tiab] OR Zambia[tiab] OR Mozambique[tiab] OR Malawi[tiab] OR Uganda[tiab] OR Equatorial+Guinea[tiab] OR Kenya[tiab] OR Tanzania[tiab] OR sub+Saharan+Africa[tiab] OR sub-Saharan+Africa[tiab]) AND (treatment+failure[tiab] OR switch[tiab] OR switches[tiab] OR switching[tiab] OR first+line[tiab] OR first-line[tiab] OR second+line[tiab] OR second-line[tiab] OR  lost+to+follow+up[tiab] OR lost+to+follow-up[tiab] OR loss+to+follow+up[tiab] OR loss+to+follow-up[tiab] OR dropout[tiab] OR drop-out[tiab] OR dropouts[tiab] OR drop +out[tiab] OR drop+outs[tiab])) AND ((2010/01/01[PDAT] : 2015/12/31[PDAT]) AND humans[MeSH Terms] AND English[lang])"

# the equivalent search strategy on PubMed is 
# ((("Human immunodeficiency virus"[tiab] OR "acquired immunodeficiency syndrome"[tiab] OR HIV[tiab] OR AIDS[tiab] OR "HIV/AIDS"[tiab]) AND (Swaziland[tiab] OR Botswana[tiab] OR Lesotho[tiab] OR "South Africa"[tiab] OR Zimbabwe[tiab] OR Namibia[tiab] OR Zambia[tiab] OR Mozambique[tiab] OR Malawi[tiab] OR Uganda[tiab] OR "Equatorial Guinea"[tiab] OR Kenya[tiab] OR Tanzania[tiab] OR "sub Saharan Africa"[tiab] OR "sub-Saharan Africa"[tiab])) AND ("treatment failure"[tiab] OR switch[tiab] OR switches[tiab] OR switching[tiab] OR "first line"[tiab] OR "first-line"[tiab] OR "second line"[tiab] OR "second-line"[tiab] OR "lost to follow up"[tiab] OR "lost to follow-up"[tiab] OR "loss to follow up"[tiab] OR "loss to follow-up"[tiab] OR dropout[tiab] OR "drop-out"[tiab] OR dropouts[tiab] OR "drop out"[tiab] OR "drop outs"[tiab])) AND (("2010/01/01"[PDAT] : "2015/12/31"[PDAT]) AND "humans"[MeSH Terms] AND English[lang]) 

handle = Entrez.egquery(term=SearchTerm)

record = Entrez.read(handle)
for row in record["eGQueryResult"]:
	if row["DbName"]=="pubmed":
		print row["Count"]		# prints the total number of articles (suppose N) with the same search concepts

# Now we use the Bio.Entrez.efetch function to download the PubMed IDs of these articles:
handle = Entrez.esearch(db="pubmed", term=SearchTerm, retmax=1000)  # put N=the maximum number of articles you will like to download. We put 1000 just as max.

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










