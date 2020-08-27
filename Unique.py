import numpy as np 
  
MeSH = []
with open("F:\MeSH 2020.txt", "r") as P:
	MeSH = [line.strip() for line in P]
myset = set(MeSH)
print(myset)