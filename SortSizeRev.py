#!/usr/bin/python
listA = []
with open("F:\Research\Python\data.txt", "r") as P:
    listA = [line.strip() for line in P]
listA = sorted(listA, key=len) 
for line in listA:
		print(line,'\n' , end="" )
		
	