from graph import Graph


def print_conns(graph: Graph):
    for v in graph.getVertices():
        vert = graph.getVertex(v)
        print(vert)
    print()


def rev_graph(graph: Graph):
    new_g = Graph()
    for v in graph.getVertices():
        vert = graph.getVertex(v)
        for conn in vert.getConnections():
            new_g.addEdge(conn.id, vert.id)

    return new_g


if __name__ == "__main__":
    graph = Graph()
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(2, 1)
    graph.addEdge(1, 3)
    print("graph:")
    print_conns(graph)
    print("reversed graph:")
    print_conns(rev_graph(graph))