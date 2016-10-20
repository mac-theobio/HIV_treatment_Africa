import cPickle as pickle
from sys import argv

# Pickle files
script, target, pin = argv
pout =  target.replace("txt", "pkl")

# load a pickle file
records = pickle.load(open( pin, "rb" ) )

for record in records:
	print "----------------------------------------\n"

	### Head material
	print record['TI'] 
	print "__" + record['JT'] + "__"
	if 'AU' in record.keys():
		print "_" + (" ".join(record['AU'])) + "_"

	### Links
	print("\n"
		+ "[Pubmed](https://www.ncbi.nlm.nih.gov/pubmed/"
		+ record['PMID']
		+ ")"	
	)

	### Abstract
	if 'AB' in record.keys():
		print "\n" + record['AB']

	print "\n"

