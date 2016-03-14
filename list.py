
from Bio import Entrez   # biopython module for searching on Entrez
from Bio import Medline
import numpy as np

import cPickle as pickle
from sys import argv

import csv
import os

Entrez.email = "jdushoff@gmail.com"  

script, target, pkl = argv

idlist = pickle.load( open( pkl, "rb" ) )

print idlist

handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline",retmode="text")
records = Medline.parse(handle)

records = list(records)

np.savetxt(target, records, fmt="%s") # this saves in a text format
