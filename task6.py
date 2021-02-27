
from pathlib import Path
import  math
import pandas as pd

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


def flatten(all_docs):
    flatList = []
    for elem in all_docs:
        # if an element of a list is a list
        # iterate over this list and add elements to flatList 
        if type(elem) == list:
            for e in elem:
                flatList.append(e)
        else:
            flatList.append(elem)
    return flatList

FlatList = flatten(all_docs)
# print(FlatList)
def unique(FlatList):
    """ Assumes lst is already sorted """
    unique_list = []
    for el in FlatList:
        if el not in unique_list:
            unique_list.append(el)
    return unique_list
Unique_list = unique(FlatList)
# print(FlatList)
print("Unique_list",Unique_list)
print("all_docs",all_docs)

list1 =[]
for i in all_docs:
    print('i',i)
    dic_1 ={}
    j = 0
    for m in Unique_list:
        for n in i:
            if m == n:
                print("m",m)
                if m not in dic_1:
                    dic_1[m] = 0
                else:
                    dic_1[m] += 1
            else:
                print("else m",m)
                if m not in dic_1:
                    dic_1[m] = 0
                else:
                    dic_1[m] += 1
    #     k += 1
    # j += 1
print(dic_1)

#         if Unique_list[k] not in dic_1:
#             print(Unique_list[k])
#             print(True)
#             dic_1[Unique_list[k]] = 0
#             # print("dic_1",dic_1)
#             k += 1
#         else:
#             dic_1[Unique_list[k]] += 1
#             k += 1
        
#     else:
#         dic_1[Unique_list[k]] = 0
#         k += 1
#     print("dic_1",dic_1)
#     list1.append(dic_1)
#     print("list1Insde",list1)
#     list2 = list(dic_1)
#     j += 1

# print("leftOutside",list1)
# print("lis2",list2)
    
# print("list1",list1)
# words_df =pd.DataFrame.from_dict([dic_1])
# print(words_df)

    # if check is True: