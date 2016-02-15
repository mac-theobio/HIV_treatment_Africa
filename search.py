from Bio import Entrez   
from Bio import Medline
import numpy as np

Entrez.email = "jdushoff@gmail.com"  

# below are four different search concepts (using boolean arguments). Uncomment only one of them to see the output of the search. 

#SearchTerm="((((Human immunodeficiency virus) OR HIV OR AIDS) AND (Malawi OR (South Africa))) AND ('treatment failure' OR dropout))"

SearchTerm= "((((Human immunodeficiency virus) OR (acquired immunodeficiency syndrome) OR HIV OR AIDS OR (HIV/AIDS)) AND (Swaziland OR Botswana OR Lesotho OR (South Africa) OR Zimbabwe OR Namibia OR Zambia OR Mozambique OR Malawi OR Uganda OR (Equatorial Guinea) OR Kenya OR Tanzania OR (sub Saharan Africa) OR (sub-Saharan Africa)))  AND ((treatment failure) OR switch OR switches OR switching OR (first line) OR (first-line) OR (second line) OR (second-line) OR (lost to follow up) OR (lost to follow-up) OR (loss to follow up) OR (loss to follow-up) OR dropout OR (drop-out) OR dropouts OR (drop out) OR (drop outs)))" 

# SearchTerm= "((((Human immunodeficiency virus) OR (acquired immunodeficiency syndrome) OR HIV OR AIDS OR (HIV/AIDS)) AND (Swaziland OR Botswana OR Lesotho OR (South Africa) OR Zimbabwe OR Namibia OR Zambia OR Mozambique OR Malawi OR Uganda OR (Equatorial Guinea) OR Kenya OR Tanzania OR (sub Saharan Africa) OR (sub-Saharan Africa)))  AND ((treatment failure) OR switch OR switches OR switching OR (first line) OR (first-line) OR (second line) OR (second-line) OR (lost to follow up) OR (lost to follow-up) OR (loss to follow up) OR (loss to follow-up) OR dropout OR (drop-out) OR dropouts OR (drop out) OR (drop outs)))  AND  ((2010/01/01[PDat] : 2015/12/31[PDat]) AND Humans[Mesh] AND English[lang]))"

#SearchTerm="((('Human immunodeficiency virus' OR 'acquired immunodeficiency syndrome' OR HIV OR AIDS OR 'HIV/AIDS') AND (Swaziland OR Botswana OR Lesotho OR 'South Africa' OR Zimbabwe OR Namibia OR Zambia OR Mozambique OR Malawi OR Uganda OR 'Equatorial Guinea' OR Kenya OR Tanzania OR 'sub Saharan Africa' OR 'sub-Saharan Africa'))  AND ('treatment failure' OR switch OR switches OR switching OR 'first line' OR 'first-line' OR 'second line' OR 'second-line' OR  'lost to follow up' OR 'lost to follow-up' OR 'loss to follow up' OR 'loss to follow-up' OR dropout OR 'drop-out' OR dropouts OR 'drop out' OR 'drop outs'))"

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

# np.savetxt('SystematicSearch.txt', records, fmt="%s") # this saves in a text format


 














