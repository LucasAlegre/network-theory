#%%
from igraph import *
import matplotlib.pyplot as plt
import seaborn as sns
import random
sns.set()
random.seed(7)


def plot_degree_distribution(g: Graph):
    plt.figure()
    plt.hist(g.degree())
    plt.xlabel("Degree")
    plt.ylabel("#Vertices")
    plt.show()

def global_metrics(g: Graph):
    summary(g)
    print("GLOBAL MEASUURES")
    print("Connected:", g.is_connected())
    print("Density:", g.density())
    print("Diameter:", g.diameter())
    print("Clustering Coefficient:", g.transitivity_undirected())
    print("Average Local Clustering Coefficient:", g.transitivity_avglocal_undirected())
    print("Average Degree:", mean(g.degree()))
    print("Max Degree:", g.maxdegree())
    print("Average Betweenness:", mean(g.betweenness()))
    print("Max Betweenness:", max(g.betweenness()))
    print("Average Closeness:", mean(g.closeness()))
    print("Max Closeness:", max(g.closeness()))

def local_metrics(g: Graph):
    if "name" not in g.vertex_attributes():
        g.vs["name"] = [str(i) for i in range(g.vcount())]
    degrees = g.degree()
    betweenness = g.betweenness()
    closeness = g.closeness()
    if not g.is_directed():
        clustering_coef = g.transitivity_local_undirected()
    print("LOCAL MEASURES")
    for i in range(g.vcount()):
        print(g.vs["name"][i] + ':')
        print(" Degree:", degrees[i])
        print(" Betweenness:", betweenness[i])
        print(" Closeness:", closeness[i])
        if not g.is_directed():
            print(" Clustering Coefficient:", clustering_coef[i])
    print("Vertex with highest degree:", g.vs.select(_degree = g.maxdegree())['name'])
    print("Vertex with highest betweenness:", g.vs.select(_betweenness = max(betweenness))['name'])
    print("Vertex with highest closeness:", g.vs.select(_closeness = max(closeness))['name'])
    if not g.is_directed():
        print("Vertex with highest clustering coefficient:", g.vs[clustering_coef.index(max(clustering_coef))]['name'])


#%%
""" g = Graph.Read_Ncol('matta.txt', directed=False)
global_metrics(g)
local_metrics(g)
plot_degree_distribution(g)

plot(g, layout=g.layout("fr"), vertex_label=g.vs['name'], vertex_frame_width=0) """

#%%
g = Graph.Read_GraphML('enron')
g.simplify()
g.vs['name'] = g.vs['Name']; del g.vs["Name"]

global_metrics(g)
local_metrics(g)
plot_degree_distribution(g)

colours = ['#fecc5c', '#a31a1c']
visual_style = {}
visual_style["bbox"] = (3000,2000)
visual_style["vertex_color"] = 'grey'
visual_style["edge_width"] = .25
visual_style["edge_arrow_size"] = .25
visual_style["vertex_size"] = 20
visual_style["vertex_label_size"] = 8
visual_style["edge_curved"] = False
visual_style["layout"] = g.layout("fr")
plot(g, vertex_frame_width=0, vertex_label=g.vs["name"], **visual_style)
