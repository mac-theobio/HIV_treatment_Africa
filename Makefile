# HIV_treatment_Africa
### Hooks for the editor to set the default target
current: target

target pngtarget pdftarget vtarget acrtarget: base.table.txt 

##################################################################

# make files

Sources = Makefile .gitignore README.md stuff.mk LICENSE.md
include stuff.mk
-include $(ms)/python.def

##################################################################

## Content

Sources += notes.md

Sources += base.txt

Sources += $(wildcard *.py)

SystematicSearch.txt: SystematicSearch.py
	python $<

## Get a list of ids matching a search
base.search.pkl: base.search.txt ;
base.search.txt: base.txt search.py
%.search.txt: %.txt search.py
	$(PITHOUT)

## Get records from a list of ids
## Right now list.py is just producing a text dump
## Our goal is to produce human-usable files: an html file for browsing abstracts and articles, and a csv file for entering notes and codes

base.list.txt: list.py
%.list.txt: %.search.pkl list.py
	$(PITHOUT)

## Do something useful with a list of IDs

base.table.txt: table.py
%.table.txt: %.list.pkl table.py
	$(PITHOUT)

##################################################################

%.pkl: %.txt ;

%.html: %.csv
	csv2html -o $@ $<

######################################################################

### Makestuff

-include $(ms)/git.mk
-include $(ms)/visual.mk

# -include $(ms)/wrapR.mk
# -include $(ms)/oldlatex.mk
