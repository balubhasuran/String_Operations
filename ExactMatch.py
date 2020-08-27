#!/usr/bin/python
import re
pubmed = []
genes = []
with open("F:\OMIMCorpus.txt", "r") as P:
	pubmed = [line.strip() for line in P]
with open("F:\Research\Python\biologicalprocess.txt", "r") as G:
    genes = [line.strip() for line in G]

for text in pubmed:
	count=0
	for line in genes:
		newg='<gene>'+line+'</gene>'
		#line='\\b'+line+'\\b'
		text=re.sub('\\b'+line+'\\b', newg, text)	
		
	print(text,'\n' , end="" )