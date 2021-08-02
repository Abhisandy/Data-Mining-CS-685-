import json
import requests
import csv
import pandas as pd
import numpy as np
#import import_ipynb
from question1 import modified_dist
from question1 import id_dist
from statistics import stdev

q6_week = pd.read_csv('Cases-week.csv')
q6_month = pd.read_csv('Cases-Month.csv')
q6_overall = pd.read_csv('cases-overall.csv')
q6_stateweek = pd.read_csv('state-week.csv')
q6_statemonth = pd.read_csv('state-month.csv')
q6_stateoverall = pd.read_csv('state-overall.csv')
q6_neibhborweek = pd.read_csv('neighbor-week.csv')
q6_neighbormonth = pd.read_csv('neighbor-month.csv')
q6_neighboroverall = pd.read_csv('neighbor-overall.csv')

with open('zscore-week.csv', 'w', newline='') as zw:
    the_zw = csv.writer(zw)
    the_zw.writerow(['id', 'timeid', 'z_neighbour', 'z_state'])

    for dd in range(101, 820):
        for ff in range(1, 26):
            x = 0
            xs = 0
            df6_w = q6_week.loc[(q6_week.iloc[:, 0] == dd) & (q6_week.iloc[:, 1] == ff)]
            df6_n = q6_neibhborweek.loc[(q6_neibhborweek.iloc[:, 0] == dd) & (q6_neibhborweek.iloc[:, 1] == ff)]
            df6_s = q6_stateweek.loc[(q6_stateweek.iloc[:, 0] == dd) & (q6_stateweek.iloc[:, 1] == ff)]
            if (df6_n.empty == False) & (df6_s.empty == False):
                w_value = float(df6_w.iloc[0:, 2])  # cases in that particular district
                n_value_mean = float(df6_n.iloc[0:, 2])
                n_value_sd = float(df6_n.iloc[0:, 3])
                s_value_mean = float(df6_s.iloc[0:, 2])
                s_value_sd = float(df6_s.iloc[0:, 3])
                if n_value_sd != 0:
                    x = "{:.2f}".format((w_value - n_value_mean) / n_value_sd)
                else:
                    x = 0
                if s_value_sd != 0:
                    xs = "{:.2f}".format((w_value - s_value_mean) / s_value_sd)
                else:
                    xs = 0  # need to check this (when sd is zero)
                the_zw.writerow([dd, ff, x, xs])

with open('zscore-month.csv', 'w', newline='') as zm:
    the_zm = csv.writer(zm)
    the_zm.writerow(['id', 'timeid', 'z_neighbour', 'z_state'])

    for ddm in range(101, 820):
        for ffm in range(1, 8):
            xm = 0
            xsm = 0
            df6_m = q6_month.loc[(q6_month.iloc[:, 0] == ddm) & (q6_month.iloc[:, 1] == ffm)]
            df6_nm = q6_neighbormonth.loc[(q6_neighbormonth.iloc[:, 0] == ddm) & (q6_neighbormonth.iloc[:, 1] == ffm)]
            df6_sm = q6_statemonth.loc[(q6_statemonth.iloc[:, 0] == ddm) & (q6_statemonth.iloc[:, 1] == ffm)]
            if (df6_nm.empty == False) & (df6_sm.empty == False):
                w_valuem = float(df6_m.iloc[0:, 2])  # cases in that particular district
                n_value_meanm = float(df6_nm.iloc[0:, 2])
                n_value_sdm = float(df6_nm.iloc[0:, 3])
                s_value_meanm = float(df6_sm.iloc[0:, 2])
                s_value_sdm = float(df6_sm.iloc[0:, 3])
                if n_value_sdm != 0:
                    xm = "{:.2f}".format((w_valuem - n_value_meanm) / n_value_sdm)
                else:
                    xm = 0  # need to check this (when sd is zero)
                if s_value_sdm != 0:
                    xsm = "{:.2f}".format((w_valuem - s_value_meanm) / s_value_sdm)
                else:
                    xsm = 0

                the_zm.writerow([ddm, ffm, xm, xsm])

with open('zscore-overall.csv', 'w', newline='') as zo:
    the_zo = csv.writer(zo)
    the_zo.writerow(['id', 'timeid', 'z_neighbour', 'z_state'])

    for ddo in range(101, 820):
        for ffo in range(1, 2):
            xo = 0
            xso = 0
            df6_o = q6_overall.loc[(q6_overall.iloc[:, 0]==ddo)&(q6_overall.iloc[:, 1]==ffo)]
            df6_no = q6_neighboroverall.loc[(q6_neighboroverall.iloc[:, 0]==ddo)&(q6_neighboroverall.iloc[:, 1]==ffo)]
            df6_so = q6_stateoverall.loc[(q6_stateoverall.iloc[:, 0]==ddo)&(q6_stateoverall.iloc[:, 1]==ffo)]
            if(df6_no.empty == False)&(df6_so.empty == False):
                w_valueo = int(df6_o.iloc[0:, 2]) #cases in that particular district
                n_value_meano = float(df6_no.iloc[0:, 2])
                n_value_sdo = float(df6_no.iloc[0:, 3])
                s_value_meano = float(df6_so.iloc[0:, 2])
                s_value_sdo = float(df6_so.iloc[0:, 3])
                if n_value_sdo != 0:
                    xo = "{:.2f}".format((w_valueo - n_value_meano)/n_value_sdo)
                else:
                    xo = 0 #need to check this (when sd is zero)
                if s_value_sdo != 0:
                    xso = "{:.2f}".format((w_valueo - s_value_meano) / s_value_sdo)
                else:
                    xso = 0
                the_zo.writerow([ddo, ffo, xo, xso])
