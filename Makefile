# HIV_treatment_Africa
# https://github.com/mac-theobio/HIV_treatment_Africa/
## Dangerously developing generic bib stuff here! Can I cut it out??

### Hooks for the editor to set the default target

-include target.mk
current: target

##################################################################

# make files

.SUFFIXES:

Sources = Makefile .gitignore README.md sub.mk LICENSE.md
include sub.mk
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

search-results.html: base.list.pkl searchresults-HTML.py
	python searchresults-HTML.py

meeting.md: base.list.pkl meeting.py
	$(PITH)

meeting.html: meeting.py

######################################################################

## JD's pipeline

Sources += hampson.txt dushoff.txt

## Modify a search by limiting to reviews

%.rev.txt: %.txt
	$(copy)
	echo 'AND Review[ptyp]' >> $@

## These two scripts use Pubmed, and can be dicey
## Get a list of ids matching a search

Ignore += *.search.txt
.PRECIOUS: %.search.txt
%.search.txt: %.txt search.py
	$(PITHOUT)

## Get records from a list of ids
## Right now list.py is just producing a text dump
## Our goal is to produce human-usable files: an html file for browsing abstracts and articles, and a csv file for entering notes and codes

%.search.pkl: %.search.txt ;
%.list.txt: %.search.pkl list.py
	$(PITHOUT)

# Include this to bypass Pubmed stuff, in theory
# Old caching stuff; update 
Sources += nopub.mk

######################################################################

## Do something useful with a list of IDs

### A table
base.table.txt: table.py
%.table.txt: %.list.pkl table.py
	$(PITHOUT)

base.table.csv: table.py

### Formatting
dushoff.curr.md: curr.py
dushoff.curr.html: curr.py

Ignore += *.list.pkl
%.list.pkl: %.list.txt ;

Ignore += *.curr.md *.curr.html
%.curr.md: %.list.pkl curr.py
	$(PITHOUT)

### A review document
base.rev.review.html:
%.review.md: %.list.pkl review.py
	$(PITHOUT)

######################################################################

%.pkl: %.txt ;
%.csv: %.txt ;

%.csv.html: %.csv
	csv2html -o $@ $<

######################################################################

### Makestuff

-include $(ms)/git.mk
-include $(ms)/visual.mk
-include $(ms)/pandoc.mk

# -include $(ms)/wrapR.mk
# -include $(ms)/oldlatex.mk
