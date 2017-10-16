import cPickle as pickle
import sys 
import re

# Pickle files
script, target, pin = sys.argv
pout =  target.replace("txt", "pkl")

# load a pickle file
records = pickle.load(open( pin, "rb" ) )

for record in records:
	if 'AU' in record.keys():
		for anum in range(0, len(record['AU'])):
			aname = record['AU'][anum]
			names =  aname.split(" ")
			first = ""
			last = names[0]
			if (len(names)>1):
				first = re.sub(r'(\w)', r'\1.', names[1])
			if anum == 0:
				sys.stdout.write(last)
				if first != "": sys.stdout.write( ", " + first)
			elif anum == len(record['AU'])-1:
				print "and",
				if first != "": print first,
				print last + ".",
			else:
				print ", ",
				if first != "": print first,
				sys.stdout.write(last)

	print record['JT'] 
	print record['TI'] 

	print "\n"
