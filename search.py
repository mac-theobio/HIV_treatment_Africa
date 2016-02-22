from Bio import Entrez   
from Bio import Medline
import numpy as np
from sys import argv

Entrez.email = "jdushoff@gmail.com"  

script, filename = argv

txt = open(filename)

SearchTerm = txt.read()

# Get Pubmed IDs matching SearchTerm
handle = Entrez.esearch(db="pubmed", term=SearchTerm, retmax=1000) 

## ADD a warning if retmax articles are returned

record = Entrez.read(handle)
idlist = record["IdList"]
print len(idlist)
print idlist
