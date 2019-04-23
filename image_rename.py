import os
import pandas as pd

basePath = 'images/dove_soap/'
imageExtensions = 'png jpg jpeg'.split()

# extensions = pd.Series([x.split('.')[-1] for x in os.listdir(basePath)])
# print(extensions.unique())

files = [(x[:-len(x.split('.')[-1])-1], x.split('.')[-1]) for x in os.listdir(basePath) if x.split('.')[-1].lower() in imageExtensions]
existingNumbers = {int(x[0]):x[1] for x in files if x[0].isdigit()}

i=0
cnt=0
for f in files:
    rename = 0
    if f[0].isdigit():
        if int(f[0])>10000:
            print(f[0], 'is an integer above 10000, renaming file....')
            rename = 1
    else:
        print(f[0], 'is not an integer, renaming file....')
        rename = 1
    if rename:
        while os.path.exists(basePath+str(i)+'.'+f[1]):
            i+=1
        os.rename(basePath+f[0]+'.'+f[1], basePath+str(i)+'.'+f[1])
        cnt+=1
print('Renamed', cnt, 'files.')