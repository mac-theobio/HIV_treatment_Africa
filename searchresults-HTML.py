import webbrowser
import pickle

# load a pickle file
pkl_file = open('base.list.pkl', 'rb')
mydict = pickle.load(pkl_file)
pkl_file.close()

print list(mydict)[0].keys()

data = []

ncount0=0;   # to enumerate the articles 
for record in mydict:
	ncount=ncount0 +1 
	#ti_list = record['TI'] #titles
	data.append({'Article Number #', ncount})	
	data.append({'PMID:=',record['PMID']})
	data.append({record['TI']})
	data.append({record['JT']})
	data.append({record['AB']})
	if 'LID' in record.keys():
		data.append({record['LID']})
	else :
		data.append({'No LID'})
	ncount0=ncount # update the counting 

listofrows=data

#now create a string with the following:
htmlstuff='<p> <p>'

#now you would add the COLUMN HEADERS to the list...
#for header in listofheaders:
#    htmlstuff=htmlstuff+'<th>'+str(header)+'</th>\n'

#then you can populate the table row by row...
for row in listofrows:
    htmlstuff+='  <p>\n'
    for item in row:
        htmlstuff=htmlstuff+'    <td>'+ str(item)+'</td>\n'
    htmlstuff+='  </p>\n'

# finish off the html coding...
# htmlstuff+='</table>\n</body>\n\n</html>'

# now create the html page and write the data...
f=open('search-results.html','w')
f.write(htmlstuff)
f.close()

webbrowser.open('search-results.html')

