from Bio import Entrez   
from Bio import Medline
import numpy as np
import cPickle as pickle
from sys import argv

Entrez.email = "jdushoff@gmail.com"  

script, target, filename = argv

txt = open(filename)

SearchTerm = txt.read()

# Get Pubmed IDs matching SearchTerm
handle = Entrez.esearch(db="pubmed", term=SearchTerm, retmax=1000) 

## ADD a warning if retmax articles are returned

record = Entrez.read(handle)
idlist = record["IdList"]

## For humans, just the number of records
print len(idlist)

## For pipeline, save all the pubmed IDs
target =  target.replace("txt", "pkl")
pickle.dump(idlist, open( target, "wb" ) )

