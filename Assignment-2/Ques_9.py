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
from Ques_2 import list_categories
from Ques_8 import list_article_count

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

dict_cat_art_Q9 = [[] for i in range(146)]
for aii in list_sub_cat_id.keys():
    for b in list_sub_cat_id[aii]:
        a = b
        a1 = re.findall('\d+', a )
        a11 = int(a1[0])
        dict_cat_art_Q9[a11 - 1].append(aii)

human_path_count_rp_Q9 = []
for di in dict_cat_art_Q9:
    s = 0
    for el in di:
        a = el
        a1 = re.findall('\d+', a )
        a11 = int(a1[0])
        s = s + list_article_count[a11-1]
    human_path_count_rp_Q9.append(s)

list_article_count_wp_Q9 = [0] * 146
for ai in new_list_path_split_Q9:
    leni = len(ai)
    bo1 = [0] * 146

    for i, ele in enumerate(ai):

        a = list(dict_names.keys())[list(dict_names.values()).index(ele)]

        for m in list_sub_cat_id[a]:
            a = m
            a1 = re.findall('\d+', a)
            a11 = int(a1[0])
            if (bo1[a11 - 1] == 0):
                list_article_count_wp_Q9[a11 - 1] = list_article_count_wp_Q9[a11 - 1] + 1
                bo1[a11 - 1] = 1
    bo1.clear()


df_SP = pd.read_csv("Data/shrtpath.csv", sep='\n', header=None)
list_SP_Q9 = []
for index, row in df_SP.iterrows():
    list_SP_Q9.append(str(row.iloc[0]).split(','))
list_SP_count_Q9 = [0]*4604
for a in list_SP_Q9:
    for b in a:
        if (b!= '') & (b != 'NA') & (b != 'nan'):
            x = int(b)
            list_SP_count_Q9[x - 1] = list_SP_count_Q9[x - 1] + 1

shortest_path_count_rp_Q9 = []
for di in dict_cat_art_Q9:
    s = 0
    for el in di:
        a = el
        a1 = re.findall('\d+', a )
        a11 = int(a1[0])
        s = s + list_SP_count_Q9[a11-1]
    shortest_path_count_rp_Q9.append(s)

Shortest_article_count_wp_Q9 = [0] * 146
for ai in list_SP_Q9:
    leni = len(ai)
    bo = [0] * 146

    for i, ele in enumerate(ai):
        if (ele != '') & (ele != 'NA') & (ele != 'nan'):
            a = ('A' + "{:04d}".format(int(ele)))
            # print(a)
            for m in list_sub_cat_id[a]:
                a = m
                a1 = re.findall('\d+', a)
                a11 = int(a1[0])
                if (bo[a11 - 1] == 0):
                    Shortest_article_count_wp_Q9[a11 - 1] = Shortest_article_count_wp_Q9[a11 - 1] + 1
                    bo[a11 - 1] = 1
    bo.clear()

cat_li_Q9 = []
for s in dict_category.values():
    cat_li_Q9.append(s)

df_bfs_Q9 = pd.DataFrame({'Cat.Id': cat_li_Q9  ,'Number of path traversed' : list_article_count_wp_Q9  , 'Number of times traversed': human_path_count_rp_Q9 ,'Number of path traversed Shortest':Shortest_article_count_wp_Q9 , 'Number of time traversed Shortest':shortest_path_count_rp_Q9})
df_bfs_Q9.to_csv('category-subtree-paths.csv' , index = False , header = False)