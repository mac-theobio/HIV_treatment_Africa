from Bio import Entrez   # biopython module for searching on Entrez
from Bio import Medline

import cPickle as pickle
from sys import argv

Entrez.email = "jdushoff@gmail.com"  

# Pickle files
script, target, pin = argv
pout =  target.replace("txt", "pkl")

idlist = pickle.load( open( pin, "rb" ) )

handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",retmode="text")
records = Medline.parse(handle)
for record in records:
	print record

## Bewketu, can you figure out how to save the records in pickle?
# pickle.dump(records, open( pout, "wb" ) )
