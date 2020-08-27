import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import json

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os

datafiles = []
for dirname, _, filenames in os.walk('D:\Covid-19'):
    for filename in filenames:
        ifile = os.path.join(dirname, filename)
        if ifile.split(".")[-1] == "json":
            datafiles.append(ifile)

id2title = []
for file in datafiles:
    with open(file,'r')as f:
        doc = json.load(f)
    title = doc['metadata']['title']
    id2title.append({title})


id2abstract = []
for file in datafiles:
    with open(file,'r')as f:
        doc = json.load(f)
    abstract = ''
    for item in doc['abstract']:
        abstract = abstract + item['text']
        
    id2abstract.append({abstract})
	
	
id2bodytext = []
for file in datafiles:
    with open(file,'r')as f:
        doc = json.load(f)
    bodytext = ''
    for item in doc['body_text']:
        bodytext = bodytext + item['text']
        
    id2bodytext.append({bodytext})


print(id2title)
print(id2abstract)
print(id2bodytext)
	
#for (a, b, c) in zip(id2title, id2abstract, id2bodytext): 
	#print (a, b, c)