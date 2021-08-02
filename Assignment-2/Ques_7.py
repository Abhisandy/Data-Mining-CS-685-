import pandas as pd
import numpy as np
import re
import csv
import sys
from collections import defaultdict
from collections import OrderedDict
from Ques_1 import dict_names

df_Finished_back = pd.read_csv("finished-paths-back.csv" , header = None)
df_Finished_without_back = pd.read_csv("finished-paths-no-back.csv" , header = None)

len_df = len(df_Finished_back)

exact = 0
pathlen_1 = 0
pathlen_2 = 0
pathlen_3 = 0
pathlen_4 = 0
pathlen_5 = 0
pathlen_6 = 0
pathlen_7 = 0
pathlen_8 = 0
pathlen_9 = 0
pathlen_10 = 0
pathlen_11 = 0
for index, row in df_Finished_back.iterrows():
        if row.iloc[0] - row.iloc[1] == 0:
            exact = exact + 1
        if row.iloc[0] - row.iloc[1] == 1:
            pathlen_1 = pathlen_1 + 1
        if row.iloc[0] - row.iloc[1] == 2:
            pathlen_2 = pathlen_2 + 1
        if row.iloc[0] - row.iloc[1] == 3:
            pathlen_3 = pathlen_3 + 1
        if row.iloc[0] - row.iloc[1] == 4:
            pathlen_4 = pathlen_4 + 1
        if row.iloc[0] - row.iloc[1] == 5:
            pathlen_5 = pathlen_5 + 1
        if row.iloc[0] - row.iloc[1] == 6:
            pathlen_6 = pathlen_6 + 1
        if row.iloc[0] - row.iloc[1] == 7:
            pathlen_7 = pathlen_7 + 1
        if row.iloc[0] - row.iloc[1] == 8:
            pathlen_8 = pathlen_8 + 1
        if row.iloc[0] - row.iloc[1] == 9:
            pathlen_9 = pathlen_9 + 1
        if row.iloc[0] - row.iloc[1] == 10:
            pathlen_10 = pathlen_10 + 1
        if row.iloc[0] - row.iloc[1] >= 11:
            pathlen_11 = pathlen_11 + 1

exact_per = (exact/len_df)*100
pathlen_1_per = (pathlen_1/len_df)*100
pathlen_2_per = (pathlen_2/len_df)*100
pathlen_3_per = (pathlen_3/len_df)*100
pathlen_4_per = (pathlen_4/len_df)*100
pathlen_5_per = (pathlen_5/len_df)*100
pathlen_6_per = (pathlen_6/len_df)*100
pathlen_7_per = (pathlen_7/len_df)*100
pathlen_8_per = (pathlen_8/len_df)*100
pathlen_9_per = (pathlen_9/len_df)*100
pathlen_10_per = (pathlen_10/len_df)*100
pathlen_11_per = (pathlen_11/len_df)*100

with open('percentage-paths-back.csv', 'w', newline='') as wbt:
    the_wbt = csv.writer(wbt)
    the_wbt.writerow([ exact_per , pathlen_1_per , pathlen_2_per , pathlen_3_per , pathlen_4_per , pathlen_5_per , pathlen_6_per , pathlen_7_per , pathlen_8_per , pathlen_9_per , pathlen_10_per , pathlen_11_per  ])

len_df_without_BT = len(df_Finished_without_back)
exact_wBT = 0
pathlen_1_wBT = 0
pathlen_2_wBT = 0
pathlen_3_wBT = 0
pathlen_4_wBT = 0
pathlen_5_wBT = 0
pathlen_6_wBT = 0
pathlen_7_wBT = 0
pathlen_8_wBT = 0
pathlen_9_wBT = 0
pathlen_10_wBT = 0
pathlen_11_wBT = 0
for index, row in df_Finished_without_back.iterrows():
        if row.iloc[0] - row.iloc[1] == 0:
            exact_wBT = exact_wBT + 1
        if row.iloc[0] - row.iloc[1] == 1:
            pathlen_1_wBT = pathlen_1_wBT + 1
        if row.iloc[0] - row.iloc[1] == 2:
            pathlen_2_wBT = pathlen_2_wBT + 1
        if row.iloc[0] - row.iloc[1] == 3:
            pathlen_3_wBT = pathlen_3_wBT + 1
        if row.iloc[0] - row.iloc[1] == 4:
            pathlen_4_wBT = pathlen_4_wBT + 1
        if row.iloc[0] - row.iloc[1] == 5:
            pathlen_5_wBT = pathlen_5_wBT + 1
        if row.iloc[0] - row.iloc[1] == 6:
            pathlen_6_wBT = pathlen_6_wBT + 1
        if row.iloc[0] - row.iloc[1] == 7:
            pathlen_7_wBT = pathlen_7_wBT + 1
        if row.iloc[0] - row.iloc[1] == 8:
            pathlen_8_wBT = pathlen_8_wBT + 1
        if row.iloc[0] - row.iloc[1] == 9:
            pathlen_9_wBT = pathlen_9_wBT + 1
        if row.iloc[0] - row.iloc[1] == 10:
            pathlen_10_wBT = pathlen_10_wBT + 1
        if row.iloc[0] - row.iloc[1] >= 11:
            pathlen_11_wBT = pathlen_11_wBT + 1

exact_per_wBT = (exact_wBT/len_df_without_BT)*100
pathlen_1_per_wBT = (pathlen_1_wBT/len_df_without_BT)*100
pathlen_2_per_wBT = (pathlen_2_wBT/len_df_without_BT)*100
pathlen_3_per_wBT = (pathlen_3_wBT/len_df_without_BT)*100
pathlen_4_per_wBT = (pathlen_4_wBT/len_df_without_BT)*100
pathlen_5_per_wBT = (pathlen_5_wBT/len_df_without_BT)*100
pathlen_6_per_wBT = (pathlen_6_wBT/len_df_without_BT)*100
pathlen_7_per_wBT = (pathlen_7_wBT/len_df_without_BT)*100
pathlen_8_per_wBT = (pathlen_8_wBT/len_df_without_BT)*100
pathlen_9_per_wBT = (pathlen_9_wBT/len_df_without_BT)*100
pathlen_10_per_wBT = (pathlen_10_wBT/len_df_without_BT)*100
pathlen_11_per_wBT = (pathlen_11_wBT/len_df_without_BT)*100

with open('percentage-paths-no-back.csv', 'w', newline='') as bt:
    the_bt = csv.writer(bt)
    the_bt.writerow([ exact_per_wBT , pathlen_1_per_wBT , pathlen_2_per_wBT , pathlen_3_per_wBT , pathlen_4_per_wBT , pathlen_5_per_wBT , pathlen_6_per_wBT , pathlen_7_per_wBT , pathlen_8_per_wBT , pathlen_9_per_wBT , pathlen_10_per_wBT , pathlen_11_per_wBT  ])