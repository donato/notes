"""
Given an array of objects with a known set of properties,
implement a function that finds all possible partial matches
(one object's property value matches the same property on another object),
and produce a results object that describes those matches in any format you want.

"""
from collections import namedtuple, defaultdict
import uuid

class obj:
    a = None
    b = None

Obj = namedtuple('Obj', ['a', 'b'])

class Vertice:
    obj = None
    edges = None
    mark = None
    visited = None

    def __init__(self, o):
        self.obj = o
        self.edges = []
        self.mark = None
        self.visited = False


def build_graph(obj_array, attributes):
    vertices = []

    for obj in obj_array:
        v = Vertice(obj)
        vertices.append(v)

    for index, attr in enumerate(attributes):
        map = {}
        for v in vertices:
            attr_value = v.obj[index]
            if attr_value in map:
                v.edges.append(map[attr_value])
                map[attr_value].edges.append(v)
            else:
                map[attr_value] = v


    for v in vertices:
        mark = uuid.uuid1()
        dfs(v, mark)

    clusters = defaultdict(list)
    for v in vertices:
        clusters[v.mark].append(v.obj)

    for c in clusters:
        print(clusters[c])



def dfs(v, mark):
    if v.visited:
        return

    v.visited = True
    v.mark = mark
    for neighbor in v.edges:
        dfs(neighbor, mark)



test_attributes = ['a', 'b']

z1 = Obj("Happy", "Cat")
z2 = Obj("Sad",   "Cat")
z3 = Obj("Happy", "Dog")
z4 = Obj("banana", "apple")
z5 = Obj("frozen", "apple")

test_input = [
    z1,z2, z3,z4,z5
]

build_graph(test_input, test_attributes)
