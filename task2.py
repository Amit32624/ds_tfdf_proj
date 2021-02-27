from glob import glob
from collections import Counter
from numpy.core.numeric import normalize_axis_tuple
import pandas as pd
import numpy as np
import re
import os




folderpaths = 'C://Users//91720//Documents//ds_tfdf_proj//Dataset-P1'
doc2vocab  = dict()
vocab2doc  = dict()
counter = Counter()
for i in range(0,60):
    doc2vocab[i] = dict()

    with open('./folderpaths/*.txt' % i, 'r', encoding="utf-8") as doc:
        words = re.findall(r'\w+', doc.read().lower()) #Returns a match where the string contains any word character
        print(words)
        # if len(words) >=4 and len(words) <= 20:
        counter1 = counter + Counter(words)
        counter2 = Counter(words)
        # word_in_the_document = 
        print(counter) 

        for words in counter2:
            # make document and vocab pair dictionary
            if words in doc2vocab[i]:
                doc2vocab[i][words] += 1
                
            else:
                doc2vocab[i][words] = 1
            
            # make inverted index, {word : [doc1, doc3, ... ]}
            text_str = str(i) + '.txt'
            if words in vocab2doc:
                if text_str not in vocab2doc[words]:
                    vocab2doc[words].append(text_str)
                    
            else:
                vocab2doc[words] = list()
                vocab2doc[words].append(text_str)