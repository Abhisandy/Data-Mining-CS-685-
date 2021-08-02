import pandas as pd
import numpy as np
import csv
from collections import OrderedDict
from Ques_2 import dict_diff_articleAndCategory_id
from Ques_1 import index_real

df_ShortestPath = pd.read_csv("Data/shortest-path-distance-matrix.txt",sep="\tab",header = None,engine='python')
df_ShortestPath = df_ShortestPath.iloc[16:]

first = 0
with open('edges.csv', 'w', newline='') as nei_dis:
    the_writer = csv.writer(nei_dis)
    for index, row in df_ShortestPath.iterrows():
        second = 0
        for i in range(0,4604) :
            if row[0][i] == '1' :
                the_writer.writerow([index_real[first] , index_real[second]])
            second  = second + 1
        first = first + 1