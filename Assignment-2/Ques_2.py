import pandas as pd
import numpy as np
from collections import OrderedDict
from Ques_1 import dict_names
from Ques_1 import list_t

df_categories = pd.read_csv("Data/categories.tsv",sep="\tab",header = None,engine='python')
df_categories = df_categories.iloc[12:]

list_categories = []
for index, row in df_categories.iterrows():
    list_categories.append(row.iloc[0].split('\t'))

list_category_only = []
for e in list_categories:
    list_category_only.append(e[1])

list_category_only_split  = []
for f in list_category_only:
    list_category_only_split.append(f.split('.'))

heirarchy_lvl_1 = []
heirarchy_lvl_2 = []
heirarchy_lvl_3 = []
heirarchy_lvl_4 = []
count_1 = 0
for g in list_category_only_split:
    count_1 = 0
    if count_1<len(g):
        count_1 += 1
        heirarchy_lvl_1.append(g[0])
    if count_1<len(g):
        count_1 += 1
        heirarchy_lvl_2.append(g[0]+'.'+g[1])
    if  count_1<len(g):
        count_1 += 1
        heirarchy_lvl_3.append(g[0]+'.'+g[1]+'.'+g[2])
    if  count_1<len(g):
        count_1 += 1
        heirarchy_lvl_4.append(g[0]+'.'+g[1]+'.'+g[2]+'.'+g[3])

heirarchy_lvl_1.sort()
heirarchy_lvl_2.sort()
heirarchy_lvl_3.sort()
heirarchy_lvl_4.sort()
heirarchy_lvl_1_different = list(OrderedDict.fromkeys(heirarchy_lvl_1))
heirarchy_lvl_2_different = list(OrderedDict.fromkeys(heirarchy_lvl_2))
heirarchy_lvl_3_different = list(OrderedDict.fromkeys(heirarchy_lvl_3))
heirarchy_lvl_4_different = list(OrderedDict.fromkeys(heirarchy_lvl_4))

list_category_id = []
for h in range(1, len(heirarchy_lvl_1_different) + 1):
    list_category_id.append('C' + "{:04d}".format(h))

dict_category = {}
count_2 = 0

for i in heirarchy_lvl_1_different:
    dict_category[i] = list_category_id[count_2]
    count_2 = count_2 + 1

for j in range(len(heirarchy_lvl_1_different)+1, len(heirarchy_lvl_2_different)+len(heirarchy_lvl_1_different)+1):
    list_category_id.append('C'+"{:04d}".format(j))

for k in heirarchy_lvl_2_different:
    dict_category[k] = list_category_id[count_2]
    count_2 = count_2 + 1

extra_len = 0
for g2 in heirarchy_lvl_2_different:
    list_temp = []
    for g1 in list_category_only_split:
        count_1 = 2
        if len(g1) >= 3:
            if (g1[0]+'.'+g1[1]) == g2:
                list_temp.append(g1[0]+'.'+g1[1]+'.'+g1[2])
    list_temp.sort()
    list_temp = list(OrderedDict.fromkeys(list_temp))

    for l in range(extra_len+len(heirarchy_lvl_1_different)+len(heirarchy_lvl_2_different)+1 , extra_len+len(list_temp)+len(heirarchy_lvl_2_different)+len(heirarchy_lvl_1_different)+1):
        list_category_id.append('C'+"{:04d}".format(l))
    for k in list_temp:
        dict_category[k] = list_category_id[count_2]
        count_2 = count_2 + 1
    extra_len = extra_len + len(list_temp)

len_dict = len(dict_category)

extra_len = 0
for g2 in heirarchy_lvl_3_different:
    list_temp = []
    for g1 in list_category_only_split:
        count_1 = 2
        if len(g1) >= 4:
            if g1[0]+'.'+g1[1]+'.'+g1[2] == g2:
                list_temp.append(g1[0]+'.'+g1[1]+'.'+g1[2]+'.'+g1[3])
    list_temp.sort()
    list_temp = list(OrderedDict.fromkeys(list_temp))

    for l in range(extra_len + len_dict + 1 , extra_len + len(list_temp) + len_dict + 1):
        list_category_id.append('C'+"{:04d}".format(l))

    for k in list_temp:
        dict_category[k] = list_category_id[count_2]
        count_2 = count_2 + 1
    extra_len = extra_len + len(list_temp)

list_of_dictKeys = []
for p in dict_category.keys():
    list_of_dictKeys.append(p)

list_of_dictValues = []
for q in dict_category.values():
    list_of_dictValues.append(q)

csv_q2 = pd.DataFrame({'Category':list_of_dictKeys , 'Keys':list_of_dictValues})
csv_q2.to_csv('category-ids.csv', index = False , header = False)

for s in list_categories:
    s[1] = s[1].split('.')

dict_diff_articleAndCategory = {}

for t in list_t:
    list_temp = []
    for u in list_categories:
        count_3 = 0
        if t == u[0]:
            if count_3 < len(u[1]):

                if len(u[1]) == 1:
                    list_temp.append(u[1][0])
                count_3 = count_3 + 1

                if count_3 < len(u[1]):

                    if len(u[1]) == 2:
                        list_temp.append(u[1][0] + '.' + u[1][1])
                    count_3 = count_3 + 1

                    if count_3 < len(u[1]):

                        if len(u[1]) == 3:
                            list_temp.append(u[1][0] + '.' + u[1][1] + '.' + u[1][2])
                        count_3 = count_3 + 1

                        if count_3 < len(u[1]):

                            if len(u[1]) == 4:
                                list_temp.append(u[1][0] + '.' + u[1][1] + '.' + u[1][2] + '.' + u[1][3])
                            count_3 = count_3 + 1

    dict_diff_articleAndCategory[t] = list_temp

list_category_articles_different_id = []
for w in list_t:
    list_category_articles_different_id.append(list(dict_names.keys())[list(dict_names.values()).index(w)])

dict_diff_articleAndCategory_id = {}
for x in list_t:
    list_temp = []
    for y in list_categories:

        count_3 = 0
        if x == y[0]:

            if count_3 < len(y[1]):
                if len(y[1]) == 1:
                    list_temp.append(dict_category.get(y[1][0]))
                count_3 = count_3 + 1

                if count_3 < len(y[1]):
                    if len(y[1]) == 2:
                        list_temp.append(dict_category.get(y[1][0] + '.' + y[1][1]))
                    count_3 = count_3 + 1

                    if count_3 < len(y[1]):
                        if len(y[1]) == 3:
                            list_temp.append(dict_category.get(y[1][0] + '.' + y[1][1] + '.' + y[1][2]))
                        count_3 = count_3 + 1

                        if count_3 < len(y[1]):
                            if len(y[1]) == 4:
                                list_temp.append(
                                    dict_category.get(y[1][0] + '.' + y[1][1] + '.' + y[1][2] + '.' + y[1][3]))
                            count_3 = count_3 + 1

    list_temp_different = list(OrderedDict.fromkeys(list_temp))
    list_temp_different.sort()
    dict_diff_articleAndCategory_id[list(dict_names.keys())[list(dict_names.values()).index(x)]] = list_temp_different

lis = ['C0001']
for x in dict_diff_articleAndCategory_id.keys():
    if len(dict_diff_articleAndCategory_id[x]) == 0:
        dict_diff_articleAndCategory_id[x] = lis