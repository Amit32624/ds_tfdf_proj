
from pathlib import Path
import  math


folderpaths = 'C:\\Users\\91720\Documents\\ds_tfdf_proj\\Dataset-P1'
# filepaths = glob(os.path.join(folderpaths,'*.txt'))
all_txt_files =[]
for file in Path(folderpaths).rglob("*.txt"):
     all_txt_files.append(file.parent / file.name)
    #  print(all_txt_files)
# counts the length of the list
n_files = len(all_txt_files)
print(n_files)
all_txt_files.sort()
print(all_txt_files[0])


all_docs = []
new_list =[]
for txt_file in all_txt_files:
    with open(txt_file) as f:
        tfDict = {}
        txt_file_as_string = f.read().lower()
    # Splitting the document into individual terms 
        normalizeTermFreq = txt_file_as_string.lower().split()  
        all_docs.append(normalizeTermFreq)
        print(normalizeTermFreq)

        term_in_document =[]
        term = 0
        for i in normalizeTermFreq:
            term_tf = (normalizeTermFreq[term])
            print(term_tf)
            term_in_document =(normalizeTermFreq.count(term_tf)  )
            print(term_in_document)
            term += 1
            len_of_document =len(normalizeTermFreq)  
            print(len_of_document) 
            tfDict[term_tf] = term_in_document / len_of_document
            new_list.append(tfDict)  
            
            # return normalized_tf
# print(inverseDocumentFrequency,)
print("normalized_tfss: ",tfDict) 
print("normalized_tf",new_list)
num_docs_with_given_term = 0
    # Iterate through all the documents 
for doc in all_docs: 
    print("doc",doc)
    term_in_all_document =[]
    term_allDocs = 0
    for i in doc:
        term_tf_allDocs = (doc[term_allDocs])
        print(term_tf_allDocs,"term_tf_allDocs")
        term_allDocs += 1
        # print(all_docs[doc])
    if term_tf_allDocs in doc: 
        num_docs_with_given_term += 1

    if num_docs_with_given_term > 0: 
        # Total number of documents 
        total_num_docs = len(all_docs)  

        # Calculating the IDF  
    idf_val = math.log10(float(total_num_docs) / num_docs_with_given_term)
    if idf_val:
        print("idf_val",idf_val)
    else:
        print("0",0)

    # print(txt_file_as_string)
    # all_docs.append(txt_file_as_string)
# print(termFrequency(txt_file_as_string))
print(all_docs)































# from glob import glob
# from collections import Counter
# import pandas as pd
# import numpy as np
# import math
# import re
# import os

# folderpaths = 'C:\\Users\\91720\Documents\\ds_tfdf_proj\\Dataset-P1'
# filepaths = glob(os.path.join(folderpaths,'*.txt'))
# b = 0
# file_nameList =[]

# for file in filepaths:

#     with open(file) as f:
#         file_nameList.append(os.path.basename(filepaths[b]))
#         b += 1
# print(file_nameList)
# file_nameList.sort()
# print(file_nameList[0])

# all_docs = []
# for txt_file in file_nameList:
#     with open(txt_file) as f:
#         txt_file_as_string = f.read()
#     all_docs.append(txt_file_as_string)
#     print(all_docs)