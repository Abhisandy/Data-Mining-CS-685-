import json
import requests
import csv
import pandas as pd
import numpy as np

q8_week = pd.read_csv('Cases-week.csv')
q8_month = pd.read_csv('Cases-Month.csv')
q8_overall = pd.read_csv('cases-overall.csv')
q8_zweek = pd.read_csv('zscore-week.csv')
q8_zmonth = pd.read_csv('zscore-month.csv')
q8_zoverall = pd.read_csv('zscore-overall.csv')
q8_stateweek = pd.read_csv('state-week.csv')
q8_statemonth = pd.read_csv('state-month.csv')
q8_stateoverall = pd.read_csv('state-overall.csv')
q8_neibhborweek = pd.read_csv('neighbor-week.csv')
q8_neighbormonth = pd.read_csv('neighbor-month.csv')
q8_neighboroverall = pd.read_csv('neighbor-overall.csv')

with open('top-week.csv', 'w', newline='') as ztw:
    the_ztw = csv.writer(ztw)
    for yymhw in range(1, 26):
        list_hotw = {}
        list_coldw = {}
        list_hotw.clear()
        list_coldw.clear()
        list_hotstw = {}
        list_coldstw = {}
        list_hotstw.clear()
        list_coldstw.clear()
        for ttmhw in range(101, 820):
            mean_valuemhw = 0
            sd_valuemhw = 0
            df8_mhw = q8_neibhborweek[((q8_neibhborweek.iloc[:, 0]) == ttmhw) & ((q8_neibhborweek.iloc[:, 1]) == yymhw)]
            x_value_datamhw = q8_week[((q8_week.iloc[:, 0]) == ttmhw) & ((q8_week.iloc[:, 1]) == yymhw)]
            if df8_mhw.empty == False and x_value_datamhw.empty == False:
                mean_valuemhw = float(df8_mhw.iloc[0:, 2])
                sd_valuemhw = float(df8_mhw.iloc[:, 3])
                x_valuemhw = float(x_value_datamhw.iloc[:, 2])
                difmhw = mean_valuemhw + sd_valuemhw
                difm_coldw = mean_valuemhw - sd_valuemhw

                z_valmw = q8_zweek[((q8_zweek.iloc[:, 0]) == ttmhw) & ((q8_zweek.iloc[:, 1]) == yymhw)]

                if x_valuemhw > difmhw:
                    if z_valmw.empty == False:
                        list_hotw[ttmhw] = float(z_valmw.iloc[0:, 2])
                if x_valuemhw < difm_coldw:
                    if z_valmw.empty == False:
                        list_coldw[ttmhw] = float(z_valmw.iloc[0:, 2])

            mean_valuestw = 0
            sd_valuestw = 0
            df8_stw = q8_stateweek[((q8_stateweek.iloc[:, 0]) == ttmhw) & ((q8_stateweek.iloc[:, 1]) == yymhw)]
            x_value_datastw = q8_week[((q8_week.iloc[:, 0]) == ttmhw) & ((q8_week.iloc[:, 1]) == yymhw)]
            if df8_stw.empty == False and x_value_datastw.empty == False:
                mean_valuestw = float(df8_stw.iloc[0:, 2])
                sd_valuestw = float(df8_stw.iloc[:, 3])
                x_valuestw = float(x_value_datastw.iloc[:, 2])
                difstw = mean_valuestw + sd_valuestw
                dif_coldstw = mean_valuestw - sd_valuestw

                if x_valuestw > difstw:
                    if z_valmw.empty == False:
                        list_hotstw[ttmhw] = float(z_valmw.iloc[0:, 3])
                if x_valuestw < dif_coldstw:
                    if z_valmw.empty == False:
                        list_coldstw[ttmhw] = float(z_valmw.iloc[0:, 3])
        # print(len(list_hotst))
        # print('and')
        # print(len(list_coldst))
        # print('#######')
        hot_sortw = sorted(list_hotw.items(), key=lambda kvw: (kvw[1], kvw[0]))  # this gives a list
        cold_sortw = sorted(list_coldw.items(), key=lambda kvyw: (kvyw[1], kvyw[0]))  # this gives a list
        hot_sortstw = sorted(list_hotstw.items(), key=lambda kvstw: (kvstw[1], kvstw[0]))  # this gives a list
        cold_sortstw = sorted(list_coldstw.items(), key=lambda kvystw: (kvystw[1], kvystw[0]))  # this gives a list
        # print(hot_sort[-1][0])
        if len(hot_sortw) > 4:
            the_ztw.writerow(
                [yymhw, 'neighborhood', 'hot', hot_sortw[-1][0], hot_sortw[-2][0], hot_sortw[-3][0], hot_sortw[-4][0],
                 hot_sortw[-5][0]])
        elif len(hot_sortw) == 4:
            the_ztw.writerow(
                [yymhw, 'neighborhood', 'hot', hot_sortw[-1][0], hot_sortw[-2][0], hot_sortw[-3][0], hot_sortw[-4][0]])
        elif len(hot_sortw) == 3:
            the_ztw.writerow([yymhw, 'neighborhood', 'hot', hot_sortw[-1][0], hot_sortw[-2][0], hot_sortw[-3][0]])
        elif len(hot_sortw) == 2:
            the_ztw.writerow([yymhw, 'neighborhood', 'hot', hot_sortw[-1][0], hot_sortw[-2][0]])
        elif len(hot_sortw) == 1:
            the_ztw.writerow([yymhw, 'neighborhood', 'hot', hot_sortw[-1][0]])
        else:
            the_ztw.writerow([yymhw, 'neighborhood', 'hot', 'NA'])

        if len(cold_sortw) > 4:
            the_ztw.writerow(
                [yymhw, 'neighborhood', 'cold', cold_sortw[0][0], cold_sortw[1][0], cold_sortw[2][0], cold_sortw[3][0],
                 cold_sortw[4][0]])
        elif len(cold_sortw) == 4:
            the_ztw.writerow(
                [yymhw, 'neighborhood', 'cold', cold_sortw[0][0], cold_sortw[1][0], cold_sortw[2][0], cold_sortw[3][0]])
        elif len(cold_sortw) == 3:
            the_ztw.writerow([yymhw, 'neighborhood', 'cold', cold_sortw[0][0], cold_sortw[1][0], cold_sortw[2][0]])
        elif len(cold_sortw) == 2:
            the_ztw.writerow([yymhw, 'neighborhood', 'cold', cold_sortw[0][0], cold_sortw[1][0]])
        elif len(cold_sortw) == 1:
            the_ztw.writerow([yymhw, 'neighborhood', 'cold', cold_sortw[0][0]])
        else:
            the_ztw.writerow([yymhw, 'neighborhood', 'cold', 'NA'])

        if len(hot_sortstw) > 4:
            the_ztw.writerow(
                [yymhw, 'state', 'hot', hot_sortstw[-1][0], hot_sortstw[-2][0], hot_sortstw[-3][0], hot_sortstw[-4][0],
                 hot_sortstw[-5][0]])
        elif len(hot_sortstw) == 4:
            the_ztw.writerow(
                [yymhw, 'state', 'hot', hot_sortstw[-1][0], hot_sortstw[-2][0], hot_sortstw[-3][0], hot_sortstw[-4][0]])
        elif len(hot_sortstw) == 3:
            the_ztw.writerow([yymhw, 'state', 'hot', hot_sortstw[-1][0], hot_sortstw[-2][0], hot_sortstw[-3][0]])
        elif len(hot_sortstw) == 2:
            the_ztw.writerow([yymhw, 'state', 'hot', hot_sortstw[-1][0], hot_sortstw[-2][0]])
        elif len(hot_sortstw) == 1:
            the_ztw.writerow([yymhw, 'state', 'hot', hot_sortstw[-1][0]])
        else:
            the_ztw.writerow([yymhw, 'state', 'hot', 'NA'])

        if len(cold_sortstw) > 4:
            the_ztw.writerow(
                [yymhw, 'state', 'cold', cold_sortstw[0][0], cold_sortstw[1][0], cold_sortstw[2][0], cold_sortstw[3][0],
                 cold_sortstw[4][0]])
        elif len(cold_sortstw) == 4:
            the_ztw.writerow([yymhw, 'state', 'cold', cold_sortstw[0][0], cold_sortstw[1][0], cold_sortstw[2][0],
                              cold_sortstw[3][0]])
        elif len(cold_sortstw) == 3:
            the_ztw.writerow([yymhw, 'state', 'cold', cold_sortstw[0][0], cold_sortstw[1][0], cold_sortstw[2][0]])
        elif len(cold_sortstw) == 2:
            the_ztw.writerow([yymhw, 'state', 'cold', cold_sortstw[0][0], cold_sortstw[1][0]])
        elif len(cold_sortstw) == 1:
            the_ztw.writerow([yymhw, 'state', 'cold', cold_sortstw[0][0]])
        else:
            the_ztw.writerow([yymhw, 'state', 'cold', 'NA'])

        # print(list_coldstw)

with open('top-month.csv', 'w', newline='') as zt:
    the_zt = csv.writer(zt)
    for yymh in range(1, 8):
        list_hot = {}
        list_cold = {}
        list_hot.clear()
        list_cold.clear()
        list_hotst = {}
        list_coldst = {}
        list_hotst.clear()
        list_coldst.clear()
        for ttmh in range(101, 820):
            mean_valuemh = 0
            sd_valuemh = 0
            df8_mh = q8_neighbormonth[((q8_neighbormonth.iloc[:, 0]) == ttmh) & ((q8_neighbormonth.iloc[:, 1]) == yymh)]
            x_value_datamh = q8_month[((q8_month.iloc[:, 0]) == ttmh) & ((q8_month.iloc[:, 1]) == yymh)]
            if df8_mh.empty == False and x_value_datamh.empty == False:
                mean_valuemh = float(df8_mh.iloc[0:, 2])
                sd_valuemh = float(df8_mh.iloc[:, 3])
                x_valuemh = float(x_value_datamh.iloc[:, 2])
                difmh = mean_valuemh + sd_valuemh
                difm_cold = mean_valuemh - sd_valuemh

                z_valm = q8_zmonth[((q8_zmonth.iloc[:, 0]) == ttmh) & ((q8_zmonth.iloc[:, 1]) == yymh)]

                if x_valuemh > difmh:
                    if z_valm.empty == False:
                        list_hot[ttmh] = float(z_valm.iloc[0:, 2])
                if x_valuemh < difm_cold:
                    if z_valm.empty == False:
                        list_cold[ttmh] = float(z_valm.iloc[0:, 2])
            mean_valuest = 0
            sd_valuest = 0
            df8_st = q8_statemonth[((q8_statemonth.iloc[:, 0]) == ttmh) & ((q8_statemonth.iloc[:, 1]) == yymh)]
            x_value_datast = q8_month[((q8_month.iloc[:, 0]) == ttmh) & ((q8_month.iloc[:, 1]) == yymh)]
            if df8_st.empty == False and x_value_datast.empty == False:
                mean_valuest = float(df8_st.iloc[0:, 2])
                sd_valuest = float(df8_st.iloc[:, 3])
                x_valuest = float(x_value_datast.iloc[:, 2])
                difst = mean_valuest + sd_valuest
                dif_coldst = mean_valuest - sd_valuest
                if x_valuest > difst:
                    list_hotst[ttmh] = float(z_valm.iloc[0:, 3])
                if x_valuest < dif_coldst:
                    list_coldst[ttmh] = float(z_valm.iloc[0:, 3])
        # print(len(list_hot))
        # print('and')
        # print(len(list_cold))
        # print('#######')
        hot_sort = sorted(list_hot.items(), key=lambda kv: (kv[1], kv[0]))  # this gives a list
        cold_sort = sorted(list_cold.items(), key=lambda kvy: (kvy[1], kvy[0]))  # this gives a list
        hot_sortst = sorted(list_hotst.items(), key=lambda kvst: (kvst[1], kvst[0]))  # this gives a list
        cold_sortst = sorted(list_coldst.items(), key=lambda kvyst: (kvyst[1], kvyst[0]))  # this gives a list
        # print(hot_sortst)
        if len(hot_sort) > 4:
            the_zt.writerow(
                [yymh, 'neighborhood', 'hot', hot_sort[-1][0], hot_sort[-2][0], hot_sort[-3][0], hot_sort[-4][0],
                 hot_sort[-5][0]])
        elif len(hot_sort) == 4:
            the_zt.writerow(
                [yymh, 'neighborhood', 'hot', hot_sort[-1][0], hot_sort[-2][0], hot_sort[-3][0], hot_sort[-4][0]])
        elif len(hot_sort) == 3:
            the_zt.writerow([yymh, 'neighborhood', 'hot', hot_sort[-1][0], hot_sort[-2][0], hot_sort[-3][0]])
        elif len(hot_sort) == 2:
            the_zt.writerow([yymh, 'neighborhood', 'hot', hot_sort[-1][0], hot_sort[-2][0]])
        elif len(hot_sort) == 1:
            the_zt.writerow([yymh, 'neighborhood', 'hot', hot_sort[-1][0]])
        else:
            the_zt.writerow([yymh, 'neighborhood', 'hot', 'NA'])

        if len(cold_sort) > 4:
            the_zt.writerow(
                [yymh, 'neighborhood', 'cold', cold_sort[0][0], cold_sort[1][0], cold_sort[2][0], cold_sort[3][0],
                 cold_sort[4][0]])
        elif len(cold_sort) == 4:
            the_zt.writerow(
                [yymh, 'neighborhood', 'cold', cold_sort[0][0], cold_sort[1][0], cold_sort[2][0], cold_sort[3][0]])
        elif len(cold_sort) == 3:
            the_zt.writerow([yymh, 'neighborhood', 'cold', cold_sort[0][0], cold_sort[1][0], cold_sort[2][0]])
        elif len(cold_sort) == 2:
            the_zt.writerow([yymh, 'neighborhood', 'cold', cold_sort[0][0], cold_sort[1][0]])
        elif len(cold_sort) == 1:
            the_zt.writerow([yymh, 'neighborhood', 'cold', cold_sort[0][0]])
        else:
            the_zt.writerow([yymh, 'neighborhood', 'cold', 'NA'])

        if len(hot_sortst) > 4:
            the_zt.writerow(
                [yymh, 'state', 'hot', hot_sortst[-1][0], hot_sortst[-2][0], hot_sortst[-3][0], hot_sortst[-4][0],
                 hot_sortst[-5][0]])
        elif len(hot_sortst) == 4:
            the_zt.writerow(
                [yymh, 'state', 'hot', hot_sortst[-1][0], hot_sortst[-2][0], hot_sortst[-3][0], hot_sortst[-4][0]])
        elif len(hot_sortst) == 3:
            the_zt.writerow([yymh, 'state', 'hot', hot_sortst[-1][0], hot_sortst[-2][0], hot_sortst[-3][0]])
        elif len(hot_sortst) == 2:
            the_zt.writerow([yymh, 'state', 'hot', hot_sortst[-1][0], hot_sortst[-2][0]])
        elif len(hot_sortst) == 1:
            the_zt.writerow([yymh, 'state', 'hot', hot_sortst[-1][0]])
        else:
            the_zt.writerow([yymh, 'state', 'hot', 'NA'])

        if len(cold_sortst) > 4:
            the_zt.writerow(
                [yymh, 'state', 'cold', cold_sortst[0][0], cold_sortst[1][0], cold_sortst[2][0], cold_sortst[3][0],
                 cold_sortst[4][0]])
        elif len(cold_sortst) == 4:
            the_zt.writerow(
                [yymh, 'state', 'cold', cold_sortst[0][0], cold_sortst[1][0], cold_sortst[2][0], cold_sortst[3][0]])
        elif len(cold_sortst) == 3:
            the_zt.writerow([yymh, 'state', 'cold', cold_sortst[0][0], cold_sortst[1][0], cold_sortst[2][0]])
        elif len(cold_sortst) == 2:
            the_zt.writerow([yymh, 'state', 'cold', cold_sortst[0][0], cold_sortst[1][0]])
        elif len(cold_sortst) == 1:
            the_zt.writerow([yymh, 'state', 'cold', cold_sortst[0][0]])
        else:
            the_zt.writerow([yymh, 'state', 'cold', 'NA'])

with open('top-overall.csv', 'w', newline='') as zt0:
    the_zt0 = csv.writer(zt0)
    for yymho in range(1, 2):
        list_hoto = {}
        list_coldo = {}
        list_hoto.clear()
        list_coldo.clear()
        list_hotsto = {}
        list_coldsto = {}
        list_hotsto.clear()
        list_coldsto.clear()
        for ttmho in range(101, 820):
            mean_valuemho = 0
            sd_valuemho = 0
            df8_mho = q8_neighboroverall[
                ((q8_neighboroverall.iloc[:, 0]) == ttmho) & ((q8_neighboroverall.iloc[:, 1]) == yymho)]
            x_value_datamho = q8_overall[((q8_overall.iloc[:, 0]) == ttmho) & ((q8_overall.iloc[:, 1]) == yymho)]
            if df8_mho.empty == False and x_value_datamho.empty == False:
                mean_valuemho = float(df8_mho.iloc[0:, 2])
                sd_valuemho = float(df8_mho.iloc[:, 3])
                x_valuemho = float(x_value_datamho.iloc[:, 2])
                difmho = mean_valuemho + sd_valuemho
                difm_coldo = mean_valuemho - sd_valuemho

                z_valm0 = q8_zoverall[((q8_zoverall.iloc[:, 0]) == ttmho) & ((q8_zoverall.iloc[:, 1]) == yymho)]

                if x_valuemho > difmho:
                    if z_valm0.empty == False:
                        list_hoto[ttmho] = float(z_valm0.iloc[:, 2])
                if x_valuemho < difm_coldo:
                    if z_valm0.empty == False:
                        list_coldo[ttmho] = float(z_valm0.iloc[:, 2])

            mean_valuesto = 0
            sd_valuesto = 0
            df8_sto = q8_stateoverall[((q8_stateoverall.iloc[:, 0]) == ttmho) & ((q8_stateoverall.iloc[:, 1]) == yymho)]
            x_value_datasto = q8_overall[((q8_overall.iloc[:, 0]) == ttmho) & ((q8_overall.iloc[:, 1]) == yymho)]
            if df8_sto.empty == False and x_value_datasto.empty == False:
                mean_valuesto = float(df8_sto.iloc[0:, 2])
                sd_valuesto = float(df8_sto.iloc[:, 3])
                x_valuesto = float(x_value_datasto.iloc[:, 2])
                difsto = mean_valuesto + sd_valuesto
                dif_coldsto = mean_valuesto - sd_valuesto
                if x_valuesto > difsto:
                    if z_valm0.empty == False:
                        list_hotsto[ttmho] = float(z_valm0.iloc[:, 3])
                if x_valuesto < dif_coldsto:
                    if z_valm0.empty == False:
                        list_coldsto[ttmho] = float(z_valm0.iloc[:, 3])
                        # print(len(list_hoto))
        # print('and')
        # print(len(list_coldo))
        # print('#######')
        hot_sorto = sorted(list_hoto.items(), key=lambda kvo: (kvo[1], kvo[0]))  # this gives a list
        cold_sorto = sorted(list_coldo.items(), key=lambda kvyo: (kvyo[1], kvyo[0]))  # this gives a list
        hot_sortsto = sorted(list_hotsto.items(), key=lambda kvsto: (kvsto[1], kvsto[0]))  # this gives a list
        cold_sortsto = sorted(list_coldsto.items(), key=lambda kvysto: (kvysto[1], kvysto[0]))  # this gives a list
        if len(hot_sorto) > 4:
            the_zt0.writerow(
                [yymho, 'neighborhood', 'hot', hot_sorto[-1][0], hot_sorto[-2][0], hot_sorto[-3][0], hot_sorto[-4][0],
                 hot_sorto[-5][0]])
        elif len(hot_sorto) == 4:
            the_zt0.writerow(
                [yymho, 'neighborhood', 'hot', hot_sorto[-1][0], hot_sorto[-2][0], hot_sorto[-3][0], hot_sorto[-4][0]])
        elif len(hot_sorto) == 3:
            the_zt0.writerow([yymho, 'neighborhood', 'hot', hot_sorto[-1][0], hot_sorto[-2][0], hot_sorto[-3][0]])
        elif len(hot_sorto) == 2:
            the_zt0.writerow([yymho, 'neighborhood', 'hot', hot_sorto[-1][0], hot_sorto[-2][0]])
        elif len(hot_sorto) == 1:
            the_zt0.writerow([yymho, 'neighborhood', 'hot', hot_sorto[-1][0]])
        else:
            the_zt0.writerow([yymho, 'neighborhood', 'hot', 'NA'])

        if len(cold_sorto) > 4:
            the_zt0.writerow(
                [yymho, 'neighborhood', 'cold', cold_sorto[0][0], cold_sorto[1][0], cold_sorto[2][0], cold_sorto[3][0],
                 cold_sorto[4][0]])
        elif len(cold_sorto) == 4:
            the_zt0.writerow(
                [yymho, 'neighborhood', 'cold', cold_sorto[0][0], cold_sorto[1][0], cold_sorto[2][0], cold_sorto[3][0]])
        elif len(cold_sorto) == 3:
            the_zt0.writerow([yymho, 'neighborhood', 'cold', cold_sorto[0][0], cold_sorto[1][0], cold_sorto[2][0]])
        elif len(cold_sorto) == 2:
            the_zt0.writerow([yymho, 'neighborhood', 'cold', cold_sorto[0][0], cold_sorto[1][0]])
        elif len(cold_sorto) == 1:
            the_zt0.writerow([yymho, 'neighborhood', 'cold', cold_sorto[0][0]])
        else:
            the_zt0.writerow([yymho, 'neighborhood', 'cold', 'NA'])

        if len(hot_sortsto) > 4:
            the_zt0.writerow(
                [yymho, 'state', 'hot', hot_sortsto[-1][0], hot_sortsto[-2][0], hot_sortsto[-3][0], hot_sortsto[-4][0],
                 hot_sortsto[-5][0]])
        elif len(hot_sortsto) == 4:
            the_zt0.writerow(
                [yymho, 'state', 'hot', hot_sortsto[-1][0], hot_sortsto[-2][0], hot_sortsto[-3][0], hot_sortsto[-4][0]])
        elif len(hot_sortsto) == 3:
            the_zt0.writerow([yymho, 'state', 'hot', hot_sortsto[-1][0], hot_sortsto[-2][0], hot_sortsto[-3][0]])
        elif len(hot_sortsto) == 2:
            the_zt0.writerow([yymho, 'state', 'hot', hot_sortsto[-1][0], hot_sortsto[-2][0]])
        elif len(hot_sortsto) == 1:
            the_zt0.writerow([yymho, 'state', 'hot', hot_sortsto[-1][0]])
        else:
            the_zt0.writerow([yymho, 'state', 'hot', 'NA'])

        if len(cold_sortsto) > 4:
            the_zt0.writerow(
                [yymho, 'state', 'cold', cold_sortsto[0][0], cold_sortsto[1][0], cold_sortsto[2][0], cold_sortsto[3][0],
                 cold_sortsto[4][0]])
        elif len(cold_sortsto) == 4:
            the_zt0.writerow([yymho, 'state', 'cold', cold_sortsto[0][0], cold_sortsto[1][0], cold_sortsto[2][0],
                              cold_sortsto[3][0]])
        elif len(cold_sortsto) == 3:
            the_zt0.writerow([yymho, 'state', 'cold', cold_sortsto[0][0], cold_sortsto[1][0], cold_sortsto[2][0]])
        elif len(cold_sortsto) == 2:
            the_zt0.writerow([yymho, 'state', 'cold', cold_sortsto[0][0], cold_sortsto[1][0]])
        elif len(cold_sortsto) == 1:
            the_zt0.writerow([yymho, 'state', 'cold', cold_sortsto[0][0]])
        else:
            the_zt0.writerow([yymho, 'state', 'cold', 'NA'])

