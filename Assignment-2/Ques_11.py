import pandas as pd
import numpy as np
import re
import csv
import sys
import itertools
from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from Ques_1 import dict_names
from Ques_2 import dict_diff_articleAndCategory_id
from Ques_2 import dict_category
from Ques_2 import list_categories

df_PathFinished = pd.read_csv("Data/paths_finished.tsv",sep="\tab",header = None,engine='python')
df_PathFinished = df_PathFinished.iloc[15:]

list_path_Q9 = []
for index, row in df_PathFinished.iterrows():
    list_path_Q9.append(row.iloc[0].split('\t'))

list_path_split_Q9 = []
for sp in list_path_Q9:
    list_path_split_Q9.append(sp[3].split(';'))

new_list_path_split_Q9 = []
for st in list_path_split_Q9:
    if len(st) != 1:
        t = []
        for m in range(0 , len(st)):
            if st[m] == '<':
                t.pop(-1)
            else:
                t.append(st[m])
        new_list_path_split_Q9.append(t)

new_list_path_split_Q9.pop(2395)

pair_fin = []
for i in new_list_path_split_Q9:
    pair_fin.append(( list(dict_names.keys())[list(dict_names.values()).index(i[0])] , list(dict_names.keys())[list(dict_names.values()).index(i[-1])] ))

dict_human_path = {}
for h in new_list_path_split_Q9:
    if (list(dict_names.keys())[list(dict_names.values()).index(h[0])],
        list(dict_names.keys())[list(dict_names.values()).index(h[-1])]) in dict_human_path:
        dict_human_path[(list(dict_names.keys())[list(dict_names.values()).index(h[0])],
                         list(dict_names.keys())[list(dict_names.values()).index(h[-1])])].append(len(h) - 1)
    else:
        dict_human_path[(list(dict_names.keys())[list(dict_names.values()).index(h[0])],
                         list(dict_names.keys())[list(dict_names.values()).index(h[-1])])] = [len(h) - 1]

list_sub_cat_id = {}

for ab in list_categories:
    y = []
    if len(ab[1]) == 1:

        if list(dict_names.keys())[list(dict_names.values()).index(ab[0])] in list_sub_cat_id.keys():
            list_sub_cat_id[list(dict_names.keys())[list(dict_names.values()).index(ab[0])]].append(
                dict_category.get(ab[1][0]))
        else:
            y.append(dict_category.get(ab[1][0]))
            list_sub_cat_id[list(dict_names.keys())[list(dict_names.values()).index(ab[0])]] = y

    elif len(ab[1]) == 2:
        if list(dict_names.keys())[list(dict_names.values()).index(ab[0])] in list_sub_cat_id.keys():
            list_sub_cat_id[list(dict_names.keys())[list(dict_names.values()).index(ab[0])]].append(
                dict_category.get(ab[1][0]))
            list_sub_cat_id[list(dict_names.keys())[list(dict_names.values()).index(ab[0])]].append(
                dict_category.get(ab[1][0] + '.' + ab[1][1]))
        else:
            y.append(dict_category.get(ab[1][0]))
            y.append(dict_category.get(ab[1][0] + '.' + ab[1][1]))

            list_sub_cat_id[list(dict_names.keys())[list(dict_names.values()).index(ab[0])]] = y
    elif len(ab[1]) == 3:
        if list(dict_names.keys())[list(dict_names.values()).index(ab[0])] in list_sub_cat_id.keys():
            list_sub_cat_id[list(dict_names.keys())[list(dict_names.values()).index(ab[0])]].append(
                dict_category.get(ab[1][0]))
            list_sub_cat_id[list(dict_names.keys())[list(dict_names.values()).index(ab[0])]].append(
                dict_category.get(ab[1][0] + '.' + ab[1][1]))
            list_sub_cat_id[list(dict_names.keys())[list(dict_names.values()).index(ab[0])]].append(
                dict_category.get(ab[1][0] + '.' + ab[1][1] + '.' + ab[1][2]))
        else:

            y.append(dict_category.get(ab[1][0]))
            y.append(dict_category.get(ab[1][0] + '.' + ab[1][1]))
            y.append(dict_category.get(ab[1][0] + '.' + ab[1][1] + '.' + ab[1][2]))

            list_sub_cat_id[list(dict_names.keys())[list(dict_names.values()).index(ab[0])]] = y
    elif len(ab[1]) == 4:
        if list(dict_names.keys())[list(dict_names.values()).index(ab[0])] in list_sub_cat_id.keys():
            list_sub_cat_id[list(dict_names.keys())[list(dict_names.values()).index(ab[0])]].append(
                dict_category.get(ab[1][0]))
            list_sub_cat_id[list(dict_names.keys())[list(dict_names.values()).index(ab[0])]].append(
                dict_category.get(ab[1][0] + '.' + ab[1][1]))
            list_sub_cat_id[list(dict_names.keys())[list(dict_names.values()).index(ab[0])]].append(
                dict_category.get(ab[1][0] + '.' + ab[1][1] + '.' + ab[1][2]))
            list_sub_cat_id[list(dict_names.keys())[list(dict_names.values()).index(ab[0])]].append(
                dict_category.get(ab[1][0] + '.' + ab[1][1] + '.' + ab[1][2] + '.' + ab[1][3]))
        else:

            y.append(dict_category.get(ab[1][0]))
            y.append(dict_category.get(ab[1][0] + '.' + ab[1][1]))
            y.append(dict_category.get(ab[1][0] + '.' + ab[1][1] + '.' + ab[1][2]))
            y.append(dict_category.get(ab[1][0] + '.' + ab[1][1] + '.' + ab[1][2] + '.' + ab[1][3]))
            list_sub_cat_id[list(dict_names.keys())[list(dict_names.values()).index(ab[0])]] = y


list_sub_cat_id['A3254'] = ['C0001']
list_sub_cat_id['1211'] = ['C0001']
list_sub_cat_id['A1232'] = ['C0001']
list_sub_cat_id['A1601'] = ['C0001']
list_sub_cat_id['A3850'] = ['C0001']
list_sub_cat_id['A4546'] = ['C0001']

for sub in list_sub_cat_id.keys():
    list_sub_cat_id[sub] = list(set(list_sub_cat_id[sub]))

pair_cat_permute = []
for a in pair_fin:
    a1 = list_sub_cat_id[a[0]]
    a2 = list_sub_cat_id[a[1]]
    for r in itertools.product(a1, a2):
        pair_cat_permute.append((r[0] , r[1]))

dict_count_fin = Counter(pair_cat_permute)
l_fin_key = list(dict_count_fin.keys())

lfin0 = []
lfin1 = []
for r in l_fin_key:
    lfin0.append(r[0])
    lfin1.append(r[1])

dict_cat_art = [[] for i in range(146)]
for ai in list_sub_cat_id.keys():
    for b in list_sub_cat_id[ai]:
        a = b
        a1 = re.findall('\d+', a )
        a11 = int(a1[0])
        dict_cat_art[a11 - 1].append(ai)

df_ShortestPath = pd.read_csv("Data/shortest-path-distance-matrix.txt",sep="\tab",header = None,engine='python')
df_ShortestPath = df_ShortestPath.iloc[16:]

srt_path = []
hum_path = []
# l_fin_key_t = [('C0002' , 'C0003')]
for x in l_fin_key:
    a = x[0]
    a1 = re.findall('\d+', a)
    a11 = int(a1[0])

    b = x[1]
    b1 = re.findall('\d+', b)
    b11 = int(b1[0])

    a1 = dict_cat_art[a11 - 1]
    a2 = dict_cat_art[b11 - 1]
    sp = 0
    hp = 0
    for r in itertools.product(a1, a2):

        if (r[0], r[1]) in dict_human_path.keys():
            u = int(r[0][1] + r[0][2] + r[0][3] + r[0][4])
            v = int(r[1][1] + r[1][2] + r[1][3] + r[1][4])
            xb = df_ShortestPath.iloc[u - 1][0][v - 1]
            if xb != '_':
                for bn in dict_human_path[(r[0], r[1])]:
                    hp = hp + bn
                    sp = sp + int(xb)

    srt_path.append(sp)
    hum_path.append(hp)

ans = []
for an in range(0 , len(srt_path)):
    ans.append(hum_path[an]/srt_path[an])

df_ans = pd.DataFrame({'a': lfin0  ,'b' : lfin1  , 'c': ans})
df_ans.sort_values(['a', 'b'], ascending=[True, True], inplace=True)
df_ans.to_csv('category-ratios.csv' , index = False , header = False)