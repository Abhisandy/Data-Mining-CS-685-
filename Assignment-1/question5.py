import json
import requests
import csv
import pandas as pd
import numpy as np
#import import_ipynb
from question1 import modified_dist
from question1 import id_dist
from statistics import pstdev

dist_state = {}  # keys-district values-states

with open('json_data/raw_data1.json') as f:
    tx1 = json.load(f)
with open('json_data/raw_data2.json') as f2:
    tx2 = json.load(f2)
with open('json_data/raw_data3.json') as f3:
    tx3 = json.load(f3)
with open('json_data/raw_data4.json') as f4:
    tx4 = json.load(f4)
with open('json_data/raw_data5.json') as f5:
    tx5 = json.load(f5)
with open('json_data/raw_data6.json') as f6:
    tx6 = json.load(f6)
with open('json_data/raw_data7.json') as f7:
    tx7 = json.load(f7)
with open('json_data/raw_data8.json') as f8:
    tx8 = json.load(f8)
with open('json_data/raw_data9.json') as f9:
    tx9 = json.load(f9)
with open('json_data/raw_data10.json') as f10:
    tx10 = json.load(f10)
with open('json_data/raw_data11.json') as f11:
    tx11 = json.load(f11)
with open('json_data/raw_data12.json') as f12:
    tx12 = json.load(f12)
with open('json_data/raw_data13.json') as f13:
    tx13 = json.load(f13)
with open('json_data/raw_data14.json') as f14:
    tx14 = json.load(f14)

# req1 = requests.get('https://api.covid19india.org/raw_data1.json')
# tx1 = json.loads(req1.text)
# tx['raw_data'][0]['detecteddistrict']
# len_raw1 = len(tx1['raw_data'])

for aw1 in tx1['raw_data']:
    # for ar1 in modified_dist:
    #    if aw1['detecteddistrict'].lower() == ar1 :
    dist_state[id_dist.get(aw1['detecteddistrict'].lower())] = aw1['detectedstate'].lower()

# req2 = requests.get('https://api.covid19india.org/raw_data2.json')
# tx2 = json.loads(req2.text)
for aw2 in tx2['raw_data']:
    # for ar2 in modified_dist:
    #   if aw2['detecteddistrict'].lower() == ar2 :
    dist_state[id_dist.get(aw2['detecteddistrict'].lower())] = aw2['detectedstate'].lower()

# req3 = requests.get('https://api.covid19india.org/raw_data3.json')
# tx3 = json.loads(req3.text)
for aw3 in tx3['raw_data']:
    # for ar3 in modified_dist:
    #    if aw3['detecteddistrict'].lower() == ar3 :
    dist_state[id_dist.get(aw3['detecteddistrict'].lower())] = aw3['detectedstate'].lower()

# req4 = requests.get('https://api.covid19india.org/raw_data4.json')
# tx4 = json.loads(req4.text)
for aw4 in tx4['raw_data']:
    # for ar4 in modified_dist:
    #    if aw4['detecteddistrict'].lower() == ar4 :
    dist_state[id_dist.get(aw4['detecteddistrict'].lower())] = aw4['detectedstate'].lower()
# req5 = requests.get('https://api.covid19india.org/raw_data5.json')
# tx5 = json.loads(req5.text)
for aw5 in tx5['raw_data']:
    # for ar5 in modified_dist:
    #    if aw5['detecteddistrict'].lower() == ar5 :
    dist_state[id_dist.get(aw5['detecteddistrict'].lower())] = aw5['detectedstate'].lower()
# req6 = requests.get('https://api.covid19india.org/raw_data6.json')
# tx6 = json.loads(req6.text)
for aw6 in tx6['raw_data']:
    # for ar6 in modified_dist:
    #    if aw6['detecteddistrict'].lower() == ar6 :
    dist_state[id_dist.get(aw6['detecteddistrict'].lower())] = aw6['detectedstate'].lower()
# req7 = requests.get('https://api.covid19india.org/raw_data7.json')
# tx7 = json.loads(req7.text)
for aw7 in tx7['raw_data']:
    for ar7 in modified_dist:
        if aw7['detecteddistrict'].lower() == ar7:
            dist_state[id_dist.get(aw7['detecteddistrict'].lower())] = aw7['detectedstate'].lower()
# req8 = requests.get('https://api.covid19india.org/raw_data8.json')
# tx8 = json.loads(req8.text)
for aw8 in tx8['raw_data']:
    # for ar8 in modified_dist:
    #    if aw8['detecteddistrict'].lower() == ar8 :
    dist_state[id_dist.get(aw8['detecteddistrict'].lower())] = aw8['detectedstate'].lower()
# req9 = requests.get('https://api.covid19india.org/raw_data9.json')
# tx9 = json.loads(req9.text)
for aw9 in tx9['raw_data']:
    # for ar9 in modified_dist:
    #    if aw9['detecteddistrict'].lower() == ar9 :
    dist_state[id_dist.get(aw9['detecteddistrict'].lower())] = aw9['detectedstate'].lower()
# req10 = requests.get('https://api.covid19india.org/raw_data10.json')
# tx10 = json.loads(req10.text)
for aw10 in tx10['raw_data']:
    # for ar10 in modified_dist:
    #    if aw10['detecteddistrict'].lower() == ar10 :
    dist_state[id_dist.get(aw10['detecteddistrict'].lower())] = aw10['detectedstate'].lower()
# req11 = requests.get('https://api.covid19india.org/raw_data11.json')
# tx11 = json.loads(req11.text)
for aw11 in tx11['raw_data']:
    # for ar11 in modified_dist:
    #    if aw11['detecteddistrict'].lower() == ar11 :
    dist_state[id_dist.get(aw11['detecteddistrict'].lower())] = aw11['detectedstate'].lower()
# req12 = requests.get('https://api.covid19india.org/raw_data12.json')
# tx12 = json.loads(req12.text)
for aw12 in tx12['raw_data']:
    # for ar12 in modified_dist:
    #    if aw12['detecteddistrict'].lower() == ar12 :
    dist_state[id_dist.get(aw12['detecteddistrict'].lower())] = aw12['detectedstate'].lower()
# req13 = requests.get('https://api.covid19india.org/raw_data13.json')
# tx13 = json.loads(req13.text)
for aw13 in tx13['raw_data']:
    # for ar13 in modified_dist:
    #    if aw13['detecteddistrict'].lower() == ar13 :
    dist_state[id_dist.get(aw13['detecteddistrict'].lower())] = aw13['detectedstate'].lower()
# req14 = requests.get('https://api.covid19india.org/raw_data14.json')
# tx14 = json.loads(req14.text)
for aw14 in tx14['raw_data']:
    # for ar14 in modified_dist:
    #    if aw14['detecteddistrict'].lower() == ar14 :
    dist_state[id_dist.get(aw14['detecteddistrict'].lower())] = aw14['detectedstate'].lower()
# print(dist_state)
flipped = {}  # key-state ,value-list of ids of its district

for key, value in dist_state.items():
    if value not in flipped:
        flipped[value] = [key]
    else:
        flipped[value].append(key)
        # print(flipped)

csv_wk = pd.read_csv('Cases-week.csv')
df_id = []
df_time = []
df_mean = []
df_sd = []

for dd in range(1, 26):

    for gg in flipped:
        sdw_list = []
        sumw = 0
        mw = 0
        sdw = 0
        lenw = len(flipped[gg]) - 1
        # print(gg)
        for ss in flipped[gg]:
            wk = csv_wk.loc[(csv_wk.iloc[:, 0] == ss) & (csv_wk.iloc[:, 1] == dd)]
            if (wk.empty == False):
                sumw = sumw + int(wk.iloc[0:, 2])
                sdw_list.append(int(wk.iloc[0:, 2]))

        # print(sdw_list)
        for hh in flipped[gg]:
            meann = 0
            sdn = 0
            sumn = 0
            sdwm_list = []
            wkn = csv_wk.loc[(csv_wk.iloc[:, 0] == hh) & (csv_wk.iloc[:, 1] == dd)]
            if (wkn.empty == False):
                sumn = sumw - int(wkn.iloc[0:, 2])
                sdwn_list = sdw_list.copy()
                sdwn_list.remove(int(wkn.iloc[0:, 2]))
            if lenw != 0:
                meann = "{:.2f}".format(sumn / lenw)
            else:
                meann = 0
            if (len(sdwn_list) >= 2):
                sdn = "{:.2f}".format(pstdev(sdwn_list))
            else:
                sdn = 0
            # print(hh)
            # print(sdwn_list)
            sdwn_list.clear()
            df_id.append(hh)
            df_time.append(dd)
            df_mean.append(meann)
            df_sd.append(sdn)
            # print(hh,dd,meann,sdn)
            # the_writersn.writerow([hh, dd, meann, sdn])

df_weekly = pd.DataFrame(list(zip(df_id, df_time, df_mean, df_sd)), columns=['id', 'time-id', 'mean', 'sd'])
df_weekly = df_weekly.sort_values(['id', 'time-id'], ascending=[True, True])
df_weekly = df_weekly.dropna()
df_weekly.to_csv('state-week.csv', index=False)

csv_wkm = pd.read_csv('Cases-Month.csv')
df_idm = []
df_timem = []
df_meanm = []
df_sdm = []

for ddm in range(1, 8):

    for ggm in flipped:
        sdw_listm = []
        sumwm = 0
        mwm = 0
        sdwm = 0
        lenwm = len(flipped[ggm]) - 1
        # print(ggm)
        for ssm in flipped[ggm]:
            wkm = csv_wkm.loc[(csv_wkm.iloc[:, 0] == ssm) & (csv_wkm.iloc[:, 1] == ddm)]
            if (wkm.empty == False):
                sumwm = sumwm + int(wkm.iloc[0:, 2])
                sdw_listm.append(int(wkm.iloc[0:, 2]))
        # print(sdw_listm)
        for hhm in flipped[ggm]:
            meannm = 0
            sdnm = 0
            sumnm = 0
            sdwn_listm = []
            wknm = csv_wkm.loc[(csv_wkm.iloc[:, 0] == hhm) & (csv_wkm.iloc[:, 1] == ddm)]
            if (wknm.empty == False):
                sumnm = sumwm - int(wknm.iloc[0:, 2])
                sdwn_listm = sdw_listm.copy()
                sdwn_listm.remove(int(wknm.iloc[0:, 2]))
            if lenwm != 0:
                meannm = "{:.2f}".format(sumnm / lenwm)
            else:
                meannm = 0
            if (len(sdwn_listm) >= 2):
                sdnm = "{:.2f}".format(pstdev(sdwn_listm))
            else:
                sdnm = 0
            sdwn_listm.clear()
            df_idm.append(hhm)
            df_timem.append(ddm)
            df_meanm.append(meannm)
            df_sdm.append(sdnm)
            # print(hh,dd,meann,sdn)
            # the_writersn.writerow([hh, dd, meann, sdn])

df_monthly = pd.DataFrame(list(zip(df_idm, df_timem, df_meanm, df_sdm)), columns=['id', 'time-id', 'mean', 'sd'])
df_monthly = df_monthly.sort_values(['id', 'time-id'], ascending=[True, True])
df_monthly = df_monthly.dropna()
df_monthly.to_csv('state-month.csv', index=False)

csv_wko = pd.read_csv('cases-overall.csv')
df_ido = []
df_timeo = []
df_meano = []
df_sdo = []

for ddo in range(1, 2):

    for ggo in flipped:
        sdw_listo = []
        sumwo = 0
        mwo = 0
        sdwo = 0
        lenwo = len(flipped[ggo]) - 1
        # print(ggo)
        for sso in flipped[ggo]:
            wko = csv_wko.loc[(csv_wko.iloc[:, 0] == sso) & (csv_wko.iloc[:, 1] == ddo)]
            if (wko.empty == False):
                sumwo = sumwo + int(wko.iloc[0:, 2])
                sdw_listo.append(int(wko.iloc[0:, 2]))
        # print(sdw_listo)
        for hho in flipped[ggo]:
            meanno = 0
            sdno = 0
            sumno = 0
            sdwm_listo = []
            wkno = csv_wko.loc[(csv_wko.iloc[:, 0] == hho) & (csv_wko.iloc[:, 1] == ddo)]
            if (wkno.empty == False):
                sumno = sumwo - int(wkno.iloc[0:, 2])
                sdwn_listo = sdw_listo.copy()
                sdwn_listo.remove(int(wkno.iloc[0:, 2]))
            if lenwo != 0:
                meanno = "{:.2f}".format(sumno / lenwo)
            else:
                meanno = 0
            if (len(sdwn_listo) >= 2):
                sdno = "{:.2f}".format(pstdev(sdwn_listo))
            else:
                sdno = 0
            sdwn_listo.clear()
            df_ido.append(hho)
            df_timeo.append(ddo)
            df_meano.append(meanno)
            df_sdo.append(sdno)
            # print(hh,dd,meann,sdn)
            # the_writersn.writerow([hh, dd, meann, sdn])

df_overall = pd.DataFrame(list(zip(df_ido, df_timeo, df_meano, df_sdo)), columns=['id', 'time-id', 'mean', 'sd'])
df_overall = df_overall.sort_values(['id', 'time-id'], ascending=[True, True])
df_overall = df_overall.dropna()
df_overall.to_csv('state-overall.csv', index=False)