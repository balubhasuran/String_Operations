#!/usr/bin/python
pubmed = []
genes = []
with open("F:\OMIMCorpus.txt", "r") as P:
	pubmed = [line.strip() for line in P]
with open("F:\Research\Python\biologicalprocess.txt", "r") as G:
    genes = [line.strip() for line in G]

for text in pubmed:
	count=0
	for line in genes:
		
		if line in text: 
			newg='<biologicalprocess>'+line+'</biologicalprocess>'
			text=text.replace(line,newg)
		else: 
			count=1
	print(text,'\n' , end="" )