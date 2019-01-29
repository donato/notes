"""
Given an array of objects with a known set of properties,
implement a function that finds all possible partial matches
(one object's property value matches the same property on another object),
and produce a results object that describes those matches in any format you want.

"""
from collections import namedtuple, defaultdict

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



def bfs(v):

    queue = [v]

    while queue:
        next = queue.pop(0)
        if next.visited:
            continue

        # Do work
        print(next.obj)
        next.visited = True

        # Enqueue neighbors
        queue = queue + next.edges



d0 = Vertice(0)
d1 = Vertice(1)
d2 = Vertice(2)
d3 = Vertice(3)

d0.edges = [d2, d3]
d3.edges = [d1, d2]


bfs(d0)

tcpdump -i any -p -s 0 -w /sdcard/capture.pcap


ls -al /data/data/com.aniplex.fategrandorder.en/files/
rm /data/data/com.aniplex.fategrandorder.en/files/*.dat
rm /data/data/com.aniplex.fategrandorder.en/shared_prefs/com.aniplex.fategrandorder.en.v2.playerprefs.xml
rm /data/data/com.aniplex.fategrandorder.en/files/MasterDataCaches/*.dat
