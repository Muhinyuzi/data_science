def answer_four():
    degree = nx.betweenness_centrality(G1)
    max_node = None
    max_degree = -1
    for key, value in degree.items():
        if value > max_degree:
        max_degree = value
        max_node = key
    return max_node