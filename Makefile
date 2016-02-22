# HIV_treatment_Africa
### Hooks for the editor to set the default target
current: target

target pngtarget pdftarget vtarget acrtarget: search.txt 

##################################################################

# make files

Sources = Makefile .gitignore README.md stuff.mk LICENSE.md
include stuff.mk
-include $(ms)/python.def

##################################################################

## Content

Sources += base_search.txt

Sources += $(wildcard *.py)

SystematicSearch.txt: SystematicSearch.py
	python $<

base.search.txt: base.txt search.py
	$(PITH)

######################################################################

### Makestuff

-include $(ms)/git.mk
-include $(ms)/visual.mk

# -include $(ms)/wrapR.mk
# -include $(ms)/oldlatex.mk
