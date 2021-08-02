import json
import requests
import csv
import pandas as pd
import numpy as np
#import import_ipynb
from question1 import modified_dist
from question1 import id_dist
from statistics import pstdev

pd.set_option('display.max_rows', None)

# list_id_modified_dist1 = []
# for al in modified_dist:
# list_id_modified_dist1.append(id_dist.get(al))
week_qu2 = pd.read_csv('Cases-week.csv')
edge = pd.read_csv('edge-graph.csv')

with open('neighbor-week.csv', 'w', newline='') as nei_dis1:
    the_writer1 = csv.writer(nei_dis1)
    the_writer1.writerow(['id', 'timeid', 'mean', 'sd'])

    for z1 in range(101, 820):
        mk1 = edge.loc[(edge.iloc[:, 0] == z1)]
        dfg = mk1.iloc[:, 1]  # neightbours of z1
        lengt = len(dfg)

        # print(lengt)

        for xc in range(1, 26):
            count = xc
            sd_list = []
            su = 0
            mean = 0
            sd = 0
            for rw in dfg:
                se = week_qu2.loc[(week_qu2.iloc[:, 0] == rw) & (week_qu2.iloc[:, 1] == xc)]
                # print(se)
                # se.iloc[:,2]
                if (se.empty == False):
                    su = su + float(se.iloc[0:, 2])
                    # print(su)
                    sd_list.append(float(se.iloc[0:, 2]))
                if (lengt != 0):
                    mean = "{:.2f}".format(su / lengt)
                else:
                    mean = 0
                if (len(sd_list) >= 2):
                    sd = "{:.2f}".format(pstdev(sd_list))
                else:
                    sd = 0
            # print(lengt)
            # print(z1, count , mean, sd)
            the_writer1.writerow([z1, count, mean, sd])
# for month

month_qu2 = pd.read_csv('Cases-Month.csv')

with open('neighbor-month.csv', 'w', newline='') as nei_dis2:
    the_writer2 = csv.writer(nei_dis2)
    the_writer2.writerow(['id', 'timeid', 'mean', 'sd'])

    for z2 in range(101, 820):
        mk2 = edge.loc[(edge.iloc[:, 0] == z2)]
        dfg2 = mk2.iloc[:, 1]  # neightbours of z1
        lengt2 = len(dfg2)

        for xc2 in range(1, 8):
            count2 = xc2
            sd_list2 = []
            su2 = 0
            mean2 = 0
            sd2 = 0
            for rw2 in dfg2:
                se2 = month_qu2.loc[(month_qu2.iloc[:, 0] == rw2) & (month_qu2.iloc[:, 1] == xc2)]
                # print(se)
                # se.iloc[:,2]
                if (se2.empty == False):
                    su2 = su2 + float(se2.iloc[0:, 2])
                    # print(su)
                    sd_list2.append(float(se2.iloc[0:, 2]))
                if (lengt2 != 0):
                    mean2 = "{:.2f}".format(su2 / lengt2)
                else:
                    mean2 = 0
                if (len(sd_list2) >= 2):
                    sd2 = "{:.2f}".format(pstdev(sd_list2))
                else:
                    sd2 = 0
            # print(lengt)
            # print(z1, count , mean, sd)
            the_writer2.writerow([z2, count2, mean2, sd2])
# for overall

overall_qu2 = pd.read_csv('cases-overall.csv')

with open('neighbor-overall.csv', 'w', newline='') as nei_dis3:
    the_writer3 = csv.writer(nei_dis3)
    the_writer3.writerow(['id', 'timeid', 'mean', 'sd'])

    for z3 in range(101, 820):
        mk3 = edge.loc[(edge.iloc[:, 0] == z3)]
        dfg3 = mk3.iloc[:, 1]  # neightbours of z1
        lengt3 = len(dfg3)

        for xc3 in range(1, 2):
            count3 = xc3
            sd_list3 = []
            su3 = 0
            mean3 = 0
            sd3 = 0
            for rw3 in dfg3:
                se3 = overall_qu2.loc[(overall_qu2.iloc[:, 0] == rw3) & (overall_qu2.iloc[:, 1] == xc3)]
                # print(se)
                # se.iloc[:,2]
                if (se3.empty == False):
                    su3 = su3 + float(se3.iloc[0:, 2])
                    # print(su)
                    sd_list3.append(float(se3.iloc[0:, 2]))
                if (lengt3 != 0):
                    mean3 = "{:.2f}".format(su3 / lengt3)
                else:
                    mean3 = 0
                if (len(sd_list3) >= 2):
                    sd3 = "{:.2f}".format(pstdev(sd_list3))
                else:
                    sd3 = 0
            # print(lengt)
            # print(z1, count , mean, sd)
            the_writer3.writerow([z3, count3, mean3, sd3])