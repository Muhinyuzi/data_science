
# coding: utf-8

# In[24]:


import networkx as nx
G = nx.Graph()
G.add_edge('A','B')
G.add_edge('A','C')
G.add_edge('B','D')
G.add_edge('C','D')
G.add_edge('C','E')
G.add_edge('D','E')
G.add_edge('D','G')
G.add_edge('E','G')
G.add_edge('G','F')
G


# In[25]:


closeCent = nx.closeness_centrality(G)
closeCent['G']


# In[26]:


btwnCent = nx.betweenness_centrality(G,normalized=True,endpoints=False)
btwnCent['G']


# In[27]:


edge_btwnCent = nx.edge_betweenness_centrality(G,normalized=False)
edge_btwnCent[('G','F')]


# In[28]:


B = nx.DiGraph()
B.add_edge('A','B')
B.add_edge('A','B')
B.add_edge('A','C')
B.add_edge('C','D')
B.add_edge('D','C')
B


# In[29]:


pagerank_09 = nx.pagerank(G,alpha=0.8)
pagerank_09['D']


# In[42]:


C = nx.DiGraph()
C.add_edge('A','B')
C.add_edge('A','C')
C.add_edge('B','C')
C.add_edge('C','A')
C.add_edge('D','C')
C


# In[44]:




h,a = nx.hits(C, max_iter=100, normalized=True)
h['C'],a['C']


# In[ ]:




