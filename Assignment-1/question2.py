import json
import requests
import csv
import pandas as pd
import numpy as np
from question1 import modified_dist
from question1 import id_dist
pd.set_option('display.max_rows', None)
dis_csv1 = pd.read_csv('json_data/raw_data1.csv')
dis_csv2 = pd.read_csv('json_data/raw_data2.csv')
dis_csv3 = pd.read_csv('json_data/raw_data3.csv')
dis_csv4 = pd.read_csv('json_data/raw_data4.csv')
dis_csv5 = pd.read_csv('json_data/raw_data5.csv')
dis_csv6 = pd.read_csv('json_data/raw_data6.csv')
dis_csv7 = pd.read_csv('json_data/raw_data7.csv')
dis_csv8 = pd.read_csv('json_data/raw_data8.csv')
dis_csv9 = pd.read_csv('json_data/raw_data9.csv')
dis_csv10 = pd.read_csv('json_data/raw_data10.csv')
dis_csv11 = pd.read_csv('json_data/raw_data11.csv')
dis_csv12 = pd.read_csv('json_data/raw_data12.csv')
dis_csv13 = pd.read_csv('json_data/raw_data13.csv')
dis_csv14 = pd.read_csv('json_data/raw_data14.csv')
#print(len(modified_dist))
#print(modified_dist)

list_id_modified_dist = []
for al in modified_dist:
    list_id_modified_dist.append(id_dist.get(al))

conc = [dis_csv1, dis_csv2]
dis_csv = pd.concat(conc)
csv_district = []
csv_Date = []

for dfc in dis_csv['Detected District']:
    dfc = str(dfc).lower()
    csv_district.append(dfc)
for dfc2 in dis_csv['Date Announced']:
    csv_Date.append(dfc2)
# print(csv_district, csv_Date)

d_csv = pd.DataFrame({'District': csv_district, 'Date': csv_Date})
d_csv['Date'] = pd.to_datetime(d_csv['Date'], format='%d/%m/%Y')

w1_data = d_csv[(d_csv['Date'] >= '2020/03/15') & (d_csv['Date'] <= '2020/03/21')]
n = len(modified_dist)
value1 = [0] * n
v1 = 0
for w1 in modified_dist:
    for wq1 in w1_data['District']:
        if w1 == wq1:
            value1[v1] += 1
    v1 = v1 + 1
w1_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value1})
w1_csv.insert(1, 'WeekId', 1)

w2_data = d_csv[(d_csv['Date'] >= '2020/03/22') & (d_csv['Date'] <= '2020/03/28')]
value2 = [0] * n
v2 = 0
for w2 in modified_dist:
    for wq2 in w2_data['District']:
        if w2 == wq2:
            value2[v2] += 1
    v2 = v2 + 1
w2_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value2})
w2_csv.insert(1, 'WeekId', 2)

w3_data = d_csv[(d_csv['Date'] >= '2020/03/29') & (d_csv['Date'] <= '2020/04/04')]
value3 = [0] * n
v3 = 0
for w3 in modified_dist:
    for wq3 in w3_data['District']:
        if w3 == wq3:
            value3[v3] += 1
    v3 = v3 + 1
w3_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value3})
w3_csv.insert(1, 'WeekId', 3)

w4_data = d_csv[(d_csv['Date'] >= '2020/04/05') & (d_csv['Date'] <= '2020/04/11')]
value4 = [0] * n
v4 = 0
for w4 in modified_dist:
    for wq4 in w4_data['District']:
        if w4 == wq4:
            value4[v4] += 1
    v4 = v4 + 1
w4_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value4})
w4_csv.insert(1, 'WeekId', 4)

w5_data = d_csv[(d_csv['Date'] >= '2020/04/12') & (d_csv['Date'] <= '2020/04/18')]
value5 = [0] * n
v5 = 0
for w5 in modified_dist:
    for wq5 in w5_data['District']:
        if w5 == wq5:
            value5[v5] += 1
    v5 = v5 + 1
w5_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value5})
w5_csv.insert(1, 'WeekId', 5)

w6_data = d_csv[(d_csv['Date'] >= '2020/04/19') & (d_csv['Date'] <= '2020/04/25')]
value6 = [0] * n
v6 = 0
for w6 in modified_dist:
    for wq6 in w6_data['District']:
        if w6 == wq6:
            value6[v6] += 1
    v6 = v6 + 1
w6_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value6})
w6_csv.insert(1, 'WeekId', 6)

# 26th april
w6_ap = d_csv[(d_csv['Date'] == '2020/04/26')]
value_ap = [0] * n
v_ap = 0
for apr in modified_dist:
    for apr1 in w6_ap['District']:
        if apr == apr1:
            value_ap[v_ap] += 1
    v_ap = v_ap + 1

con1 = [dis_csv3, dis_csv4, dis_csv5, dis_csv6, dis_csv7, dis_csv8, dis_csv9, dis_csv10, dis_csv11, dis_csv12,
        dis_csv13, dis_csv14]
dis_csv1 = pd.concat(con1)
d_csv7 = dis_csv1.loc[:, ['Date Announced', 'Detected District', 'Num Cases']]
d_csv7 = d_csv7.dropna()
d_csv7['Date Announced'] = pd.to_datetime(d_csv7['Date Announced'], format='%d/%m/%Y')

w7_data = d_csv7[(d_csv7['Date Announced'] >= '2020/04/27') & (d_csv7['Date Announced'] <= '2020/05/02')]
value7 = [0] * n

for iq7, w7 in w7_data.iterrows():
    if (w7['Detected District'].lower() != 'hnahthial') & (w7['Detected District'].lower() != 'nan') & (
            w7['Detected District'].lower() != 'north and middle andaman') & (
            w7['Detected District'].lower() != 'italians') & (w7['Detected District'].lower() != 'capf personnel') & (
            w7['Detected District'].lower() != 'unknown') & (w7['Detected District'].lower() != 'yanam') & (
            w7['Detected District'].lower() != 'budgam') & (w7['Detected District'].lower() != 'chengalpattu') & (
            w7['Detected District'].lower() != 'evacuees') & (w7['Detected District'].lower() != 'morigaon') & (
            w7['Detected District'].lower() != 'other state') & (w7['Detected District'].lower() != 'ranipet') & (
            w7['Detected District'].lower() != 'south andaman') & (w7['Detected District'].lower() != 'tenkasi') & (
            w7['Detected District'].lower() != 'tirupathur') & (w7['Detected District'].lower() != 'unassigned') & (
            w7['Detected District'].lower() != 'airport quarantine') & (
            w7['Detected District'].lower() != 'bsf camp') & (w7['Detected District'].lower() != 'cooch behar') & (
            w7['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w7['Detected District'].lower() != 'foreign evacuees') & (
            w7['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w7['Detected District'].lower() != 'karbi anglong') & (w7['Detected District'].lower() != 'khawzawl') & (
            w7['Detected District'].lower() != 'lakhimpur') & (w7['Detected District'].lower() != 'other region') & (
            w7['Detected District'].lower() != 'railway quarantine') & (
            w7['Detected District'].lower() != 'saitual') & (w7['Detected District'].lower() != 'others'):
        if (w7['Num Cases'] > 0):
            value7[id_dist.get((w7['Detected District'].lower())) - 101] += w7['Num Cases']

value7_f = list(np.array(value7) + np.array(value_ap))

w7_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value7_f})
w7_csv.insert(1, 'WeekId', 7)

w8_data = d_csv7[(d_csv7['Date Announced'] >= '2020/05/03') & (d_csv7['Date Announced'] <= '2020/05/09')]
value8 = [0] * n
for iq8, w8 in w8_data.iterrows():
    if (w8['Detected District'].lower() != 'budgam') & (w8['Detected District'].lower() != 'chengalpattu') & (
            w8['Detected District'].lower() != 'evacuees') & (w8['Detected District'].lower() != 'morigaon') & (
            w8['Detected District'].lower() != 'other state') & (w8['Detected District'].lower() != 'ranipet') & (
            w8['Detected District'].lower() != 'south andaman') & (w8['Detected District'].lower() != 'tenkasi') & (
            w8['Detected District'].lower() != 'tirupathur') & (w8['Detected District'].lower() != 'unassigned') & (
            w8['Detected District'].lower() != 'airport quarantine') & (
            w8['Detected District'].lower() != 'bsf camp') & (w8['Detected District'].lower() != 'cooch behar') & (
            w8['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w8['Detected District'].lower() != 'foreign evacuees') & (
            w8['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w8['Detected District'].lower() != 'karbi anglong') & (w8['Detected District'].lower() != 'khawzawl') & (
            w8['Detected District'].lower() != 'lakhimpur kheri') & (
            w8['Detected District'].lower() != 'other region') & (
            w8['Detected District'].lower() != 'railway quarantine') & (
            w8['Detected District'].lower() != 'saitual') & (w8['Detected District'].lower() != 'others'):
        if (w8['Num Cases'] > 0):
            value8[id_dist.get((w8['Detected District'].lower())) - 101] += w8['Num Cases']
w8_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value8})
w8_csv.insert(1, 'WeekId', 8)
w9_data = d_csv7[(d_csv7['Date Announced'] >= '2020/05/10') & (d_csv7['Date Announced'] <= '2020/05/16')]
value9 = [0] * n
for iq9, w9 in w9_data.iterrows():
    if (w9['Detected District'].lower() != 'budgam') & (w9['Detected District'].lower() != 'chengalpattu') & (
            w9['Detected District'].lower() != 'evacuees') & (w9['Detected District'].lower() != 'morigaon') & (
            w9['Detected District'].lower() != 'other state') & (w9['Detected District'].lower() != 'ranipet') & (
            w9['Detected District'].lower() != 'south andaman') & (w9['Detected District'].lower() != 'tenkasi') & (
            w9['Detected District'].lower() != 'tirupathur') & (w9['Detected District'].lower() != 'unassigned') & (
            w9['Detected District'].lower() != 'airport quarantine') & (
            w9['Detected District'].lower() != 'bsf camp') & (w9['Detected District'].lower() != 'cooch behar') & (
            w9['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w9['Detected District'].lower() != 'foreign evacuees') & (
            w9['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w9['Detected District'].lower() != 'karbi anglong') & (w9['Detected District'].lower() != 'khawzawl') & (
            w9['Detected District'].lower() != 'lakhimpur kheri') & (
            w9['Detected District'].lower() != 'other region') & (
            w9['Detected District'].lower() != 'railway quarantine') & (
            w9['Detected District'].lower() != 'saitual') & (w9['Detected District'].lower() != 'others'):
        if (w9['Num Cases'] > 0):
            value9[id_dist.get((w9['Detected District'].lower())) - 101] += w9['Num Cases']
w9_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value9})
w9_csv.insert(1, 'WeekId', 9)

w10_data = d_csv7[(d_csv7['Date Announced'] >= '2020/05/17') & (d_csv7['Date Announced'] <= '2020/05/23')]
value10 = [0] * n
for iq10, w10 in w10_data.iterrows():
    if (w10['Detected District'].lower() != 'budgam') & (w10['Detected District'].lower() != 'chengalpattu') & (
            w10['Detected District'].lower() != 'evacuees') & (w10['Detected District'].lower() != 'morigaon') & (
            w10['Detected District'].lower() != 'other state') & (w10['Detected District'].lower() != 'ranipet') & (
            w10['Detected District'].lower() != 'south andaman') & (w10['Detected District'].lower() != 'tenkasi') & (
            w10['Detected District'].lower() != 'tirupathur') & (w10['Detected District'].lower() != 'unassigned') & (
            w10['Detected District'].lower() != 'airport quarantine') & (
            w10['Detected District'].lower() != 'bsf camp') & (w10['Detected District'].lower() != 'cooch behar') & (
            w10['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w10['Detected District'].lower() != 'foreign evacuees') & (
            w10['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w10['Detected District'].lower() != 'karbi anglong') & (w10['Detected District'].lower() != 'khawzawl') & (
            w10['Detected District'].lower() != 'lakhimpur') & (w10['Detected District'].lower() != 'other region') & (
            w10['Detected District'].lower() != 'railway quarantine') & (
            w10['Detected District'].lower() != 'saitual') & (w10['Detected District'].lower() != 'others'):
        if (w10['Num Cases'] > 0):
            value10[id_dist.get((w10['Detected District'].lower())) - 101] += w10['Num Cases']
w10_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value10})
w10_csv.insert(1, 'WeekId', 10)

w11_data = d_csv7[(d_csv7['Date Announced'] >= '2020/05/24') & (d_csv7['Date Announced'] <= '2020/05/30')]
value11 = [0] * n
for iq11, w11 in w11_data.iterrows():
    if (w11['Detected District'].lower() != 'budgam') & (w11['Detected District'].lower() != 'chengalpattu') & (
            w11['Detected District'].lower() != 'evacuees') & (w11['Detected District'].lower() != 'morigaon') & (
            w11['Detected District'].lower() != 'other state') & (w11['Detected District'].lower() != 'ranipet') & (
            w11['Detected District'].lower() != 'south andaman') & (w11['Detected District'].lower() != 'tenkasi') & (
            w11['Detected District'].lower() != 'tirupathur') & (w11['Detected District'].lower() != 'unassigned') & (
            w11['Detected District'].lower() != 'airport quarantine') & (
            w11['Detected District'].lower() != 'bsf camp') & (w11['Detected District'].lower() != 'cooch behar') & (
            w11['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w11['Detected District'].lower() != 'foreign evacuees') & (
            w11['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w11['Detected District'].lower() != 'karbi anglong') & (w11['Detected District'].lower() != 'khawzawl') & (
            w11['Detected District'].lower() != 'lakhimpur') & (w11['Detected District'].lower() != 'other region') & (
            w11['Detected District'].lower() != 'railway quarantine') & (
            w11['Detected District'].lower() != 'saitual') & (w11['Detected District'].lower() != 'others'):
        if (w11['Num Cases'] > 0):
            value11[id_dist.get((w11['Detected District'].lower())) - 101] += w11['Num Cases']
w11_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value11})
w11_csv.insert(1, 'WeekId', 11)

w12_data = d_csv7[(d_csv7['Date Announced'] >= '2020/05/31') & (d_csv7['Date Announced'] <= '2020/06/06')]
value12 = [0] * n
for iq12, w12 in w12_data.iterrows():
    if (w12['Detected District'].lower() != 'budgam') & (w12['Detected District'].lower() != 'chengalpattu') & (
            w12['Detected District'].lower() != 'evacuees') & (w12['Detected District'].lower() != 'morigaon') & (
            w12['Detected District'].lower() != 'other state') & (w12['Detected District'].lower() != 'ranipet') & (
            w12['Detected District'].lower() != 'south andaman') & (w12['Detected District'].lower() != 'tenkasi') & (
            w12['Detected District'].lower() != 'tirupathur') & (w12['Detected District'].lower() != 'unassigned') & (
            w12['Detected District'].lower() != 'airport quarantine') & (
            w12['Detected District'].lower() != 'bsf camp') & (w12['Detected District'].lower() != 'cooch behar') & (
            w12['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w12['Detected District'].lower() != 'foreign evacuees') & (
            w12['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w12['Detected District'].lower() != 'karbi anglong') & (w12['Detected District'].lower() != 'khawzawl') & (
            w12['Detected District'].lower() != 'lakhimpur') & (w12['Detected District'].lower() != 'other region') & (
            w12['Detected District'].lower() != 'railway quarantine') & (
            w12['Detected District'].lower() != 'saitual') & (w12['Detected District'].lower() != 'others'):
        if (w12['Num Cases'] > 0):
            value12[id_dist.get((w12['Detected District'].lower())) - 101] += w12['Num Cases']
w12_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value12})
w12_csv.insert(1, 'WeekId', 12)

w13_data = d_csv7[(d_csv7['Date Announced'] >= '2020/06/07') & (d_csv7['Date Announced'] <= '2020/06/13')]
value13 = [0] * n
for iq13, w13 in w13_data.iterrows():
    if (w13['Detected District'].lower() != 'budgam') & (w13['Detected District'].lower() != 'chengalpattu') & (
            w13['Detected District'].lower() != 'evacuees') & (w13['Detected District'].lower() != 'morigaon') & (
            w13['Detected District'].lower() != 'other state') & (w13['Detected District'].lower() != 'ranipet') & (
            w13['Detected District'].lower() != 'south andaman') & (w13['Detected District'].lower() != 'tenkasi') & (
            w13['Detected District'].lower() != 'tirupathur') & (w13['Detected District'].lower() != 'unassigned') & (
            w13['Detected District'].lower() != 'airport quarantine') & (
            w13['Detected District'].lower() != 'bsf camp') & (w13['Detected District'].lower() != 'cooch behar') & (
            w13['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w13['Detected District'].lower() != 'foreign evacuees') & (
            w13['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w13['Detected District'].lower() != 'karbi anglong') & (w13['Detected District'].lower() != 'khawzawl') & (
            w13['Detected District'].lower() != 'lakhimpur') & (w13['Detected District'].lower() != 'other region') & (
            w13['Detected District'].lower() != 'railway quarantine') & (
            w13['Detected District'].lower() != 'saitual') & (w13['Detected District'].lower() != 'others'):
        if (w13['Num Cases'] > 0):
            value13[id_dist.get((w13['Detected District'].lower())) - 101] += w13['Num Cases']
w13_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value13})
w13_csv.insert(1, 'WeekId', 13)

w14_data = d_csv7[(d_csv7['Date Announced'] >= '2020/06/14') & (d_csv7['Date Announced'] <= '2020/06/20')]
value14 = [0] * n
for iq14, w14 in w14_data.iterrows():
    if (w14['Detected District'].lower() != 'budgam') & (w14['Detected District'].lower() != 'chengalpattu') & (
            w14['Detected District'].lower() != 'evacuees') & (w14['Detected District'].lower() != 'morigaon') & (
            w14['Detected District'].lower() != 'other state') & (w14['Detected District'].lower() != 'ranipet') & (
            w14['Detected District'].lower() != 'south andaman') & (w14['Detected District'].lower() != 'tenkasi') & (
            w14['Detected District'].lower() != 'tirupathur') & (w14['Detected District'].lower() != 'unassigned') & (
            w14['Detected District'].lower() != 'airport quarantine') & (
            w14['Detected District'].lower() != 'bsf camp') & (w14['Detected District'].lower() != 'cooch behar') & (
            w14['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w14['Detected District'].lower() != 'foreign evacuees') & (
            w14['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w14['Detected District'].lower() != 'karbi anglong') & (w14['Detected District'].lower() != 'khawzawl') & (
            w14['Detected District'].lower() != 'lakhimpur') & (w14['Detected District'].lower() != 'other region') & (
            w14['Detected District'].lower() != 'railway quarantine') & (
            w14['Detected District'].lower() != 'saitual') & (w14['Detected District'].lower() != 'others'):
        if (w14['Num Cases'] > 0):
            value14[id_dist.get((w14['Detected District'].lower())) - 101] += w14['Num Cases']
w14_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value14})
w14_csv.insert(1, 'WeekId', 14)

w15_data = d_csv7[(d_csv7['Date Announced'] >= '2020/06/21') & (d_csv7['Date Announced'] <= '2020/06/27')]
value15 = [0] * n
for iq15, w15 in w15_data.iterrows():
    if (w15['Detected District'].lower() != 'unknown') & (w15['Detected District'].lower() != 'yanam') & (
            w15['Detected District'].lower() != 'budgam') & (w15['Detected District'].lower() != 'chengalpattu') & (
            w15['Detected District'].lower() != 'evacuees') & (w15['Detected District'].lower() != 'morigaon') & (
            w15['Detected District'].lower() != 'other state') & (w15['Detected District'].lower() != 'ranipet') & (
            w15['Detected District'].lower() != 'south andaman') & (w15['Detected District'].lower() != 'tenkasi') & (
            w15['Detected District'].lower() != 'tirupathur') & (w15['Detected District'].lower() != 'unassigned') & (
            w15['Detected District'].lower() != 'airport quarantine') & (
            w15['Detected District'].lower() != 'bsf camp') & (w15['Detected District'].lower() != 'cooch behar') & (
            w15['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w15['Detected District'].lower() != 'foreign evacuees') & (
            w15['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w15['Detected District'].lower() != 'karbi anglong') & (w15['Detected District'].lower() != 'khawzawl') & (
            w15['Detected District'].lower() != 'lakhimpur') & (w15['Detected District'].lower() != 'other region') & (
            w15['Detected District'].lower() != 'railway quarantine') & (
            w15['Detected District'].lower() != 'saitual') & (w15['Detected District'].lower() != 'others'):
        if (w15['Num Cases'] > 0):
            value15[id_dist.get((w15['Detected District'].lower())) - 101] += w15['Num Cases']
w15_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value15})
w15_csv.insert(1, 'WeekId', 15)

w16_data = d_csv7[(d_csv7['Date Announced'] >= '2020/06/28') & (d_csv7['Date Announced'] <= '2020/07/04')]
value16 = [0] * n
for iq16, w16 in w16_data.iterrows():
    if (w16['Detected District'].lower() != 'unknown') & (w16['Detected District'].lower() != 'yanam') & (
            w16['Detected District'].lower() != 'budgam') & (w16['Detected District'].lower() != 'chengalpattu') & (
            w16['Detected District'].lower() != 'evacuees') & (w16['Detected District'].lower() != 'morigaon') & (
            w16['Detected District'].lower() != 'other state') & (w16['Detected District'].lower() != 'ranipet') & (
            w16['Detected District'].lower() != 'south andaman') & (w16['Detected District'].lower() != 'tenkasi') & (
            w16['Detected District'].lower() != 'tirupathur') & (w16['Detected District'].lower() != 'unassigned') & (
            w16['Detected District'].lower() != 'airport quarantine') & (
            w16['Detected District'].lower() != 'bsf camp') & (w16['Detected District'].lower() != 'cooch behar') & (
            w16['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w16['Detected District'].lower() != 'foreign evacuees') & (
            w16['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w16['Detected District'].lower() != 'karbi anglong') & (w16['Detected District'].lower() != 'khawzawl') & (
            w16['Detected District'].lower() != 'lakhimpur') & (w16['Detected District'].lower() != 'other region') & (
            w16['Detected District'].lower() != 'railway quarantine') & (
            w16['Detected District'].lower() != 'saitual') & (w16['Detected District'].lower() != 'others'):
        if (w16['Num Cases'] > 0):
            value16[id_dist.get((w16['Detected District'].lower())) - 101] += w16['Num Cases']
w16_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value16})
w16_csv.insert(1, 'WeekId', 16)

w17_data = d_csv7[(d_csv7['Date Announced'] >= '2020/07/05') & (d_csv7['Date Announced'] <= '2020/07/11')]
value17 = [0] * n
for iq17, w17 in w17_data.iterrows():
    if (w17['Detected District'].lower() != 'unknown') & (w17['Detected District'].lower() != 'yanam') & (
            w17['Detected District'].lower() != 'budgam') & (w17['Detected District'].lower() != 'chengalpattu') & (
            w17['Detected District'].lower() != 'evacuees') & (w17['Detected District'].lower() != 'morigaon') & (
            w17['Detected District'].lower() != 'other state') & (w17['Detected District'].lower() != 'ranipet') & (
            w17['Detected District'].lower() != 'south andaman') & (w17['Detected District'].lower() != 'tenkasi') & (
            w17['Detected District'].lower() != 'tirupathur') & (w17['Detected District'].lower() != 'unassigned') & (
            w17['Detected District'].lower() != 'airport quarantine') & (
            w17['Detected District'].lower() != 'bsf camp') & (w17['Detected District'].lower() != 'cooch behar') & (
            w17['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w17['Detected District'].lower() != 'foreign evacuees') & (
            w17['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w17['Detected District'].lower() != 'karbi anglong') & (w17['Detected District'].lower() != 'khawzawl') & (
            w17['Detected District'].lower() != 'lakhimpur') & (w17['Detected District'].lower() != 'other region') & (
            w17['Detected District'].lower() != 'railway quarantine') & (
            w17['Detected District'].lower() != 'saitual') & (w17['Detected District'].lower() != 'others'):
        if (w17['Num Cases'] > 0):
            value17[id_dist.get((w17['Detected District'].lower())) - 101] += w17['Num Cases']
w17_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value17})
w17_csv.insert(1, 'WeekId', 17)

w18_data = d_csv7[(d_csv7['Date Announced'] >= '2020/07/12') & (d_csv7['Date Announced'] <= '2020/07/18')]
value18 = [0] * n
for iq18, w18 in w18_data.iterrows():
    if (w18['Detected District'].lower() != 'unknown') & (w18['Detected District'].lower() != 'yanam') & (
            w18['Detected District'].lower() != 'budgam') & (w18['Detected District'].lower() != 'chengalpattu') & (
            w18['Detected District'].lower() != 'evacuees') & (w18['Detected District'].lower() != 'morigaon') & (
            w18['Detected District'].lower() != 'other state') & (w18['Detected District'].lower() != 'ranipet') & (
            w18['Detected District'].lower() != 'south andaman') & (w18['Detected District'].lower() != 'tenkasi') & (
            w18['Detected District'].lower() != 'tirupathur') & (w18['Detected District'].lower() != 'unassigned') & (
            w18['Detected District'].lower() != 'airport quarantine') & (
            w18['Detected District'].lower() != 'bsf camp') & (w18['Detected District'].lower() != 'cooch behar') & (
            w18['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w18['Detected District'].lower() != 'foreign evacuees') & (
            w18['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w18['Detected District'].lower() != 'karbi anglong') & (w18['Detected District'].lower() != 'khawzawl') & (
            w18['Detected District'].lower() != 'lakhimpur') & (w18['Detected District'].lower() != 'other region') & (
            w18['Detected District'].lower() != 'railway quarantine') & (
            w18['Detected District'].lower() != 'saitual') & (w18['Detected District'].lower() != 'others'):
        if (w18['Num Cases'] > 0):
            value18[id_dist.get((w18['Detected District'].lower())) - 101] += w18['Num Cases']
w18_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value18})
w18_csv.insert(1, 'WeekId', 18)

w19_data = d_csv7[(d_csv7['Date Announced'] >= '2020/07/19') & (d_csv7['Date Announced'] <= '2020/07/25')]
value19 = [0] * n
for iq19, w19 in w19_data.iterrows():
    if (w19['Detected District'].lower() != 'unknown') & (w19['Detected District'].lower() != 'yanam') & (
            w19['Detected District'].lower() != 'budgam') & (w19['Detected District'].lower() != 'chengalpattu') & (
            w19['Detected District'].lower() != 'evacuees') & (w19['Detected District'].lower() != 'morigaon') & (
            w19['Detected District'].lower() != 'other state') & (w19['Detected District'].lower() != 'ranipet') & (
            w19['Detected District'].lower() != 'south andaman') & (w19['Detected District'].lower() != 'tenkasi') & (
            w19['Detected District'].lower() != 'tirupathur') & (w19['Detected District'].lower() != 'unassigned') & (
            w19['Detected District'].lower() != 'airport quarantine') & (
            w19['Detected District'].lower() != 'bsf camp') & (w19['Detected District'].lower() != 'cooch behar') & (
            w19['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w19['Detected District'].lower() != 'foreign evacuees') & (
            w19['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w19['Detected District'].lower() != 'karbi anglong') & (w19['Detected District'].lower() != 'khawzawl') & (
            w19['Detected District'].lower() != 'lakhimpur') & (w19['Detected District'].lower() != 'other region') & (
            w19['Detected District'].lower() != 'railway quarantine') & (
            w19['Detected District'].lower() != 'saitual') & (w19['Detected District'].lower() != 'others'):
        if (w19['Num Cases'] > 0):
            value19[id_dist.get((w19['Detected District'].lower())) - 101] += w19['Num Cases']
w19_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value19})
w19_csv.insert(1, 'WeekId', 19)

w20_data = d_csv7[(d_csv7['Date Announced'] >= '2020/07/26') & (d_csv7['Date Announced'] <= '2020/08/01')]
value20 = [0] * n
for iq20, w20 in w20_data.iterrows():
    if (w20['Detected District'].lower() != 'capf personnel') & (w20['Detected District'].lower() != 'unknown') & (
            w20['Detected District'].lower() != 'yanam') & (w20['Detected District'].lower() != 'budgam') & (
            w20['Detected District'].lower() != 'chengalpattu') & (w20['Detected District'].lower() != 'evacuees') & (
            w20['Detected District'].lower() != 'morigaon') & (w20['Detected District'].lower() != 'other state') & (
            w20['Detected District'].lower() != 'ranipet') & (w20['Detected District'].lower() != 'south andaman') & (
            w20['Detected District'].lower() != 'tenkasi') & (w20['Detected District'].lower() != 'tirupathur') & (
            w20['Detected District'].lower() != 'unassigned') & (
            w20['Detected District'].lower() != 'airport quarantine') & (
            w20['Detected District'].lower() != 'bsf camp') & (w20['Detected District'].lower() != 'cooch behar') & (
            w20['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w20['Detected District'].lower() != 'foreign evacuees') & (
            w20['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w20['Detected District'].lower() != 'karbi anglong') & (w20['Detected District'].lower() != 'khawzawl') & (
            w20['Detected District'].lower() != 'lakhimpur') & (w20['Detected District'].lower() != 'other region') & (
            w20['Detected District'].lower() != 'railway quarantine') & (
            w20['Detected District'].lower() != 'saitual') & (w20['Detected District'].lower() != 'others'):
        if (w20['Num Cases'] > 0):
            value20[id_dist.get((w20['Detected District'].lower())) - 101] += w20['Num Cases']
w20_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value20})
w20_csv.insert(1, 'WeekId', 20)

w21_data = d_csv7[(d_csv7['Date Announced'] >= '2020/08/02') & (d_csv7['Date Announced'] <= '2020/08/08')]
value21 = [0] * n
for iq21, w21 in w21_data.iterrows():
    if (w21['Detected District'].lower() != 'italians') & (w21['Detected District'].lower() != 'hnahthial') & (
            w21['Detected District'].lower() != 'capf personnel') & (w21['Detected District'].lower() != 'unknown') & (
            w21['Detected District'].lower() != 'yanam') & (w21['Detected District'].lower() != 'budgam') & (
            w21['Detected District'].lower() != 'chengalpattu') & (w21['Detected District'].lower() != 'evacuees') & (
            w21['Detected District'].lower() != 'morigaon') & (w21['Detected District'].lower() != 'other state') & (
            w21['Detected District'].lower() != 'ranipet') & (w21['Detected District'].lower() != 'south andaman') & (
            w21['Detected District'].lower() != 'tenkasi') & (w21['Detected District'].lower() != 'tirupathur') & (
            w21['Detected District'].lower() != 'unassigned') & (
            w21['Detected District'].lower() != 'airport quarantine') & (
            w21['Detected District'].lower() != 'bsf camp') & (w21['Detected District'].lower() != 'cooch behar') & (
            w21['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w21['Detected District'].lower() != 'foreign evacuees') & (
            w21['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w21['Detected District'].lower() != 'karbi anglong') & (w21['Detected District'].lower() != 'khawzawl') & (
            w21['Detected District'].lower() != 'lakhimpur') & (w21['Detected District'].lower() != 'other region') & (
            w21['Detected District'].lower() != 'railway quarantine') & (
            w21['Detected District'].lower() != 'saitual') & (w21['Detected District'].lower() != 'others'):
        if (w21['Num Cases'] > 0):
            value21[id_dist.get((w21['Detected District'].lower())) - 101] += w21['Num Cases']
w21_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value21})
w21_csv.insert(1, 'WeekId', 21)

w22_data = d_csv7[(d_csv7['Date Announced'] >= '2020/08/09') & (d_csv7['Date Announced'] <= '2020/08/15')]
value22 = [0] * n
for iq22, w22 in w22_data.iterrows():
    if (w22['Detected District'].lower() != 'italians') & (w22['Detected District'].lower() != 'hnahthial') & (
            w22['Detected District'].lower() != 'capf personnel') & (w22['Detected District'].lower() != 'unknown') & (
            w22['Detected District'].lower() != 'yanam') & (w22['Detected District'].lower() != 'budgam') & (
            w22['Detected District'].lower() != 'chengalpattu') & (w22['Detected District'].lower() != 'evacuees') & (
            w22['Detected District'].lower() != 'morigaon') & (w22['Detected District'].lower() != 'other state') & (
            w22['Detected District'].lower() != 'ranipet') & (w22['Detected District'].lower() != 'south andaman') & (
            w22['Detected District'].lower() != 'tenkasi') & (w22['Detected District'].lower() != 'tirupathur') & (
            w22['Detected District'].lower() != 'unassigned') & (
            w22['Detected District'].lower() != 'airport quarantine') & (
            w22['Detected District'].lower() != 'bsf camp') & (w22['Detected District'].lower() != 'cooch behar') & (
            w22['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w22['Detected District'].lower() != 'foreign evacuees') & (
            w22['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w22['Detected District'].lower() != 'karbi anglong') & (w22['Detected District'].lower() != 'khawzawl') & (
            w22['Detected District'].lower() != 'lakhimpur') & (w22['Detected District'].lower() != 'other region') & (
            w22['Detected District'].lower() != 'railway quarantine') & (
            w22['Detected District'].lower() != 'saitual') & (w22['Detected District'].lower() != 'others'):
        if (w22['Num Cases'] > 0):
            value22[id_dist.get((w22['Detected District'].lower())) - 101] += w22['Num Cases']
w22_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value22})
w22_csv.insert(1, 'WeekId', 22)

w23_data = d_csv7[(d_csv7['Date Announced'] >= '2020/08/16') & (d_csv7['Date Announced'] <= '2020/08/22')]
value23 = [0] * n
for iq23, w23 in w23_data.iterrows():
    if (w23['Detected District'].lower() != 'italians') & (w23['Detected District'].lower() != 'hnahthial') & (
            w23['Detected District'].lower() != 'capf personnel') & (w23['Detected District'].lower() != 'unknown') & (
            w23['Detected District'].lower() != 'yanam') & (w23['Detected District'].lower() != 'budgam') & (
            w23['Detected District'].lower() != 'chengalpattu') & (w23['Detected District'].lower() != 'evacuees') & (
            w23['Detected District'].lower() != 'morigaon') & (w23['Detected District'].lower() != 'other state') & (
            w23['Detected District'].lower() != 'ranipet') & (w23['Detected District'].lower() != 'south andaman') & (
            w23['Detected District'].lower() != 'tenkasi') & (w23['Detected District'].lower() != 'tirupathur') & (
            w23['Detected District'].lower() != 'unassigned') & (
            w23['Detected District'].lower() != 'airport quarantine') & (
            w23['Detected District'].lower() != 'bsf camp') & (w23['Detected District'].lower() != 'cooch behar') & (
            w23['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w23['Detected District'].lower() != 'foreign evacuees') & (
            w23['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w23['Detected District'].lower() != 'karbi anglong') & (w23['Detected District'].lower() != 'khawzawl') & (
            w23['Detected District'].lower() != 'lakhimpur') & (w23['Detected District'].lower() != 'other region') & (
            w23['Detected District'].lower() != 'railway quarantine') & (
            w23['Detected District'].lower() != 'saitual') & (w23['Detected District'].lower() != 'others'):
        if (w23['Num Cases'] > 0):
            value23[id_dist.get((w23['Detected District'].lower())) - 101] += w23['Num Cases']
w23_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value23})
w23_csv.insert(1, 'WeekId', 23)

w24_data = d_csv7[(d_csv7['Date Announced'] >= '2020/08/23') & (d_csv7['Date Announced'] <= '2020/08/29')]
value24 = [0] * n
for iq24, w24 in w24_data.iterrows():
    if (w24['Detected District'].lower() != 'hnahthial') & (w24['Detected District'].lower() != 'italians') & (
            w24['Detected District'].lower() != 'capf personnel') & (w24['Detected District'].lower() != 'unknown') & (
            w24['Detected District'].lower() != 'yanam') & (w24['Detected District'].lower() != 'budgam') & (
            w24['Detected District'].lower() != 'chengalpattu') & (w24['Detected District'].lower() != 'evacuees') & (
            w24['Detected District'].lower() != 'morigaon') & (w24['Detected District'].lower() != 'other state') & (
            w24['Detected District'].lower() != 'ranipet') & (w24['Detected District'].lower() != 'south andaman') & (
            w24['Detected District'].lower() != 'tenkasi') & (w24['Detected District'].lower() != 'tirupathur') & (
            w24['Detected District'].lower() != 'unassigned') & (
            w24['Detected District'].lower() != 'airport quarantine') & (
            w24['Detected District'].lower() != 'bsf camp') & (w24['Detected District'].lower() != 'cooch behar') & (
            w24['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w24['Detected District'].lower() != 'foreign evacuees') & (
            w24['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w24['Detected District'].lower() != 'karbi anglong') & (w24['Detected District'].lower() != 'khawzawl') & (
            w24['Detected District'].lower() != 'lakhimpur') & (w24['Detected District'].lower() != 'other region') & (
            w24['Detected District'].lower() != 'railway quarantine') & (
            w24['Detected District'].lower() != 'saitual') & (w24['Detected District'].lower() != 'others'):
        if (w24['Num Cases'] > 0):
            value24[id_dist.get((w24['Detected District'].lower())) - 101] += w24['Num Cases']
w24_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value24})
w24_csv.insert(1, 'WeekId', 24)

w25_data = d_csv7[(d_csv7['Date Announced'] >= '2020/08/30') & (d_csv7['Date Announced'] <= '2020/09/05')]
value25 = [0] * n
for iq25, w25 in w25_data.iterrows():
    if (w25['Detected District'].lower() != 'hnahthial') & (w25['Detected District'].lower() != 'italians') & (
            w25['Detected District'].lower() != 'capf personnel') & (w25['Detected District'].lower() != 'unknown') & (
            w25['Detected District'].lower() != 'yanam') & (w25['Detected District'].lower() != 'budgam') & (
            w25['Detected District'].lower() != 'chengalpattu') & (w25['Detected District'].lower() != 'evacuees') & (
            w25['Detected District'].lower() != 'morigaon') & (w25['Detected District'].lower() != 'other state') & (
            w25['Detected District'].lower() != 'ranipet') & (w25['Detected District'].lower() != 'south andaman') & (
            w25['Detected District'].lower() != 'tenkasi') & (w25['Detected District'].lower() != 'tirupathur') & (
            w25['Detected District'].lower() != 'unassigned') & (
            w25['Detected District'].lower() != 'airport quarantine') & (
            w25['Detected District'].lower() != 'bsf camp') & (w25['Detected District'].lower() != 'cooch behar') & (
            w25['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w25['Detected District'].lower() != 'foreign evacuees') & (
            w25['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w25['Detected District'].lower() != 'karbi anglong') & (w25['Detected District'].lower() != 'khawzawl') & (
            w25['Detected District'].lower() != 'lakhimpur') & (w25['Detected District'].lower() != 'other region') & (
            w25['Detected District'].lower() != 'railway quarantine') & (
            w25['Detected District'].lower() != 'saitual') & (w25['Detected District'].lower() != 'others'):
        if (w25['Num Cases'] > 0):
            value25[id_dist.get((w25['Detected District'].lower())) - 101] += w25['Num Cases']
w25_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value25})
w25_csv.insert(1, 'WeekId', 25)

weekly = [w1_csv, w2_csv, w3_csv, w4_csv, w5_csv, w6_csv, w7_csv, w8_csv, w9_csv, w10_csv, w11_csv, w12_csv, w13_csv,
          w14_csv, w15_csv, w16_csv, w17_csv, w18_csv, w19_csv, w20_csv, w21_csv, w22_csv, w23_csv, w24_csv, w25_csv]
res = pd.concat(weekly)
res = res.sort_values(['District', 'WeekId'])
res.to_csv('Cases-week.csv', index=False, header=True)

# monthly


m1_data = d_csv[(d_csv['Date'] >= '2020/03/29') & (d_csv['Date'] <= '2020/03/31')]
mon1_extra = [0] * n
d1 = 0
for m1 in modified_dist:
    for mq1 in m1_data['District']:
        if m1 == mq1:
            mon1_extra[d1] += 1
    d1 = d1 + 1
mon1 = list(np.array(value1) + np.array(value2) + np.array(mon1_extra))
m1_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': mon1})
m1_csv.insert(1, 'Month_ID', 1)

m2_data = d_csv[(d_csv['Date'] >= '2020/04/01') & (d_csv['Date'] <= '2020/04/04')]
mon2_extra = [0] * n
d2 = 0
for m2 in modified_dist:
    for mq2 in m2_data['District']:
        if m2 == mq2:
            mon2_extra[d2] += 1
    d2 = d2 + 1
m2_data = d_csv[(d_csv['Date'] >= '2020/04/27') & (d_csv['Date'] <= '2020/04/30')]
mon2_extra1 = [0] * n
for iq2, m2 in m2_data.iterrows():
    if (m2['Detected District'].lower() != 'hnahthial') & (m2['Detected District'].lower() != 'italians') & (
            m2['Detected District'].lower() != 'capf personnel') & (m2['Detected District'].lower() != 'unknown') & (
            m2['Detected District'].lower() != 'yanam') & (m2['Detected District'].lower() != 'budgam') & (
            m2['Detected District'].lower() != 'chengalpattu') & (m2['Detected District'].lower() != 'evacuees') & (
            m2['Detected District'].lower() != 'morigaon') & (m2['Detected District'].lower() != 'other state') & (
            m2['Detected District'].lower() != 'ranipet') & (m2['Detected District'].lower() != 'south andaman') & (
            m2['Detected District'].lower() != 'tenkasi') & (m2['Detected District'].lower() != 'tirupathur') & (
            m2['Detected District'].lower() != 'unassigned') & (
            m2['Detected District'].lower() != 'airport quarantine') & (
            m2['Detected District'].lower() != 'bsf camp') & (m2['Detected District'].lower() != 'cooch behar') & (
            m2['Detected District'].lower() != 'dakshin bastar dantewada') & (
            m2['Detected District'].lower() != 'foreign evacuees') & (
            m2['Detected District'].lower() != 'gaurela pendra marwahi') & (
            m2['Detected District'].lower() != 'karbi anglong') & (m2['Detected District'].lower() != 'khawzawl') & (
            m2['Detected District'].lower() != 'lakhimpur') & (m2['Detected District'].lower() != 'other region') & (
            m2['Detected District'].lower() != 'railway quarantine') & (
            m2['Detected District'].lower() != 'saitual') & (m2['Detected District'].lower() != 'others'):
        if (m2['Num Cases'] > 0):
            mon2_extra1[id_dist.get((m2['Detected District'].lower())) - 101] += m2['Num Cases']
m2_data = d_csv[(d_csv['Date'] == '2020/04/26')]
mon2_extra2 = [0] * n
d2 = 0
for m2 in modified_dist:
    for mq2 in m2_data['District']:
        if m2 == mq2:
            mon2_extra2[d2] += 1
    d2 = d2 + 1

mon2 = list(
    np.array(value4) + np.array(value5) + np.array(value6) + np.array(mon2_extra) + np.array(mon2_extra1) + np.array(
        mon2_extra2))  # 5 days left 26/4 to 30/4
m2_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': mon2})
m2_csv.insert(1, 'Month_ID', 2)

w26_data = d_csv7[(d_csv7['Date Announced'] >= '2020/05/01') & (d_csv7['Date Announced'] <= '2020/05/02')]
value26_extra = [0] * n
for iq26, w26 in w26_data.iterrows():
    if (w26['Detected District'].lower() != 'hnahthial') & (w26['Detected District'].lower() != 'italians') & (
            w26['Detected District'].lower() != 'capf personnel') & (w26['Detected District'].lower() != 'unknown') & (
            w26['Detected District'].lower() != 'yanam') & (w26['Detected District'].lower() != 'budgam') & (
            w26['Detected District'].lower() != 'chengalpattu') & (w26['Detected District'].lower() != 'evacuees') & (
            w26['Detected District'].lower() != 'morigaon') & (w26['Detected District'].lower() != 'other state') & (
            w26['Detected District'].lower() != 'ranipet') & (w26['Detected District'].lower() != 'south andaman') & (
            w26['Detected District'].lower() != 'tenkasi') & (w26['Detected District'].lower() != 'tirupathur') & (
            w26['Detected District'].lower() != 'unassigned') & (
            w26['Detected District'].lower() != 'airport quarantine') & (
            w26['Detected District'].lower() != 'bsf camp') & (w26['Detected District'].lower() != 'cooch behar') & (
            w26['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w26['Detected District'].lower() != 'foreign evacuees') & (
            w26['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w26['Detected District'].lower() != 'karbi anglong') & (w26['Detected District'].lower() != 'khawzawl') & (
            w26['Detected District'].lower() != 'lakhimpur') & (w26['Detected District'].lower() != 'other region') & (
            w26['Detected District'].lower() != 'railway quarantine') & (
            w26['Detected District'].lower() != 'saitual') & (w26['Detected District'].lower() != 'others'):
        if (w26['Num Cases'] > 0):
            value26_extra[id_dist.get((w26['Detected District'].lower())) - 101] += w26['Num Cases']
w26_data = d_csv7[(d_csv7['Date Announced'] == '2020/05/31')]
value26_extra1 = [0] * n
for iq26, w26 in w26_data.iterrows():
    if (w26['Detected District'].lower() != 'hnahthial') & (w26['Detected District'].lower() != 'italians') & (
            w26['Detected District'].lower() != 'capf personnel') & (w26['Detected District'].lower() != 'unknown') & (
            w26['Detected District'].lower() != 'yanam') & (w26['Detected District'].lower() != 'budgam') & (
            w26['Detected District'].lower() != 'chengalpattu') & (w26['Detected District'].lower() != 'evacuees') & (
            w26['Detected District'].lower() != 'morigaon') & (w26['Detected District'].lower() != 'other state') & (
            w26['Detected District'].lower() != 'ranipet') & (w26['Detected District'].lower() != 'south andaman') & (
            w26['Detected District'].lower() != 'tenkasi') & (w26['Detected District'].lower() != 'tirupathur') & (
            w26['Detected District'].lower() != 'unassigned') & (
            w26['Detected District'].lower() != 'airport quarantine') & (
            w26['Detected District'].lower() != 'bsf camp') & (w26['Detected District'].lower() != 'cooch behar') & (
            w26['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w26['Detected District'].lower() != 'foreign evacuees') & (
            w26['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w26['Detected District'].lower() != 'karbi anglong') & (w26['Detected District'].lower() != 'khawzawl') & (
            w26['Detected District'].lower() != 'lakhimpur') & (w26['Detected District'].lower() != 'other region') & (
            w26['Detected District'].lower() != 'railway quarantine') & (
            w26['Detected District'].lower() != 'saitual') & (w26['Detected District'].lower() != 'others'):
        if (w26['Num Cases'] > 0):
            value26_extra1[id_dist.get((w26['Detected District'].lower())) - 101] += w26['Num Cases']
value26 = list(
    np.array(value8) + np.array(value9) + np.array(value10) + np.array(value11) + np.array(value26_extra) + np.array(
        value26_extra1))

m3_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value26})
m3_csv.insert(1, 'Month_ID', 3)

w27_data = d_csv7[(d_csv7['Date Announced'] >= '2020/07/01') & (d_csv7['Date Announced'] <= '2020/07/04')]
value27_extra = [0] * n
for iq27, w27 in w27_data.iterrows():
    if (w27['Detected District'].lower() != 'hnahthial') & (w27['Detected District'].lower() != 'italians') & (
            w27['Detected District'].lower() != 'capf personnel') & (w27['Detected District'].lower() != 'unknown') & (
            w27['Detected District'].lower() != 'yanam') & (w27['Detected District'].lower() != 'budgam') & (
            w27['Detected District'].lower() != 'chengalpattu') & (w27['Detected District'].lower() != 'evacuees') & (
            w27['Detected District'].lower() != 'morigaon') & (w27['Detected District'].lower() != 'other state') & (
            w27['Detected District'].lower() != 'ranipet') & (w27['Detected District'].lower() != 'south andaman') & (
            w27['Detected District'].lower() != 'tenkasi') & (w27['Detected District'].lower() != 'tirupathur') & (
            w27['Detected District'].lower() != 'unassigned') & (
            w27['Detected District'].lower() != 'airport quarantine') & (
            w27['Detected District'].lower() != 'bsf camp') & (w27['Detected District'].lower() != 'cooch behar') & (
            w27['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w27['Detected District'].lower() != 'foreign evacuees') & (
            w27['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w27['Detected District'].lower() != 'karbi anglong') & (w27['Detected District'].lower() != 'khawzawl') & (
            w27['Detected District'].lower() != 'lakhimpur') & (w27['Detected District'].lower() != 'other region') & (
            w27['Detected District'].lower() != 'railway quarantine') & (
            w27['Detected District'].lower() != 'saitual') & (w27['Detected District'].lower() != 'others'):
        if (w27['Num Cases'] > 0):
            value27_extra[id_dist.get((w27['Detected District'].lower())) - 101] += w27['Num Cases']
value27 = list(
    np.array(value12) + np.array(value13) + np.array(value14) + np.array(value15) - np.array(value26_extra1) - np.array(
        value27_extra) + np.array(value16))

m4_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value27})
m4_csv.insert(1, 'Month_ID', 4)

w28_data = d_csv7[(d_csv7['Date Announced'] == '2020/08/01')]
value28_extra = [0] * n
for iq28, w28 in w28_data.iterrows():
    if (w28['Detected District'].lower() != 'hnahthial') & (w28['Detected District'].lower() != 'italians') & (
            w28['Detected District'].lower() != 'capf personnel') & (w28['Detected District'].lower() != 'unknown') & (
            w28['Detected District'].lower() != 'yanam') & (w28['Detected District'].lower() != 'budgam') & (
            w28['Detected District'].lower() != 'chengalpattu') & (w28['Detected District'].lower() != 'evacuees') & (
            w28['Detected District'].lower() != 'morigaon') & (w28['Detected District'].lower() != 'other state') & (
            w28['Detected District'].lower() != 'ranipet') & (w28['Detected District'].lower() != 'south andaman') & (
            w28['Detected District'].lower() != 'tenkasi') & (w28['Detected District'].lower() != 'tirupathur') & (
            w28['Detected District'].lower() != 'unassigned') & (
            w28['Detected District'].lower() != 'airport quarantine') & (
            w28['Detected District'].lower() != 'bsf camp') & (w28['Detected District'].lower() != 'cooch behar') & (
            w28['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w28['Detected District'].lower() != 'foreign evacuees') & (
            w28['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w28['Detected District'].lower() != 'karbi anglong') & (w28['Detected District'].lower() != 'khawzawl') & (
            w28['Detected District'].lower() != 'lakhimpur') & (w28['Detected District'].lower() != 'other region') & (
            w28['Detected District'].lower() != 'railway quarantine') & (
            w28['Detected District'].lower() != 'saitual') & (w28['Detected District'].lower() != 'others'):
        if (w28['Num Cases'] > 0):
            value28_extra[id_dist.get((w28['Detected District'].lower())) - 101] += w28['Num Cases']
value28 = list(
    np.array(value17) + np.array(value18) + np.array(value19) + np.array(value20) + np.array(value27_extra) - np.array(
        value28_extra))

m5_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value28})
m5_csv.insert(1, 'Month_ID', 5)

w29_data = d_csv7[(d_csv7['Date Announced'] >= '2020/09/01') & (d_csv7['Date Announced'] <= '2020/09/05')]
value29_extra = [0] * n
for iq29, w29 in w29_data.iterrows():
    if (w29['Detected District'].lower() != 'hnahthial') & (w29['Detected District'].lower() != 'italians') & (
            w29['Detected District'].lower() != 'capf personnel') & (w29['Detected District'].lower() != 'unknown') & (
            w29['Detected District'].lower() != 'yanam') & (w29['Detected District'].lower() != 'budgam') & (
            w29['Detected District'].lower() != 'chengalpattu') & (w29['Detected District'].lower() != 'evacuees') & (
            w29['Detected District'].lower() != 'morigaon') & (w29['Detected District'].lower() != 'other state') & (
            w29['Detected District'].lower() != 'ranipet') & (w29['Detected District'].lower() != 'south andaman') & (
            w29['Detected District'].lower() != 'tenkasi') & (w29['Detected District'].lower() != 'tirupathur') & (
            w29['Detected District'].lower() != 'unassigned') & (
            w29['Detected District'].lower() != 'airport quarantine') & (
            w29['Detected District'].lower() != 'bsf camp') & (w29['Detected District'].lower() != 'cooch behar') & (
            w29['Detected District'].lower() != 'dakshin bastar dantewada') & (
            w29['Detected District'].lower() != 'foreign evacuees') & (
            w29['Detected District'].lower() != 'gaurela pendra marwahi') & (
            w29['Detected District'].lower() != 'karbi anglong') & (w29['Detected District'].lower() != 'khawzawl') & (
            w29['Detected District'].lower() != 'lakhimpur') & (w29['Detected District'].lower() != 'other region') & (
            w29['Detected District'].lower() != 'railway quarantine') & (
            w29['Detected District'].lower() != 'saitual') & (w29['Detected District'].lower() != 'others'):
        if (w29['Num Cases'] > 0):
            value29_extra[id_dist.get((w29['Detected District'].lower())) - 101] += w29['Num Cases']
value29 = list(
    np.array(value21) + np.array(value22) + np.array(value23) + np.array(value24) + np.array(value25) + np.array(
        value28_extra) - np.array(value29_extra))

m6_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value29})
m6_csv.insert(1, 'Month_ID', 6)

m7_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': value29_extra})
m7_csv.insert(1, 'Month_ID', 7)

monthly = [m1_csv, m2_csv, m3_csv, m4_csv, m5_csv, m6_csv, m7_csv]
res1 = pd.concat(monthly)
res1 = res1.sort_values(['District', 'Month_ID'])
res1.to_csv('Cases-Month.csv', index=False, header=True)

# overall cases
over1 = list(
    np.array(value29_extra) + np.array(value29) + np.array(value28) + np.array(value27) + np.array(value26) + np.array(
        mon2) + np.array(mon1))

o1_csv = pd.DataFrame({'District': list_id_modified_dist, 'Cases': over1})
o1_csv.insert(1, 'Overall', 1)
o1_csv.to_csv('cases-overall.csv', index=False, header=True)
