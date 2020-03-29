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


