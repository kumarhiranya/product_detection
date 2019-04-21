import os
import pandas as pd

basePath = 'images/dove_soap/'
imageExtensions = 'png jpg jpeg'.split()

# extensions = pd.Series([x.split('.')[-1] for x in os.listdir(basePath)])
# print(extensions.unique())

files = [x for x in os.listdir(basePath) if x.split('.')[-1].lower() in imageExtensions]

existingNumbers = {}
for i,f in enumerate(files):
    try:
        x = int(f.split('.')[0])
        existingNumbers[x] = 0
    except:
        c=i
        while c in existingNumbers.keys():
            c+=1
        os.rename(basePath+f, basePath+str(c)+'.'+str(f.split('.')[-1]))

print('renamed %d files.', i)