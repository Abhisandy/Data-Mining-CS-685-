import pandas as pd
import numpy as np
import re
import csv
import sys
from collections import defaultdict
from collections import OrderedDict
from Ques_1 import dict_names
from Ques_2 import dict_diff_articleAndCategory_id
from Ques_2 import dict_category

df_PathFinished = pd.read_csv("Data/paths_finished.tsv",sep="\tab",header = None,engine='python')
df_PathFinished = df_PathFinished.iloc[15:]

list_path = []
for index, row in df_PathFinished.iterrows():
    list_path.append(row.iloc[0].split('\t'))

list_path_split = []
for sp in list_path:
    list_path_split.append(sp[3].split(';'))

list_path_split.pop(2395)

new_list_path_split = []
for st in list_path_split:
    if len(st) != 1:
        t = []
        for m in range(0 , len(st)):
            if st[m] == '<':
                t.pop(-1)
            else:
                t.append(st[m])
        new_list_path_split.append(t)
    else:
        pass

list_article_count = [0]*4604
for ai in new_list_path_split:
    leni = len(ai)
    for i , ele in enumerate(ai):
        #if ele != '<':
         #   if ai[(i+1)%leni] != '<':
        a = list(dict_names.keys())[list(dict_names.values()).index(ele)]
        a1 = re.findall('\d+', a )
        a11 = int(a1[0])
        list_article_count[a11 - 1] = list_article_count[a11 - 1] + 1

dict_cat_art = [[] for i in range(146)]
for ai in dict_diff_articleAndCategory_id.keys():
    for b in dict_diff_articleAndCategory_id[ai]:
        a = b
        a1 = re.findall('\d+', a )
        a11 = int(a1[0])
        dict_cat_art[a11 - 1].append(ai)

human_path_count_rp = []
for di in dict_cat_art:
    s = 0
    for el in di:
        a = el
        a1 = re.findall('\d+', a )
        a11 = int(a1[0])
        s = s + list_article_count[a11-1]
    human_path_count_rp.append(s)

list_article_count_wp = [0] * 146
for ai in new_list_path_split:
    leni = len(ai)
    bo = [0] * 146

    for i, ele in enumerate(ai):
        a = list(dict_names.keys())[list(dict_names.values()).index(ele)]
        for m in dict_diff_articleAndCategory_id[a]:
            a = m
            a1 = re.findall('\d+', a)
            a11 = int(a1[0])
            if (bo[a11 - 1] == 0):
                list_article_count_wp[a11 - 1] = list_article_count_wp[a11 - 1] + 1
                bo[a11 - 1] = 1
    bo.clear()

pair_0 = []
pair_1 = []
for item in new_list_path_split:
    a = list(dict_names.keys())[list(dict_names.values()).index(item[0])]
    b = list(dict_names.keys())[list(dict_names.values()).index(item[-1])]
    pair_0.append(a)
    pair_1.append(b)

index_real_df = pd.DataFrame({'IDs' : pair_0  , 'Articles':pair_1})
index_real_df.to_csv('Data/temp.csv' , index = False , header = False)

df_SP = pd.read_csv("Data/shrtpath.csv", sep='\n', header=None)

list_SP = []
for index, row in df_SP.iterrows():
    list_SP.append(str(row.iloc[0]).split(','))

list_SP_count = [0]*4604
for a in list_SP:
    for b in a:
        if (b!= '') & (b != 'NA') & (b != 'nan'):
            x = int(b)
            list_SP_count[x - 1] = list_SP_count[x - 1] + 1

shortest_path_count_rp = []
for di in dict_cat_art:
    s = 0
    for el in di:
        a = el
        a1 = re.findall('\d+', a )
        a11 = int(a1[0])
        s = s + list_SP_count[a11-1]
    shortest_path_count_rp.append(s)

Shortest_article_count_wp = [0] * 146
for ai in list_SP:
    leni = len(ai)
    bo = [0] * 146

    for i, ele in enumerate(ai):
        if (ele != '') & (ele != 'NA') & (ele != 'nan'):
            a = ('A' + "{:04d}".format(int(ele)))
            for m in dict_diff_articleAndCategory_id[a]:
                a = m
                a1 = re.findall('\d+', a)
                a11 = int(a1[0])
                if (bo[a11 - 1] == 0):
                    Shortest_article_count_wp[a11 - 1] = Shortest_article_count_wp[a11 - 1] + 1
                    bo[a11 - 1] = 1
    bo.clear()

cat_li = []
for s in dict_category.values():
    cat_li.append(s)

df_bfs = pd.DataFrame({'Cat.Id': cat_li  ,'Number of path traversed' : list_article_count_wp  , 'Number of times traversed': human_path_count_rp ,'Number of path traversed Shortest':Shortest_article_count_wp , 'Number of time traversed Shortest':shortest_path_count_rp})
df_bfs.to_csv('category-paths.csv' , index = False , header = False)