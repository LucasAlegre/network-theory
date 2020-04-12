#%%
from igraph import *
import matplotlib.pyplot as plt
import random
random.seed(7)


def set_color_from_communities(g, communities):
    pal = drawing.colors.ClusterColoringPalette(len(communities))
    g.vs['color'] = pal.get_many(communities.membership)

def plot_big_graph(g):
    visual_style = {}
    visual_style["bbox"] = (3000,2000)
    visual_style["edge_width"] = .25
    visual_style["edge_arrow_size"] = .25
    visual_style["vertex_size"] = 20
    visual_style["vertex_label_size"] = 8
    visual_style["edge_curved"] = False
    visual_style["vertex_label"] = g.vs['name']
    visual_style["layout"] = g.layout_fruchterman_reingold(weights=g.es["weight"], niter=10000, grid='nogrid')
    return plot(g, **visual_style)


g = Graph.Read_GraphML('karate.graphml')

#If None, the dendrogram is cut at the level which maximizes the modularity when the graph is unweighted; otherwise the dendrogram is cut at at a single cluster (because cluster count selection based on modularities does not make sense for this method if not all the weights are equal).
""" communities = g.community_edge_betweenness(directed=False, weights='weight').as_clustering(2)
set_color_from_communities(g, communities)
plot(g, vertex_label=g.vs['name']).save('karate_edgbetw.png')

communities = g.community_fastgreedy(weights='weight').as_clustering()
set_color_from_communities(g, communities)
plot(g, vertex_label=g.vs['name']).save('karate_fastgreedy.png')

communities = g.community_multilevel(weights='weight')
set_color_from_communities(g, communities)
plot(g, vertex_label=g.vs['name']).save('karate_multilevel.png')

communities = g.community_leading_eigenvector(weights='weight')
set_color_from_communities(g, communities)
plot(g, vertex_label=g.vs['name']).save('karate_eigenvector.png')

communities = g.community_label_propagation(weights='weight')
set_color_from_communities(g, communities)
plot(g, vertex_label=g.vs['name']).save('karate_labelprop.png')

communities = g.community_spinglass(weights='weight')
set_color_from_communities(g, communities)
plot(g, vertex_label=g.vs['name']).save('karate_spinglass.png')

communities = g.community_walktrap(steps=4, weights='weight').as_clustering()
set_color_from_communities(g, communities)
plot(g, vertex_label=g.vs['name']).save('karate_walktrap.png')


g = Graph.Read_Ncol('matta.txt', directed=False)

communities = g.community_edge_betweenness(directed=False).as_clustering()
set_color_from_communities(g, communities)
plot(g, vertex_label=g.vs['name']).save('matta_edgbetw.png')

communities = g.community_fastgreedy().as_clustering()
set_color_from_communities(g, communities)
plot(g, vertex_label=g.vs['name']).save('matta_fastgreedy.png')

communities = g.community_multilevel()
set_color_from_communities(g, communities)
plot(g, vertex_label=g.vs['name']).save('matta_multilevel.png')

communities = g.community_leading_eigenvector()
set_color_from_communities(g, communities)
plot(g, vertex_label=g.vs['name']).save('matta_eigenvector.png')

communities = g.community_label_propagation()
set_color_from_communities(g, communities)
plot(g, vertex_label=g.vs['name']).save('matta_labelprop.png')

communities = g.community_spinglass()
set_color_from_communities(g, communities)
plot(g, vertex_label=g.vs['name']).save('matta_spinglass.png')

communities = g.community_walktrap(steps=4).as_clustering()
set_color_from_communities(g, communities)
plot(g, vertex_label=g.vs['name']).save('matta_walktrap.png') """


g = Graph.Read_GraphML('enron')
summary(g)
g.vs['name'] = g.vs['Name']; del g.vs["Name"]
g.es['weight'] = [1 for _ in g.es.indices]
g.simplify(multiple=True, loops=False, combine_edges=dict(weight="sum"))
maxw = max(g.es['weight'])
g.es['weight'] = [10*e/maxw for e in g.es['weight']]

""" communities = g.community_edge_betweenness(clusters=5, directed=True, weights='weight').as_clustering()
set_color_from_communities(g, communities)
plot_big_graph(g).save('enron_edgbetw.png')

communities = g.community_label_propagation(weights='weight')
set_color_from_communities(g, communities)
plot_big_graph(g).save('enron_labelprop.png') """

giant = g.clusters().giant()
communities = giant.community_spinglass(weights='weight', spins=5)
set_color_from_communities(giant, communities)
plot_big_graph(giant).save('enron_spinglass.png')

communities = g.community_walktrap(steps=5, weights='weight').as_clustering()
set_color_from_communities(g, communities)
plot_big_graph(g).save('enron_walktrap.png')
