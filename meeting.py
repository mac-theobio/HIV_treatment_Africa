import webbrowser
import pickle

# load a pickle file
pkl_file = open('base.list.pkl', 'rb')
records = pickle.load(pkl_file)
pkl_file.close()

for record in records:
	print "----------------------------------------\n"

	### Head material
	print record['TI'] 
	print "__" + record['JT'] + "__"
	if 'AU' in record.keys():
		print "_" + (" ".join(record['AU'])) + "_"

	### Links
	print(
		"[Pubmed](https://www.ncbi.nlm.nih.gov/pubmed/"
		+ record['PMID']
		+ ")"	
	)

	### Abstract
	print "\n" + record['AB']
	print "\n"

