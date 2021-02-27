from glob import glob
from collections import Counter
# from numpy.core.numeric import normalize_axis_tuple
import pandas as pd
import numpy as np
import math
import re
import os

folderpaths = 'C:\\Users\\91720\Documents\\ds_tfdf_proj\\Dataset-P1'
counter = Counter()
filepaths = glob(os.path.join(folderpaths,'*.txt'))
print(os.path.basename(filepaths[0]))
a = 0
file_name_list =[]
pop_200_words =[]
b = 0
file_nameList =[]
idfDict ={}
for file in filepaths:

    with open(file) as f:
        file_nameList.append(os.path.basename(filepaths[b]))
        b += 1
        num_docs_with_given_term = 0
        file_name_list.append(os.path.basename(filepaths[a])) # gives the file names in the folder in the list
        a += 1
        words = re.findall(r'\w+', f.read().lower())
        # print(words)
        counter = counter + Counter(words)
        counter2 = Counter(words)
        tf_dict = dict(counter2)
        tf_list =[]
        
        # print(tf_dict)
        items = {k:v for (k,v) in counter.items() if len(k) >=4 and len(k) <= 20} #occurances for the words length (min. size = 4 $ max. size= 20).
        for ele,value in tf_dict.items():
            tf ={}
            tf[ele] = value/len(tf_dict)  # # Gives the term frequency TF
            print(tf)
            
# N =len(file_nameList)
# idf = dict.f
# print(len(file_nameList))
# print("counter",counter)
# print(file_name_list)
pop_200_words.append(counter.most_common(10))
# print(pop_200_words)
# print(items)
# print("IDF",idf)


