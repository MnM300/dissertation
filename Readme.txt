tO DO
=========

Figure out how to install dependencies for Mantime.
crf++0.58
nltk==2.0.5
jsonrpclib>=0.1.3
pexpect>=3.1
xmltodict>=0.9.0
nltk data (tokenizers) == punkt


The Following provides an overview of the pipeline being applied.

Doc retriever
====================

Input 	- IDS
		- PubMed XML
		- Text
		
OutPut 	- Section Offsets
		- Text version
		- ManTIME XML version

MedEX
====================

Input	- Text Version
OutPut 	- Drug List
		- Possibly MedEX Sentence Offsets

ManTIME
====================

Input 	- ManTIME XML version
OutPut 	- Annotated XML file 	- Events
								- TimeX
								- Sentence Offsets
								- Word Offsets

Rules for Extraction
====================

Input 	- Annotated XML file 	- Events
								- TimeX
								- Sentence Offsets
								- Word Offsets
		- Drug List
		- MedEX Sentence Offsets
		- Section Offsets (working on this)

OutPut 	- TSV File containing Features and their count as well as a class

Evaluation
===================

Input 	- TSV File containing Features and their count
		- Sentence Offsets (MedEX or ManTIME)
		- Text Version

OutPut 	- Key Sentences