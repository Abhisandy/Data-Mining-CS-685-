import pandas as pd
import numpy as np
import csv
from collections import OrderedDict
from Ques_2 import dict_diff_articleAndCategory_id

with open('article-categories.csv', 'w', newline='') as zww:
    the_zww = csv.writer(zww)

    for i in dict_diff_articleAndCategory_id.keys():
        if len(dict_diff_articleAndCategory_id[i]) == 1:
            the_zww.writerow([i, dict_diff_articleAndCategory_id[i][0]])
        elif len(dict_diff_articleAndCategory_id[i]) == 2:
            the_zww.writerow([i, dict_diff_articleAndCategory_id[i][0], dict_diff_articleAndCategory_id[i][1]])
        elif len(dict_diff_articleAndCategory_id[i]) == 3:
            the_zww.writerow([i, dict_diff_articleAndCategory_id[i][0], dict_diff_articleAndCategory_id[i][1],
                              dict_diff_articleAndCategory_id[i][2]])       