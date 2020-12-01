""" Find the Longest Path in a DAG """
import networkx as nx

def read_data(file_name):
    with open(file_name, 'r') as file:
        src = (file.readline().strip())
        sink = (file.readline().strip())
        edges = []
        line = " "
        try:
            while line != '':
                edge, weigth = file.readline().strip().split(":")
                node1, node2 = edge.split("->")
                edges.append(((node1),(node2), int(weigth)))
        except ValueError:
            pass

#    return src, sink, edges
        return edges

def calc_dist(graph, path):
    dist = 0
    for i in range(len(path)-1):
        dist += graph[path[i]][path[i+1]]['weight']

    return dist

def find_longest_path(src, sink, graph):
    paths = nx.all_simple_paths(graph, source=src, target=sink)
    longest_path = []
    max_dist = 0
    for path in paths:
        dist = calc_dist(graph, path)
        if dist > max_dist:
            max_dist = dist
            longest_path = path

    return max_dist, longest_path

if __name__ == "__main__":
    edges = read_data("F:/python prog/BioPython/longest_path_in_DAG.txt")
    print(edges)
    src, sink="a","g"
#     src, sink, edges = read_data("F:/python prog/BioPython/Lcs2.txt")
    graph = nx.DiGraph()
    for edge in edges:
        graph.add_edge(edge[0], edge[1], weight=edge[2])

    dist, path = find_longest_path(src, sink, graph)
    print (dist)
    print ("->".join([str(path[i]) for i in range(len(path))]))