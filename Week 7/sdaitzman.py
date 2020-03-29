#!/usr/bin/env python3
import networkx as nx

def count_components(graph):
    ''' Count the components in a graph. A component is a section of the graph
    that is isolated from other sections of the graph. This algorithm uses a
    depth-first search to seek out all sections of the component we're currently
    inside, then moves along to the next one.
    graph: a networkx graph
    '''
    # print(graph.nodes(), graph.edges(), graph.neighbors(1))

    components = 0

    # set all nodes to unvisited
    nx.set_node_attributes(graph, False, 'visited')

    # iterate through all nodes
    for i,e in enumerate(graph.nodes(data=True)):
        # i: index we're currently at
        # e: node we are currently at (tuple of label and attributes dict)

        # if we haven't seen this component yet
        node = graph.nodes[e[0]]
        node["foo"] = "bar"
        print(graph.nodes(data=True))

        if not e[1]['visited']:
            # print("Another one: ", e)
            components += 1
        


G = nx.Graph()
G.add_node(1) # adds node with label 1
G.add_node(2) # adds node with label 2
G.add_node(200) # adds node with label 2
G.add_edge(1,2) # adds an undirected edge between nodes 1 and 2
G.edges() # returns an iterator over all edges
G.nodes() # returns an iterator over all nodes
G.neighbors(1) # returns the neighbors of node 1
count_components(G)