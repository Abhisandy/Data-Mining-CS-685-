import json
import requests
import csv
import pandas as pd
import numpy as np
import os

q7_week = pd.read_csv('Cases-week.csv')
q7_month = pd.read_csv('Cases-Month.csv')
q7_overall = pd.read_csv('cases-overall.csv')
q7_stateweek = pd.read_csv('state-week.csv')
q7_statemonth = pd.read_csv('state-month.csv')
q7_stateoverall = pd.read_csv('state-overall.csv')
q7_neibhborweek = pd.read_csv('neighbor-week.csv')#
q7_neighbormonth = pd.read_csv('neighbor-month.csv')
q7_neighboroverall = pd.read_csv('neighbor-overall.csv')

# week-hot
with open('temprary.csv', 'w', newline='') as zww:
    the_zww = csv.writer(zww)
    the_zww.writerow(['time-id', 'method', 'spot', 'id'])
    for yy in range(1, 26):
        for tt in range(101, 820):
            mean_value = 0
            sd_value = 0
            df7_ms = q7_neibhborweek[((q7_neibhborweek.iloc[:, 0]) == tt) & ((q7_neibhborweek.iloc[:, 1]) == yy)]
            if df7_ms.empty == False:
                mean_value = float(df7_ms.iloc[0:, 2])
                sd_value = float(df7_ms.iloc[:, 3])
                x_value_data = q7_week[((q7_week.iloc[:, 0]) == tt) & ((q7_week.iloc[:, 1]) == yy)]
                x_value = float(x_value_data.iloc[:, 2])
                dif = mean_value + sd_value
                difc = mean_value - sd_value
                if x_value > dif:
                    the_zww.writerow([yy, 'neighborhood', 'hot', tt])
                if x_value < difc:
                    # the_zwwc.writerow([yy, 'neighborhood', 'cold', tt])
                    the_zww.writerow([yy, 'neighborhood', 'cold', tt])
                    #########################################################################
            mean_valuet = 0
            sd_valuet = 0
            df7_mst = q7_stateweek[((q7_stateweek.iloc[:, 0]) == tt) & ((q7_stateweek.iloc[:, 1]) == yy)]
            if df7_mst.empty == False:
                mean_valuet = float(df7_mst.iloc[0:, 2])
                sd_valuet = float(df7_mst.iloc[:, 3])
                dift = mean_valuet + sd_valuet
                difct = mean_valuet - sd_valuet
                if x_value > dift:
                    # the_zww1.writerow([yy, 'state', 'hot', tt])
                    the_zww.writerow([yy, 'state', 'hot', tt])
                if x_value < difct:
                    # the_zwwc1.writerow([yy, 'state', 'cold', tt])
                    the_zww.writerow([yy, 'state', 'cold', tt])

df_sort = pd.read_csv('temprary.csv')
df_sort = df_sort.sort_values(['time-id', 'method', 'spot', 'id'])
df_sort.to_csv('method-spot-week.csv', index=False, header=True)
os.remove('temprary.csv')

# month-hot/cold
with open('temprary1.csv', 'w', newline='') as zwmh:
    the_zwmh = csv.writer(zwmh)
    the_zwmh.writerow(['time-id', 'method', 'spot', 'id'])

    for yymh in range(1, 8):
        for ttmh in range(101, 820):
            mean_valuemh = 0
            sd_valuemh = 0
            df7_mh = q7_neighbormonth[((q7_neighbormonth.iloc[:, 0]) == ttmh) & ((q7_neighbormonth.iloc[:, 1]) == yymh)]
            if df7_mh.empty == False:
                mean_valuemh = float(df7_mh.iloc[0:, 2])
                sd_valuemh = float(df7_mh.iloc[:, 3])
                x_value_datamh = q7_month[((q7_month.iloc[:, 0]) == ttmh) & ((q7_month.iloc[:, 1]) == yymh)]
                x_valuemh = float(x_value_datamh.iloc[:, 2])
                difmh = mean_valuemh + sd_valuemh
                difm_cold = mean_valuemh - sd_valuemh
                if x_valuemh > difmh:
                    the_zwmh.writerow([yymh, 'neighborhood', 'hot', ttmh])
                if x_valuemh < difm_cold:
                    the_zwmh.writerow([yymh, 'neighborhood', 'cold', ttmh])
                    ############################################################################################
            mean_valuemhs = 0
            sd_valuemhs = 0
            df7_mhs = q7_statemonth[((q7_statemonth.iloc[:, 0]) == ttmh) & ((q7_statemonth.iloc[:, 1]) == yymh)]
            if df7_mhs.empty == False:
                mean_valuemhs = float(df7_mhs.iloc[0:, 2])
                sd_valuemhs = float(df7_mhs.iloc[:, 3])
                difmhs = mean_valuemhs + sd_valuemhs
                difm_colds = mean_valuemhs - sd_valuemhs
                if x_valuemh > difmhs:
                    the_zwmh.writerow([yymh, 'state', 'hot', ttmh])
                if x_valuemh < difm_colds:
                    the_zwmh.writerow([yymh, 'state', 'cold', ttmh])

df_sort = pd.read_csv('temprary1.csv')
df_sort = df_sort.sort_values(['time-id', 'method', 'spot', 'id'])
df_sort.to_csv('method-spot-month.csv', index=False, header=True)
os.remove('temprary1.csv')

# overall-hot
with open('temprary2.csv', 'w', newline='') as zwwo:
    the_zwwo = csv.writer(zwwo)
    the_zwwo.writerow(['time-id', 'method', 'spot', 'id'])

    for yyo in range(1, 2):
        for tto in range(101, 820):
            mean_valueo = 0
            sd_valueo = 0
            df7_mso = q7_neighboroverall[
                ((q7_neighboroverall.iloc[:, 0]) == tto) & ((q7_neighboroverall.iloc[:, 1]) == yyo)]
            if df7_mso.empty == False:
                mean_valueo = float(df7_mso.iloc[0:, 2])
                sd_valueo = float(df7_mso.iloc[:, 3])
                x_value_datao = q7_overall[((q7_overall.iloc[:, 0]) == tto) & ((q7_overall.iloc[:, 1]) == yyo)]
                x_valueo = float(x_value_datao.iloc[:, 2])
                difo = mean_valueo + sd_valueo
                difoc = mean_valueo - sd_valueo
                if x_valueo > difo:
                    the_zwwo.writerow([yyo, 'neighborhood', 'hot', tto])
                if x_valueo < difoc:
                    the_zwwo.writerow([yyo, 'neighborhood', 'cold', tto])
                    ##################################################################
            mean_stateo = 0
            sd_stateo = 0
            df7_stateo = q7_stateoverall[((q7_stateoverall.iloc[:, 0]) == tto) & ((q7_stateoverall.iloc[:, 1]) == yyo)]
            if df7_stateo.empty == False:
                mean_stateo = float(df7_stateo.iloc[0:, 2])
                sd_stateo = float(df7_stateo.iloc[:, 3])
                dif_stateo = mean_stateo + sd_stateo
                difstateoc = mean_stateo - sd_stateo
                if x_valueo > dif_stateo:
                    the_zwwo.writerow([yyo, 'state', 'hot', tto])
                if x_valueo < difstateoc:
                    the_zwwo.writerow([yyo, 'state', 'cold', tto])

df_sort = pd.read_csv('temprary2.csv')
df_sort = df_sort.sort_values(['time-id', 'method', 'spot', 'id'])
df_sort.to_csv('method-spot-overall.csv', index=False, header=True)
os.remove('temprary2.csv')



