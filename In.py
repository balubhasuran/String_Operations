#!/usr/bin/python

def check(string, sub_str): 
	count=0
	if sub_str in string: 
		newg='<gene>'+sub_str+'</gene>'
		print(string.replace(sub_str,newg),'\n' , end="" )
	else: 
		#print(string ,'\n' , end="")
		#print(sub_str, '\n', end="" )
		count=count+1
				
with open("F:\Research\Python\data.txt", "r") as fileHandler:
	line = fileHandler.readline()
	while line:
		with open("F:\Research\Python\gene.txt", "r") as fileHandler2:
			gene = fileHandler2.readline()
			while gene:
				check(line, gene)
				gene = fileHandler2.readline()
		line = fileHandler.readline()