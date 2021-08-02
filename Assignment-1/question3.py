import json
import csv
#import import_ipynb
from question1 import id_dist
with open('neighbor-districts-modified.json') as f1:
    nei = json.load(f1)
    list_distr = []
for n3 in nei:
    list_distr.append(n3)
list_distr.sort()

with open('edge-graph.csv', 'w', newline='') as nei_dis:
    the_writer = csv.writer(nei_dis)
    the_writer.writerow(["Id", "neighbour"])
    for n1 in list_distr:
        for n2 in nei[n1]:
            the_writer.writerow([id_dist.get(n1), id_dist.get(n2)])
