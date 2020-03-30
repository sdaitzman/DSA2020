#!/usr/bin/env python3
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

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
    for e in graph.nodes(data=True):
        node = graph.nodes[e[0]]

        # if we haven't seen this component yet, mark it as visited and descend
        if not node['visited']:
            node['visited'] = True
            components += 1
            remaining = [e[0]] # stack for DFS
            while remaining:
                current_node = remaining.pop()
                for adjacent in graph.neighbors(current_node):
                    if not graph.nodes[adjacent]['visited']:
                        graph.nodes[adjacent]['visited'] = True
                        remaining.append(adjacent)
    return components

def test_count_components():
    ''' Tests the count_components function '''
    G = nx.Graph()

    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)
    G.add_node(5)
    G.add_node(6)

    # component 1:
    G.add_edge(1,2)

    # component 2:
    G.add_edge(3,4)
    G.add_edge(4,5)
    G.add_edge(5,3)

    # component 3:
    # node 6 is alone :'(

    # check the count is correct
    assert count_components(G) == 3

    # check that we visited all nodes
    for e in G.nodes(data=True): assert e[1]['visited'] == True

def make_graph(n,p):
    ''' Make a random binomial graph with n nodes, p chance of edges '''
    graph = nx.Graph()
    for i in range(n): graph.add_node(i)

    # iterate through all pairings, but don't repeat
    for i in range(graph.number_of_nodes()):
        for j in range(i+1, graph.number_of_nodes()):
            if np.random.uniform() < p:
                graph.add_edge(i,j)
    components = count_components(graph)
    return (graph, components)

def random_binomial_plot():
    ''' Plots random binomial graph behavior '''
    n_val = []
    min_p = []

    # iterate through each number of nodes, building out data
    for n in range(5,51):
        n_val.append(n)
        min_p_trials = []
        for i in range(10): # try each n repeatedly and take average
            p = 0.01
            components = None
            while components != 1:
                graph, components = make_graph(n,p)
                # print(graph.nodes, graph.edges)
                p += 0.01
            min_p_trials.append(p)
        min_p.append(np.mean(min_p_trials))

    plt.plot(n_val, min_p, '.')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Minimum Connection Probability For Single Component')
    plt.title('Random Binomial Graph Connectedness Behavior')
    # plt.show()
    plt.savefig('random_binomial_graph.png', dpi=150)


random_binomial_plot()

