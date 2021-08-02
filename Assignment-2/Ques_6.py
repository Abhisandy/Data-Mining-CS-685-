import pandas as pd
import numpy as np
import re
import csv
import sys
from collections import defaultdict
from collections import OrderedDict
from Ques_1 import dict_names

df_ShortestPath = pd.read_csv("Data/shortest-path-distance-matrix.txt",sep="\tab",header = None,engine='python')
df_ShortestPath = df_ShortestPath.iloc[16:]
df_PathFinished = pd.read_csv("Data/paths_finished.tsv",sep="\tab",header = None,engine='python')
df_PathFinished = df_PathFinished.iloc[15:]

list_path = []
for index, row in df_PathFinished.iterrows():
    list_path.append(row.iloc[0].split('\t'))

list_path_split = []
for sp in list_path:
    list_path_split.append(sp[3].split(';'))
list_path_split.pop(2395)

human_path_len = []
human_path_len_without_backtrack = []
for ln in list_path_split:
    if (len(ln)) != 1:
        backTrack = ln.count('<')
        human_path_len.append(len(ln) - 1)
        human_path_len_without_backtrack.append(len(ln) - 2*backTrack - 1)

shortest_path = []
for el in list_path_split:
    backTrack1 = el.count('<')
    if (len(el) - 2*backTrack1 ) != 1:
        a = list(dict_names.keys())[list(dict_names.values()).index(el[0])]
        b = list(dict_names.keys())[list(dict_names.values()).index(el[-1])]
        a1 = re.findall('\d+', a )
        a11 = int(a1[0])
        b1 = re.findall('\d+', b )
        b11 = int(b1[0])

        xa = df_ShortestPath.iloc[a11-1]
        xb = xa[0][b11-1]
        if(xb!='_'):
            shortest_path.append(xb)
        else:
            pass

List_Ratio = []
List_Ratio_without_backtrack = []
for item in range(0,len(human_path_len)):
    if(shortest_path[item]!='Inf') & (shortest_path[item]!='0'):
        List_Ratio.append("{:.6f}".format(human_path_len[item]/int(shortest_path[item])))
        List_Ratio_without_backtrack.append("{:.6f}".format(human_path_len_without_backtrack[item]/int(shortest_path[item])))
    else:
        pass

df_path_BT = pd.DataFrame({'Human Path':human_path_len , 'Shortest Path':shortest_path  , 'Ratio':List_Ratio})
df_path_BT.to_csv('finished-paths-back.csv' , index = False , header = False)
df_path_BT = pd.DataFrame({'Human Path':human_path_len_without_backtrack , 'Shortest Path':shortest_path  , 'Ratio':List_Ratio_without_backtrack})
df_path_BT.to_csv('finished-paths-no-back.csv' , index = False , header = False)