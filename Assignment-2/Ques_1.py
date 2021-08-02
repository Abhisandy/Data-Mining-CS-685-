import pandas as pd
import numpy as np
from collections import OrderedDict

df_articles = pd.read_csv('Data/articles.tsv')
df_articles = df_articles.iloc[10:]

df_articles.index = df_articles.index.get_level_values(0)

index_names = []
for a in df_articles.index:
    index_names.append(a)

index_real = []
for b in range(1,4605):
    index_real.append('A'+"{:04d}".format(b))

dict_names = {}
count = 0
for c in index_real:
    dict_names[c] = index_names[count]
    count += 1

dict_names_keys = []
for keys in dict_names.keys():
    dict_names_keys.append(keys)

dict_names_values = []
for values in dict_names.values():
    dict_names_values.append(values)

index_real_df = pd.DataFrame({'IDs' : dict_names_values , 'Articles':dict_names_keys})
index_real_df.to_csv('article-ids.csv' , index = False , header = False)

list_t = dict_names.values()
list_t_different = list(OrderedDict.fromkeys(list_t)) 