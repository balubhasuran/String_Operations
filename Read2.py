fileHandler = open("F:\Research\Python\data.txt", "r")
while True:
# Get next line from file
line = fileHandler.readline()
# If line is empty then end of file reached
if not line :
break;
print(line.strip())
# Close Close    
fileHandler.close()   
print("****Read file line by line using with open() *****")     
# Open file 
with open("F:\Research\Python\data.txt", "r") as fileHandler:
# Read each line in loop
for line in fileHandler:
# As each line (except last one) will contain new line character, so strip that
print(line.strip())
print("****Read file line by line using with open *****")
# Get the all the lines in file in a list 
listOfLines = list()        
with open ("data.txt", "r") as myfile:
for line in myfile:
listOfLines.append(line.strip()) 
print(listOfLines)               
print("****Read file line by line using with open() and while loop *****")
# Open file
with open("F:\Research\Python\data.txt", "r") as fileHandler:  
# Read next line
line = fileHandler.readline()
# check line is not empty
while line:
print(line.strip())
line = fileHandler.readline()