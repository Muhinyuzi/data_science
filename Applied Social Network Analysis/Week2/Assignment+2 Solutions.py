
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.2** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-social-network-analysis/resources/yPcBs) course resource._
# 
# ---

# # Assignment 2 - Network Connectivity
# 
# In this assignment you will go through the process of importing and analyzing an internal email communication network between employees of a mid-sized manufacturing company. 
# Each node represents an employee and each directed edge between two nodes represents an individual email. The left node represents the sender and the right node represents the recipient.

# ### Question 1
# 
# Using networkx, load up the directed multigraph from `email_network.txt`. Make sure the node names are strings.
# 
# *This function should return a directed multigraph networkx graph.*

# In[10]:


import networkx as nx

# This line must be commented out when submitting to the autograder
#!head email_network.txt


# In[11]:


def answer_one():
    
    # Your Code Here
    #df = pd.read_txt('email_network.txt')
    #df
    import pandas as pd
    df = pd.read_csv('email_network.txt', delimiter = "\t")  
    df = df.astype({'#Sender': str, 'Recipient': str})
    df
    senders_recipients = list(df['#Sender']) + list(df['Recipient'])
    edges = list(zip((df['#Sender']),(df['Recipient'])))
    #senders = set(df['#Sender'])
    #recipients = set(df['Recipient'])
    edges = set(edges)
    #G = nx.from_pandas_dataframe(df, '#Sender', 'Recipient', create_using=nx.MultiDiGraph())
    df['weight'] = df.groupby(['#Sender', 'Recipient'])['#Sender'].transform('size')
    G = nx.MultiDiGraph()
    for index, row in df.iterrows():
        G.add_edge(row['#Sender'],row['Recipient'],weight=row['weight'])

    #G = nx.from_pandas_dataframe(df, '#Sender', 'Recipient',edge_attr='weight',create_using=nx.DiGraph())
    
    return G#.edges(data=True)# Your Answer Here
#answer_one()


# ### Question 2
# 
# How many employees and emails are represented in the graph from Question 1?
# 
# *This function should return a tuple (#employees, #emails).*

# In[12]:


def answer_two():
    import pandas as pd
    df = pd.read_csv('email_network.txt', delimiter = "\t")  
    df = df.astype({'#Sender': str, 'Recipient': str})
    G = answer_one()
    print(type(G))
    emails = len(G.edges(data=True))
    senders_recipients = list(df['#Sender']) + list(df['Recipient'])
    employees = set(senders_recipients)
        
    # Your Code Here
    
    return len(employees),emails# Your Answer Here
#answer_two()


# ### Question 3
# 
# * Part 1. Assume that information in this company can only be exchanged through email.
# 
#     When an employee sends an email to another employee, a communication channel has been created, allowing the sender to provide information to the receiver, but not vice versa. 
# 
#     Based on the emails sent in the data, is it possible for information to go from every employee to every other employee?
# 
# 
# * Part 2. Now assume that a communication channel established by an email allows information to be exchanged both ways. 
# 
#     Based on the emails sent in the data, is it possible for information to go from every employee to every other employee?
# 
# 
# *This function should return a tuple of bools (part1, part2).*

# In[13]:


def answer_three():
        
    # Your Code Here
    G = answer_one()
    part1 = nx.is_strongly_connected(G)
    part2 = nx.is_weakly_connected(G)
    
    return part1,part2# Your Answer Here
#answer_three()


# ### Question 4
# 
# How many nodes are in the largest (in terms of nodes) weakly connected component?
# 
# *This function should return an int.*

# In[14]:


def answer_four():
        
    # Your Code Here
    G = answer_one()
    components = sorted(nx.weakly_connected_components(G))
    
    return G.number_of_nodes()# Your Answer Here
#answer_four()


# ### Question 5
# 
# How many nodes are in the largest (in terms of nodes) strongly connected component?
# 
# *This function should return an int*

# In[31]:


def answer_five():
        
    # Your Code Here
    G = answer_one()
    #components = sorted(nx.strongly_connected_components(G))
    #length = 0
    #for component in components:
        #if len(component) > length:
            #length = len(component)
    #a = {'d'}
    largest = max(nx.strongly_connected_components(G), key=len)
    return len(largest)# Your Answer Here
answer_five()


# ### Question 6
# 
# Using the NetworkX function strongly_connected_component_subgraphs, find the subgraph of nodes in a largest strongly connected component. 
# Call this graph G_sc.
# 
# *This function should return a networkx MultiDiGraph named G_sc.*

# In[32]:


def answer_six():
        
    # Your Code Here
    G = answer_one()
    #components = nx.strongly_connected_components(G)
    #length = answer_five()
    G_sc = max(nx.strongly_connected_component_subgraphs(G), key=len)
    #sub_components = nx.strongly_connected_component_subgraphs(set_1)
    return G_sc# Your Answer Here
#answer_six()


# ### Question 7
# 
# What is the average distance between nodes in G_sc?
# 
# *This function should return a float.*

# In[33]:


def answer_seven():
        
    # Your Code Here
    G_sc = answer_six()
    average = nx.average_shortest_path_length(G_sc)
    return average# Your Answer Here
#answer_seven()


# ### Question 8
# 
# What is the largest possible distance between two employees in G_sc?
# 
# *This function should return an int.*

# In[34]:


def answer_eight():
        
    # Your Code Here
    G_sc = answer_six()
    diameter = nx.diameter(G_sc)
    
    return diameter# Your Answer Here
#answer_eight()


# ### Question 9
# 
# What is the set of nodes in G_sc with eccentricity equal to the diameter?
# 
# *This function should return a set of the node(s).*

# In[60]:


def answer_nine():
       
    # Your Code Here
    G_sc = answer_six()
    periphery = nx.periphery(G_sc)
    return set(periphery)# Your Answer Here
#answer_nine()


# ### Question 10
# 
# What is the set of node(s) in G_sc with eccentricity equal to the radius?
# 
# *This function should return a set of the node(s).*

# In[62]:


def answer_ten():

    # Your Code Here
    G_sc = answer_six()
    center = nx.center(G_sc)
    
    return set(center)# Your Answer Here
#answer_ten()


# ### Question 11
# 
# Which node in G_sc is connected to the most other nodes by a shortest path of length equal to the diameter of G_sc?
# 
# How many nodes are connected to this node?
# 
# 
# *This function should return a tuple (name of node, number of satisfied connected nodes).*

# In[56]:


def answer_eleven():
        
    # Your Code Here
    G_sc = answer_six()
    diameter = nx.diameter(G_sc)
    nodes = answer_nine()
    peripheries = nx.periphery(G_sc)
    max_count = -1
    result_node = None
    for node in peripheries:
        count = 0
        sp = nx.shortest_path_length(G_sc, node)
        for key, value in sp.items():
            if value == diameter:
                count += 1        
        if count > max_count:
            result_node = node
            max_count = count
    
    return result_node, max_count    
    #target = None
    #for node in nodes:
        #target = [k for k,v in nx.shortest_path_length(G_sc, node).items() if v == diameter]
    #number_of_nodes = G_sc.degree[shortest]
    #return target#nx.shortest_path_length(G_sc,'38')#,number_of_nodes# Your Answer Here
#answer_eleven()


# ### Question 12
# 
# Suppose you want to prevent communication from flowing to the node that you found in the previous question from any node in the center of G_sc, what is the smallest number of nodes you would need to remove from the graph (you're not allowed to remove the node from the previous question or the center nodes)? 
# 
# *This function should return an integer.*

# In[57]:


def answer_twelve():
        
    # Your Code Here
    G_sc = answer_six()
    center = nx.center(G_sc)[0]
    node = answer_eleven()[0]
    return len(nx.minimum_node_cut(G_sc, center, node))
#answer_twelve()


# ### Question 13
# 
# Construct an undirected graph G_un using G_sc (you can ignore the attributes).
# 
# *This function should return a networkx Graph.*

# In[58]:


def answer_thirteen():
        
    # Your Code Here
    G_sc = answer_six()
    un_subgraph = G_sc.to_undirected()
    G_un = nx.Graph(un_subgraph)
    
    return G_un# Your Answer Here
#answer_thirteen()


# ### Question 14
# 
# What is the transitivity and average clustering coefficient of graph G_un?
# 
# *This function should return a tuple (transitivity, avg clustering).*

# In[59]:


def answer_fourteen():
        
    # Your Code Here
    B = answer_thirteen()
    
    return nx.transitivity(B), nx.average_clustering(B)# Your Answer Here
#answer_fourteen()


# In[ ]:




