pyfiles := $(shell find compiler -name '*.py')
templates := $(shell find templates -type f)
datafiles := $(shell find data -name '*.yml')

output/*/*.html : $(pyfiles) $(templates) $(datafiles)
	python -m compiler

compile : output/*/*.html

server : compile
	cd output && python -m http.server 8080

.DEFAULT_GOAL := compile
