from glob import glob
from collections import Counter
import re
import os

folderpaths = 'C://Users//91720//Documents//ds_tfdf_proj//Dataset-P1'
counter = Counter()

# filepaths = glob(os.path.join(folderpaths,'*.txt'))
# for file in filepaths:
#     with open(file) as f:
#         words = re.findall(r'\w+', f.read().lower())
#         # if len(words) >=4 and len(words) <= 20:
#         counter = counter + Counter(words)
#         items = {k:v for (k,v) in counter.items() if len(k) >=4 and len(k) <= 20}
        
# print(counter)
# print(items)
# print("Number of words: ",len(items))


filepaths = glob(os.path.join(folderpaths,'*.txt'))
for file in filepaths:
    with open(file) as f:
        def termFrequency(term, f):
                normalizeTermFreq = f.lower().split()
                term_in_document = normalizeTermFreq.count(term.lower()) 
                len_of_document = float(len(normalizeTermFreq ))
                normalized_tf = term_in_document / len_of_document
                return normalized_tf 
    

# print(normalized_tf)
# print(counter)
# print(items)
# print("Number of words: ",len(items))


