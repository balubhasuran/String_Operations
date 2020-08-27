#!/usr/bin/python

def check(string, sub_str): 
	if(string.find(sub_str) == -1): 
		print("No") 
	else: 
		newg='<gene>'+sub_str+'</gene>'
		print(string.replace(sub_str,newg), end="")
		
gene = "EPAS1"
with open("F:\Research\Python\data.txt", "r") as fileHandler:
	line = fileHandler.readline()
	while line:
		check(line, gene)
		line = fileHandler.readline()