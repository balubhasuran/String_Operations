#!/usr/bin/python
pubmed = []
genes = []
with open("F:\Research\Python\genes1.txt", "r") as P:
	pubmed = [line.strip() for line in P]
with open("F:\Research\Python\gene.txt", "r") as G:
    genes = [line.strip() for line in G]
	
    print([i for i, j in zip(pubmed, genes) if i == j])
