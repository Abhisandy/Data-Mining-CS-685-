import json
import csv
import pandas as pd


pd.set_option('display.max_rows', None)

with open('neighbor-districts.json') as f:
    data = json.load(f)
list_dist = [] #list for districts of neighbour-district.json
for i in data:
    i = i.split('/')
    list_dist.append(i[0])
dict_dist = {}
for di in list_dist:
    if di == 'bijapur_district' :
        dict_dist[di] = di.replace('bijapur_district', 'vijayapura')
    elif di == 'bidar_district' :  #coz it create problem afterwards when i replace "bid->beed", it becomes beedar
        dict_dist[di] = di.replace('bidar_district', 'bidar')
    elif di == 'lower_dibang_valley':
        dict_dist[di] = di.replace('lower_dibang_valley', 'lower dibang valley')
    elif di == 'south_salmara-mankachar':
        dict_dist[di] = di.replace('south_salmara-mankachar', 'south salmara mankachar')
    else :
        dict_dist[di] = di.replace('_' , ' ').replace(' district', '').replace('maldah', 'malda').replace('pashchimi singhbhum', 'west singhbhum').replace('purbi singhbhum', 'east singhbhum').replace('pashchim champaran', 'west champaran').replace('purba champaran', 'east champaran').replace('bishwanath', 'biswanath').replace('the nilgiris', 'nilgiris').replace('the dangs','dang').replace('yadagiri','yadgir').replace('debagarh','deogarh').replace('faizabad','ayodhya').replace('mumbai city','mumbai').replace('jyotiba phule nagar','amroha').replace('bangalore urban','bengaluru urban').replace('bangalore rural','bengaluru rural').replace('yadagiri district','yadgir').replace('sonapur','subarnapur').replace('muktsar','sri muktsar sahib').replace('sepahijala','sipahijala').replace('siddharth nagar','siddharthnagar').replace('sharawasti','shrawasti').replace('shimoga','shivamogga').replace('seraikela kharsawan','saraikela-kharsawan').replace('ri-bhoi','ribhoi').replace('puruliya','purulia').replace('pakaur','pakur').replace('narsimhapur','narsinghpur').replace('lower dibang valley','lower dibang valley').replace('kaimur (bhabua)','kaimur').replace('kabirdham','kabeerdham').replace('janjgir-champa','janjgir champa').replace('jalor','jalore').replace('sri ganganagar', 'ganganagar').replace('lower dibang valley','dibang valley').replace('devbhumi dwaraka', 'devbhumi dwarka').replace('nav sari','navsari').replace('chamarajanagar','chamarajanagara').replace('baudh', 'boudh').replace('bemetara', 'bametara').replace('bid', 'beed').replace('bellary', 'ballari').replace('ashok nagar', 'ashoknagar').replace('anugul', 'angul').replace('aizwal', 'aizawl').replace('baleshwar', 'balasore').replace('tiruchchirappalli', 'tiruchirappalli').replace('tirunelveli kattabo', 'tirunelveli').replace('belgaum', 'belagavi').replace('ysr', 'y.s.r. kadapa').replace('lakhimpur', 'lakhimpur kheri').replace('sri potti sriramulu nellore', 's.p.s. nellore').replace('banas kantha', 'banaskantha').replace('baramula', 'baramulla').replace('dhaulpur', 'dholpur').replace('jajapur', 'jajpur').replace('jhunjhunun', 'jhunjhunu').replace('shaheed bhagat singh nagar', 'shahid bhagat singh nagar').replace('sait kibir nagar', 'sant kabir nagar').replace('tiruvanamalai', 'tiruvannamalai').replace('thoothukudi', 'thoothukkudi').replace('sivagangai', 'sivaganga').replace('shopian', 'shopiyan').replace('komram bheem', 'komaram bheem').replace('rae bareilly', 'rae bareli').replace('rangareddy', 'ranga reddy').replace('sahibzada ajit singh nagar', 's.a.s. nagar').replace('kanchipuram', 'kancheepuram').replace('panch mahal', 'panchmahal').replace('sabar kantha', 'sabarkantha').replace('firozpur', 'ferozepur').replace('gondiya', 'gondia').replace('hugli', 'hooghly').replace('medchal–malkajgiri', 'medchal malkajgiri').replace('mahesana', 'mehsana').replace('pattanamtitta', 'pathanamthitta').replace('mahrajganj', 'maharajganj').replace('nandubar' ,'nandurbar').replace('palghat', 'palakkad').replace('tumkur', 'tumakuru').replace('fategarh sahib', 'fatehgarh sahib').replace('kodarma', 'koderma').replace('sant ravidas nagar', 'bhadohi').replace('rajauri' ,'rajouri').replace('jagatsinghapur','jagatsinghpur').replace('lahul and spiti','lahaul and spiti')
#.replace('east delhi','delhi')
list_keys_district = []
list_of_rightdis = []
for ke in dict_dist.keys():
    list_keys_district.append(ke)
    list_of_rightdis.append(dict_dist.get(ke))
list_of_rightdis.sort()
#print(list_of_rightdis)

with open('neighbor-districts.json') as f:
    dat = json.load(f)
modified = {}
for ae in dat:
    temp_list = []
    for ar in dat[ae]:
        ar = ar.split('/')
        temp_list.append(dict_dist.get(ar[0]))
    ae = ae.split('/')
    modified.update({dict_dist.get(ae[0]): temp_list})

del modified["central delhi"]
del modified["south delhi"]
del modified["north delhi"]
del modified["north west delhi"]
del modified["west delhi"]
del modified["south west delhi"]
del modified["new delhi"]
del modified["east delhi"]
del modified["north east delhi"]
del modified["south east delhi"]
del modified["mumbai"] #old name mumbai_city replaced to mumbai so deleting it here and create new one which contain all its neighbour
del modified["mumbai suburban"]
for ag in modified:
    for ah in modified[ag]:
        if ((ah=="mumbai suburban") or (ah=="north east delhi") or (ah=="south east delhi") or (ah=="central delhi") or (ah=="east delhi") or (ah=="south delhi") or (ah=="west delhi") or (ah=="north delhi") or (ah=="north west delhi") or (ah=="new delhi") or (ah=="south west delhi")):
            modified[ag].remove(ah)
del modified["shahdara"][1]
del modified["gautam buddha nagar"][0]
del modified["sonipat"][3]
del modified["jhajjar"][6]
modified.update({'delhi': ['gautam buddha nagar','north east delhi','south east delhi','central delhi','east delhi','south delhi','ghaziabad','shahdara','west delhi','north delhi','north west delhi','new delhi','gurugram','faridabad','sonipat','baghpat','jhajjar','south west delhi']})
modified.update({'mumbai':["konkan division","raigad","nashik","pune","ahmednagar","palghar","kolhapur","sindhudurg","thane","valsad","belagavi","north goa","satara","ratnagiri","dadra and nagar haveli","sangli"]})
modified.update({'north east delhi': ['delhi']})
modified.update({'south east delhi' : ['delhi']})
modified.update({'central delhi' : ['delhi']})
modified.update({'east delhi' : ['delhi']})
modified.update({'south delhi' : ['delhi']})
modified.update({'north delhi' : ['delhi']})
modified.update({'west delhi' : ['delhi']})
modified.update({'north west delhi' : ['delhi']})
modified.update({'new delhi' : ['delhi']})
modified.update({'south west delhi' : ['delhi']})
modified.update({'mumbai suburban': ['mumbai']})

modified["gautam buddha nagar"].append('delhi')
modified["ghaziabad"].append('delhi')
modified["shahdara"].append('delhi')
modified["gurugram"].append('delhi')
modified["faridabad"].append('delhi')
modified["sonipat"].append('delhi')
modified["baghpat"].append('delhi')
modified["jhajjar"].append('delhi')

#print(len(modified))
json_modified = json.dumps(modified, indent = 4)

with open("neighbor-districts-modified.json", "w") as outfile:
    outfile.write(json_modified)
#print(json_modified)

modified_dist = []
for aj in modified:
    modified_dist.append(aj)
modified_dist.sort()
id_dist= {}
ct = 101
for ak in modified_dist:
    id_dist[ak] = ct
    ct += 1
#print(id_dist)


# to check difference in districts

#print(len(modified_dist))
#print(modified_dist)
#dis_csv1 = pd.read_csv('json_data/raw_data1.csv')
#dis_csv2 = pd.read_csv('json_data/raw_data2.csv')
#dis_csv3 = pd.read_csv('json_data/raw_data3.csv')
#dis_csv4 = pd.read_csv('json_data/raw_data4.csv')
#dis_csv5 = pd.read_csv('json_data/raw_data5.csv')
#dis_csv6 = pd.read_csv('json_data/raw_data6.csv')
#dis_csv7 = pd.read_csv('json_data/raw_data7.csv')
#dis_csv8 = pd.read_csv('json_data/raw_data8.csv')
#dis_csv9 = pd.read_csv('json_data/raw_data9.csv')
#dis_csv10 = pd.read_csv('json_data/raw_data10.csv')
#dis_csv11 = pd.read_csv('json_data/raw_data11.csv')
#dis_csv12 = pd.read_csv('json_data/raw_data12.csv')
#dis_csv13 = pd.read_csv('json_data/raw_data13.csv')
#dis_csv14 = pd.read_csv('json_data/raw_data14.csv')
#tmep_data = [dis_csv1,dis_csv2,dis_csv3, dis_csv4, dis_csv5, dis_csv6, dis_csv7, dis_csv8 ,dis_csv9, dis_csv10 ,dis_csv11,dis_csv12 ,dis_csv13, dis_csv14]
#contemp = pd.concat(tmep_data)
#tmepe = []
#for dfct in contemp['Detected District']:
#    dfct = str(dfct).lower()
#    tmepe.append(dfct)


#def Diff(li1, li2):
#    li_dif = [item for item in li1 if item not in li2]
#    return li_dif
#list_diff = Diff(tmepe , modified_dist)
#list_diff = list(dict.fromkeys(list_diff))
#list_diff.sort()
#print(list_diff)
#print(len(list_diff))