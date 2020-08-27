#!/usr/bin/python

def check(string, sub_str): 
	if(string.find(sub_str) == -1): 
		print(string)
		print(sub_str)
	else: 
		newg='<gene>'+sub_str+'</gene>'
		print(string.replace(sub_str,newg), end="")
		
with open("F:\Research\Python\data.txt", "r") as fileHandler:
	line = fileHandler.readline()
	while line:
		with open("F:\Research\Python\gene.txt", "r") as fileHandler2:
			gene = fileHandler2.readline()
			while gene:
				check(line, gene)
				gene = fileHandler2.readline()
		line = fileHandler.readline()