from collections import deque
from graph import Graph


def person_is_seller(name):
    return name == 'anuj'


if __name__ == "__main__":

    graph2 = Graph()
    people = ["thom", "bob", "claire", "alice",
              "jonny", "anuj", "you", "peggy"]
    for name in people:
        graph2.addVertex(name)

    graph2.addEdge("you", "alice")
    graph2.addEdge("you", "bob")
    graph2.addEdge("you", "claire")

    graph2.addEdge("bob", "anuj")
    graph2.addEdge("bob", "peggy")

    graph2.addEdge("alice", "peggy")

    graph2.addEdge("claire", "thom")
    graph2.addEdge("claire", "jonny")

    for v in graph2:
        print(v)

    def search(name):
        search_queue = deque()
        search_queue += graph2.getVertex(name).getConnections()
        searched = set()
        while search_queue:
            person = search_queue.popleft().getId()
            if person not in searched:
                if person_is_seller(person):
                    print(f"{person = } is a mango seller!")
                    return True
                else:
                    print(f"{person = }")
                    search_queue += graph2.getVertex(person).getConnections()
                    searched.add(person)
        return False

    search("you")