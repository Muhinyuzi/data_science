G = nx.Graph()
G.add_edge('A','C')
G.add_edge('A','D')
G.add_edge('A','E')
G.add_edge('B','D')
G.add_edge('C','G')
G.add_edge('D','G')
G.add_edge('D','E')
G.add_edge('D','H')
G.add_edge('E','H')
G.add_edge('H','F')
common_neigh = [(e[0],e[1],len(list(nx.common_neighbors(G,e[0],e[1])))) for e in nx.non_edges(G)]
import operator
common_neigh = sorted(common_neigh,key=operator.itemgetter(2),reverse=True)
#print(common_neigh)
l= list(nx.jaccard_coefficient(G))
l.sort(key=operator.itemgetter(2),reverse=True)
#print(l)
al = list(nx.resource_allocation_index(G))
al.sort(key=operator.itemgetter(2),reverse=True)
#print(al)
pref_at = list(nx.preferential_attachment(G))
pref_at.sort(key=operator.itemgetter(2),reverse=True)
#print(pref_at)
G.node['A']['community']=0
G.node['B']['community']=0
G.node['C']['community']=0
G.node['D']['community']=0
G.node['G']['community']=0
G.node['E']['community']=1
G.node['F']['community']=1
G.node['H']['community']=1
com_neigh = list(nx.cn_soundarajan_hopcroft(G))
com_neigh.sort(key=operator.itemgetter(2),reverse=True)
#print(com_neigh)
ra_index = list(nx.ra_index_soundarajan_hopcroft(G))
ra_index.sort(key=operator.itemgetter(2),reverse=True)
print(ra_index)
