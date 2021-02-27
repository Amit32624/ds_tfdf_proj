import math
import os
import numpy as np
import itertools
import pandas as pd

token={}
lis_file=[]
lis_file2=[]
names={}
for path, dirs,files in os.walk('C:\\Users\\91720\Documents\\ds_tfdf_proj\\Dataset-P1'):
    for f in sorted(files):
        names.clear()
        filename=os.path.join(path,f)
        with open(filename,"r") as myfile:
            a=myfile.read()
            z=a.split()
            print(z)
            for item in z:
                if (item in token):
                    print("item",item)
                    token[item] += 1
                    print(token)
                else:
                    token[item] = 1
            for item in z:
                if (item in names):
                    names[item] += 1
                else:
                    names[item] = 1
        lis_file.append( dict(names))
        lis_file2.append(f)
sorted_tuples = sorted(token.items(), key=lambda item: item[1])
sorted_tuples1=sorted_tuples[::-1]
sorted_dict1 = {k: v for k, v in sorted_tuples1}
print('the top 200 most popular words',list(itertools.islice(sorted_dict1.items(), 0, 200)))
dict200={}
for key,value in sorted_dict1.items():
    if (len(key)>=4) and (len(key)<=20):
        dict200[key]=value
print('the 200 popular words with filter',list(itertools.islice(dict200.items(), 0, 200)))
Doc_length=len(lis_file)
df = pd.DataFrame.from_dict(lis_file, orient='columns')
df1 = pd.DataFrame(lis_file2)
df[0]=df1[0].values
dftrain1=df.drop([0],axis=1)

dfnull=dftrain1.isnull().sum(axis = 0)
df_count=abs(dfnull-57)
idf=[]
for i in df_count.values:
    mid_value=math.log(Doc_length/i,2)+1
    idf.append(mid_value)
dftrain1.iloc[:, 0:] *= idf
dftrain1[0]=df1[0].values
print(dftrain1,'the weighted tdf')

df_new= df[df[0]=='6.txt']
df_zeros=df.fillna(0)
print(df_zeros)
for i in range(0,len(df)):
    print(df.iloc[i])