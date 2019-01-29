"""
Skyline problem.

Given a collection of buildings, output the list of key points which define the skyline of the building
collection of buildings is already sorted by Li value

# A final key point will always be found when moving left to right when the "current_max_height" changes.
"""

import math

from collections import namedtuple, defaultdict
from heapq import heappush, heapify


Building = namedtuple('Building', ['Li', 'Ri', 'Hi'])
KeyPoint = namedtuple('KeyPoint', ['x', 'y'])



def get_critical_points(buildings):
    s = set()
    add_actions = defaultdict(set)
    end_actions = defaultdict(set)

    for b in buildings:
        s.add(b.Li)
        s.add(b.Ri)
        add_actions[b.Li].add(b)
        end_actions[b.Ri].add(b)

    critical_points = sorted(list(s))
    return critical_points, add_actions, end_actions

class ActiveRect:
    building = None

    def __init__(self, building):
        self.building = building

    def __lt__(self, other):
        # Note: To make this return high to low, we use > instead of <
        return self.building.Hi > other.building.Hi

def algo(buildings):
    # O(nlogn)
    points, adds, ends = get_critical_points(buildings)

    # While moving across track the set of active rects at a given point
    critical_points_max_height = defaultdict(set)
    active_rects_heap = []
    for p in points:
        for a in adds[p]:
            heappush(active_rects_heap, ActiveRect(a))
        # n
        for e in ends[p]:
            # n
            active_rects_heap = [a for a in active_rects_heap if a.building != e]
            # logn
            heapify(active_rects_heap)

        if len(active_rects_heap) > 0:
            critical_points_max_height[p] = active_rects_heap[0].building.Hi
        else:
            critical_points_max_height[p] = 0

    current_x = -1
    current_height = -1 * math.inf
    final_points = []
    for p in points:
        # When moving across points, only add it to the list if height changes
        p_height = critical_points_max_height[p]
        if current_x != p and current_height != p_height:
            final_points.append((p, p_height))
            current_x = p
            current_height = p_height

    print(final_points)


test_buildings = [
    Building(1,3,8),
    Building(5,8,5),
    Building(6,7,6),
    Building(6,8,4)
]

# [ (1, 8), (3, 0), (5, 5), (6,6), (7,5), (8, 0)

algo(test_buildings)
