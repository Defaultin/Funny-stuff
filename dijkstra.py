from heapq import heappush, heappop
import networkx
import warnings
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    distance = {}
    queue = [(0, start)]
    
    while queue:
        weight, node = heappop(queue)
        if node in distance:
            continue

        distance[node] = weight
        for _, n, w in graph.edges(node, data=True):
            heappush(queue, (weight + w['weight'], n))
    
    return distance


def init_graph(G, vertex):
    '''[[edge1, edge2, weight], ...]'''
    graph = networkx.Graph()
    graph.add_nodes_from(range(vertex))
    for e1, e2, w in G:
        graph.add_edge(e1, e2, weight=w)

    return graph


def show_graph(graph):
    weights = [5 * e['weight'] / len(graph) for (u, v, e) in graph.edges(data=True)]
    plt.figure(figsize=(6, 6))
    plt.axis('off')
    layout = networkx.spring_layout(graph)
    networkx.draw_networkx_nodes(graph, layout, node_color='orange', node_size=300)
    networkx.draw_networkx_edges(graph, layout, edge_color='gray', width=weights)
    networkx.draw_networkx_labels(graph, layout, font_color='black')
    plt.show(layout)


def main():
    warnings.filterwarnings('ignore', category=UserWarning)
    graph = init_graph([
            [0, 1, 3], [0, 2, 2], [1, 3, 5], [1, 4, 2], 
            [1, 2, 1], [2, 3, 4], [2, 4, 1], [3, 5, 1], 
            [3, 7, 3], [4, 3, 5], [4, 5, 2], [5, 6, 2], 
            [5, 7, 6], [6, 7, 2]
        ], 8)
    print(dijkstra(graph, 0))
    show_graph(graph)


if __name__ == '__main__':
    main()