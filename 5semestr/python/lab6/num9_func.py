import pytest



class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n) -> Vertex:
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        '''f - from t - to'''
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


#  вариант 5

def calc_dist(n1: str, n2: str, graph: Graph):
    start = graph.getVertex(n1)
    finish = graph.getVertex(n2)

    unvisited = {node: float("inf") for node in graph}
    visited = {}
    best_parents = {node: None for node in graph}
    unvisited[start] = 0


    while unvisited:
        min_vertex = min(unvisited, key=unvisited.get)

        for neighbour, distance in min_vertex.connectedTo.items():
            if neighbour not in unvisited:
                continue
            newDistance = unvisited[min_vertex] + distance
            if unvisited[neighbour] == float("inf") or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
                best_parents[neighbour] = min_vertex

        visited[min_vertex] = unvisited[min_vertex]
        del unvisited[min_vertex]
        if not unvisited or min_vertex == finish:
            break

    if visited[finish] == float("inf"):
        #print(f"Пути между городами {start.getId()} и {finish.getId()} нет")
        return False

    path = [finish]
    cost = [visited[finish]]
    while True:
        key = best_parents[path[0]]
        path.insert(0, key)
        cost.insert(0, visited[path[0]])
        if key == start:
            break
    
    res = f""

    for p, c in zip(path[:-1], cost[:-1]):
        res += f"{p.getId()}({c}) -> "
        #print(f"{p.getId()}({c}) -> ", end="")

    res += f"{path[-1].getId()}({cost[-1]})"
    #print(f"{path[-1].getId()}({cost[-1]})")
    print(res)
    return res


if __name__ == "__main__":
    graph = Graph()
    data = '''
    Киселевск, Таштагол, 215, 
    Киселевск, Прокопьевск, 13, 
    Прокопьевск, Междуреченск, 116, 
    Прокопьевск, Белово, 86, 
    Осинники, Красноярск, 778, 
    Таштагол, Осинники, 148, 
    Таштагол, Красноярск, 905, 
    Таштагол, Междуреченск, 234, 
    Междуреченск, Красноярск, 829, 
    Белово, Междуреченск, 189, 
    Белово, Красноярск, 651
    '''
    data = [i.strip() for i in data.strip().split(", ")]
    data = [data[i:i + 3] for i in range(0, len(data), 3)]

    for i in data:
        graph.addEdge(i[0], i[1], int(i[2]))

    calc_dist("Осинники", "Междуреченск", graph)
    calc_dist("Киселевск", "Красноярск", graph)
    calc_dist("Киселевск", "Прокопьевск", graph)
    calc_dist("Киселевск", "Киселевск", graph)

