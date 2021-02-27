from glob import glob
from collections import Counter
from numpy.core.numeric import normalize_axis_tuple
import pandas as pd
import numpy as np
import re
import os

folderpaths = 'C://Users//91720//Documents//ds_tfdf_proj//Dataset-P1'
counter = Counter()
idf =[]
filepaths = glob(os.path.join(folderpaths,'*.txt'))
for file in filepaths:
    with open(file) as f:
        words = re.findall(r'\w+', f.read().lower()) #Returns a match where the string contains any word character
        print(words)
        counter = counter + Counter(words) 
        print(counter) 
        items = {k:v for (k,v) in counter.items() if len(k) >=4 and len(k) <= 20}
        for ele in counter:
            idf.append(counter[ele]/len(counter))
            print(idf) # Gives the term frequency TF

# print(normalized_tf)

# print(counter)
# print("Popular_words",counter.most_common(200))
# # print(items)
# print("Number of words: ",len(items))
# print("**********************")


