from num9_func import calc_dist
from num9_func import Graph
import pytest

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


def test_normal_false():
    assert calc_dist("Осинники", "Междуреченск", graph) == False


def test_wrong_data():
    with pytest.raises(AttributeError):
        calc_dist("abs", "asd", graph)


def test_wrong_graph():
    graph_2 = Graph()
    with pytest.raises(AttributeError):
        calc_dist("Осинники", "Междуреченск", graph_2)


def test_normal_true():
    assert calc_dist("Киселевск", "Красноярск", graph) == "Киселевск(0) -> Прокопьевск(13) -> Белово(99) -> Красноярск(750)"


def test_equal_sity():
    with pytest.raises(KeyError):
        calc_dist("Киселевск", "Киселевск", graph)