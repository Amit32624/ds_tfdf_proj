#
# Created on Sun Feb 27 2021 by Amit Sambrekar[120220153]
# Msc in Data Scince and Analytics
# Information Storage and Retrieval
# Assignment #1

import numpy as np
import pandas as pd
import math
import os
import itertools
from glob import glob

#Program initialization
no_of_doc = int(input("Enter the number of docs to checked for similarity with the query doc: ")) # E.g 05
similar_docs = input("Enter the valid document name with the correct extension name: ") #E.g 85.txt

values={}
top200={}
new_list=[]
IDF=[]

tokens_dict={}
files_list=[]
main_files_lt=[]

folderpaths = 'C:\\Users\\91720\Documents\\ds_tfdf_proj\\Dataset-P1'

filepaths = glob(os.path.join(folderpaths,'*.txt'))

# for path, files in filepaths:
for path,dirs,file in os.walk(folderpaths):
    for way in sorted(file):
        values.clear()
        filename=os.path.join(path,way)
        with open(filename,"r") as specific_file:
            file=specific_file.read()
            words_z=file.split()#

            for item in words_z:
                if (item in tokens_dict):
                    tokens_dict[item] += 1
                else:
                    tokens_dict[item] = 1
            for item in words_z:
                if (item in values):
                    values[item] += 1
                else:
                    values[item] = 1
        files_list.append( dict(values))
        main_files_lt.append(way)
		
#Sorting for finding the most commom words
tuples = sorted(tokens_dict.items(), key=lambda item: item[1]) 
tup_sort=tuples[::-1]
dict_sort = {k: v for k, v in tup_sort}
print('the top 200 most popular words',list(itertools.islice(dict_sort.items(), 0, 200)))

#Sorting based on tokens_dict length
for key,value in dict_sort.items():         
    if (len(key)>=4) and (len(key)<=20):
        top200[key]=value
print('The most 200 popular words with filter',list(itertools.islice(top200.items(), 0, 200)))

#Code to find TF IDF using panda
count_of_docs=len(files_list)
df = pd.DataFrame.from_dict(files_list, orient='columns')
new_df = pd.DataFrame(main_files_lt)
df[0]=new_df[0].values
print("the tf: ",end='')

#Execute this staement to find TF

print(df.fillna(0))                          
dftrain1=df.drop([0],axis=1)
dfnull=dftrain1.isnull().sum(axis = 0)
df_count=abs(dfnull-57)
for i in df_count.values:
    mid_value=math.log(count_of_docs/i,2)+1
    IDF.append(mid_value)
print("the IDF : ",end='')
print(IDF)
#IDF calculation

dftrain1.iloc[:, 0:] *= IDF                   
dftrain1[0]=new_df[0].values
df_tfidf=dftrain1.fillna(0)

#Tf IDF

print('the tf-IDF : ',end='')                             
print(df_tfidf)

df_new= df[df[0]==similar_docs]   #Calculating Cosine Similarity
df_alphaZero=df.fillna(0)
df_zeros_new=df_alphaZero.drop([0],axis=1)
df_ref= df_alphaZero[df_alphaZero[0]==similar_docs]
df_reference1=df_ref.drop([0],axis=1)
df_ref=df_reference1*df_reference1
a_sum=df_ref.sum(axis=1)
for i in  range(len(df_zeros_new)):
   df_mul=df_zeros_new.iloc[i].mul(df_reference1)
   df33 = df_zeros_new.iloc[i] * df_zeros_new.iloc[i]
   q = df33.sum(axis=0)
   words_z=df_mul.sum(axis=1)
   #Implemenataion of Cosine Formula
   cos_sim=words_z/(math.sqrt(a_sum) * math.sqrt(q)) 
   ans=cos_sim.values
   ans1=float(ans)
   new_list.append(ans1)
arr = np.array(new_list)
arr[np.isnan(arr)] = 0
xdx = (-arr).argsort()[:no_of_doc]
matching_files_lt=[]
#Thecommon matched file

for i in xdx:                           
    file_name_new=new_df.iloc[i]
    conv=str(file_name_new.values)
    matching_files_lt.append(conv)
print("The matching files are: ",matching_files_lt)