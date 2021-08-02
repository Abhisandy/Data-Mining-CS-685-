import pandas as pd
import numpy as np
import re
import csv
import sys
from collections import defaultdict
from collections import OrderedDict
import networkx as nx
sys.setrecursionlimit(10000)

df_edges = pd.read_csv("edges.csv" , header = None)
df_ShortestPath = pd.read_csv("Data/shortest-path-distance-matrix.txt",sep="\tab",header = None,engine='python')
df_ShortestPath = df_ShortestPath.iloc[16:]


class Graph:
    list_ans = []

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.li_1d = []
        self.li_2d = []
        self.Time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def SCCUtil(self, u, low, disc, stackMember, st):

        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        stackMember[u] = True
        st.append(u)

        for v in self.graph[u]:

            if disc[v] == -1:

                self.SCCUtil(v, low, disc, stackMember, st)

                low[u] = min(low[u], low[v])

            elif stackMember[v] == True:

                low[u] = min(low[u], disc[v])


        w = -1
        if low[u] == disc[u]:
            while w != u:
                w = st.pop()
                self.li_1d.append(w)

                stackMember[w] = False
            self.li_2d.append(self.li_1d)
            self.li_1d = []

    def SCC(self):

        disc = [-1] * (self.V)
        low = [-1] * (self.V)
        stackMember = [False] * (self.V)
        st = []


        for i in range(self.V):
            if disc[i] == -1:
                self.SCCUtil(i, low, disc, stackMember, st)

    def cpy(self):
        list_ans = self.li_2d
        list_ans = list_ans[1:]
        Node = []
        Edges = []
        Dia = []
        n = 0
        for com in list_ans:

            if (len(com) == 1):
                Dia.append(0)
                Node.append(1)
                Edges.append(0)
                n = n + 1
            elif (len(com) == 2):
                Dia.append(1)
                Node.append(2)
                Edges.append(2)
                n = n + 1
            else:
                f = nx.Graph()
                count = 0
                for j in com:
                    com[count] = ('A' + "{:04d}".format(j))
                    count = count + 1
                ed = 0
                for row in range(0, 119772):
                    if (df_edges.iloc[row][0] in com) & (df_edges.iloc[row][1] in com):
                        ed = ed + 1
                        a = df_edges.iloc[row][0]
                        a1 = re.findall('\d+', a)
                        a11 = int(a1[0])

                        b = df_edges.iloc[row][1]
                        b1 = re.findall('\d+', b)
                        b11 = int(b1[0])
                        f.add_edge(a11, b11)
                Node.append(len(com))
                Edges.append(ed)
                x = nx.diameter(f)
                Dia.append(x)
                n = n + 1

        df_Q5 = pd.DataFrame({'a': Node, 'b': Edges, 'c': Dia})
        df_Q5.sort_values(['a', 'b'], ascending=[True, True], inplace=True)
        df_Q5.to_csv('graph-components.csv', index=False, header=False)

g = Graph(4605)

for row in range(0, 119772):
    a = df_edges.iloc[row][0]
    a1 = re.findall('\d+', a)
    a = int(a1[0])

    b = df_edges.iloc[row][1]
    b1 = re.findall('\d+', b)
    b = int(b1[0])

    g.addEdge(a, b)

g.SCC()
g.cpy()
