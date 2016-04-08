from Bio import Entrez   # biopython module for searching on Entrez
from Bio import Medline

import cPickle as pickle
from sys import argv

Entrez.email = "jdushoff@gmail.com"  

script, target, pin = argv
pout =  target.replace("txt", "pkl")

idlist = pickle.load( open( pin, "rb" ) )

handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",retmode="text")
records = Medline.parse(handle)

pickle.dump(idlist, open( pout, "wb" ) )
