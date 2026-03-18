import networkx as nx

graph = nx.Graph()

def add_topic(topic):

    graph.add_node(topic)

def connect_topics(a,b):

    graph.add_edge(a,b)

def get_related(topic):

    if topic in graph:
        return list(graph.neighbors(topic))
    return []