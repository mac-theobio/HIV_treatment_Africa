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

Sources += base.txt test.txt

Sources += $(wildcard *.py)

######################################################################

## BB's big script
SystematicSearch.txt: SystematicSearch.py
	python $<

html: csv2html.py base.table.txt > base.html
	python $<

######################################################################

## JD's pipeline

## These two scripts use Pubmed, and can be dicey
## Get a list of ids matching a search

.PRECIOUS: %.search.txt
%.search.txt: %.txt search.py
	$(PITHOUT)

## Get records from a list of ids
## Right now list.py is just producing a text dump
## Our goal is to produce human-usable files: an html file for browsing abstracts and articles, and a csv file for entering notes and codes

%.list.txt: %.search.pkl list.py
	$(PITHOUT)

# Include this to bypass Pubmed stuff, in theory
Sources += nopub.mk

######################################################################

## Do something useful with a list of IDs
base.table.txt: table.py
%.table.txt: %.list.pkl table.py
	$(PITHOUT)

base.table.csv: table.py

##################################################################

%.pkl: %.txt ;
%.csv: %.txt ;

%.csv.html: %.csv
	csv2html -o $@ $<

######################################################################

### Makestuff

-include $(ms)/git.mk
-include $(ms)/visual.mk

# -include $(ms)/wrapR.mk
# -include $(ms)/oldlatex.mk
