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

list_path_split_Q9.pop(2395)

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

pair_fin = []
for i in new_list_path_split_Q9:
    pair_fin.append(( list(dict_names.keys())[list(dict_names.values()).index(i[0])] , list(dict_names.keys())[list(dict_names.values()).index(i[-1])] ))

df_PathunFinished = pd.read_csv("Data/paths_unfinished.tsv",sep="\tab",header = None,engine='python')
df_PathunFinished = df_PathunFinished.iloc[16:]

un_list_path = []
for index, row in df_PathunFinished.iterrows():
    un_list_path.append(row.iloc[0].split('\t'))

un_list_path_split = []
for sp in un_list_path:
    un_list_path_split.append(sp[3].split(';'))

target = []
for s in un_list_path:
    if (s[4] == 'Long_peper') or (s[4] == 'Test') or (s[4] == 'Adolph_Hitler') or (s[4] == 'Netbook') or (s[4] == 'Podcast') or (s[4] == 'Christmas') or (s[4] == 'Sportacus') or (s[4] == 'Charlottes_web') or (s[4] == 'C++') or (s[4] == 'Macedonia') or (s[4] == 'Usa') or (s[4] == '_Zebra') or (s[4] == 'Rss') or (s[4] == 'Black_ops_2') or (s[4] == 'Western_Australia') or (s[4] == 'The_Rock') or (s[4] == 'Great') or (s[4] == 'Georgia') or (s[4] == 'English') or (s[4] == 'Fats') or (s[4] == 'Mustard') or (s[4] == 'Bogota') or (s[4] == 'The') or (s[4] == 'Rat') or (s[4] == 'Kashmir'):
        target.append('A9999')
    else:
        target.append(list(dict_names.keys())[list(dict_names.values()).index(s[4])])

un_new_list_path_split = []
for st in un_list_path_split:
    t = []
    for m in range(0 , len(st)):
        if st[m] == '<':
            t.pop(-1)
        else:
            t.append(st[m])
    un_new_list_path_split.append(t)

source = []
for u in un_new_list_path_split:
    source.append(( list(dict_names.keys())[list(dict_names.values()).index(u[0])] ))

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
list_sub_cat_id['A9999'] = ['C0001']

for sub in list_sub_cat_id.keys():
    list_sub_cat_id[sub] = list(set(list_sub_cat_id[sub]))

pair_fin_permute = []
for a in pair_fin:
    a1 = list_sub_cat_id[a[0]]
    a2 = list_sub_cat_id[a[1]]
    for r in itertools.product(a1, a2):
        pair_fin_permute.append((r[0] , r[1]))

dict_count_fin = Counter(pair_fin_permute)

pair_permute = []
for a in range(0 , len(source)):
    a1 = list_sub_cat_id[source[a]]
    a2 = list_sub_cat_id[target[a]]
    for r in itertools.product(a1, a2):
        pair_permute.append((r[0] , r[1]))

dict_count = Counter(pair_permute)

both = {}
for x in dict_count_fin.keys():
    if x in dict_count.keys():
        x1 = dict_count_fin[x] / (dict_count[x] + dict_count_fin[x])
        both[x] = [x1*100 , (1-x1)*100]
    else:
        both[x] = [1*100 , 0]
for x in dict_count.keys():
    if x in both.keys():
        pass
    else:
        both[x] = [0 , 1*100]

with open('category-pairs.csv', 'w', newline='') as ni_dis:
    the_writer2 = csv.writer(ni_dis)
    for elem in sorted(both.items()) :
        the_writer2.writerow([ elem[0][0] , elem[0][1]  , elem[1][0] ,elem[1][1] ])
