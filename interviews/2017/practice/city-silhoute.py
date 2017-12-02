# Challenge: Given a collection of Building objects, find the largest rectangle that can be found in their silhoutetes.
#   A building is defined by two x values and a height.
from collections import namedtuple
from recordclass import recordclass

Building = namedtuple('Building', ['left', 'right', 'height'])

"""
# Motivating examples
1. Complete Overlapping
2. Partial overlapping
3. Totally separate

          33333333
          33333333
    11111133333333
222222222222223333
222222222222223333
0...1...2...3...4...5...6
        L3------R3
L2----------R2
    L1--R1

"""
test_buildings = [
    Building(1, 2, 3),
    Building(0, 3, 2),
    Building(3, 4, 5)
]

"""
# Strategy
Moving from the left to the right of the sky scrape, every newly found L value begins a new "potentially largest" rectangle.
Moving from the left to the right each newly found R value "may" mark the end of a "potentially largest" rectangle,
    if-and-only-if the height of the rectangle under test is greater than that of all "active" rectangles

When moving from left to right we want easy access to
1. All "potentially largest" squares found thus far -> name this CandidateRectangles
2. An easy way to "disable" all CandidateRectangle above a certain height
    * When disabling you want to check the size of each one and potentially update the largest Candidate
3. The current max height of all Candidate rectangles
    And when turning off an "active"
4. The largest Candidate found thus far -> whether active or not
"""



# Algorithm
Point = namedtuple('Point', ['type', 'location', 'Building'])

class Candidate(recordclass('Candidate', ['left', 'right', 'height'])):
    def get_size(self):
        return (self.right - self.left) * self.height


class CandidateRectangles:
    candidate_list = []
    active_buildings = set()
    current_max_height = 0
    current_best_candidate = Candidate(0,0,0)

    def add(self, building):
        new_candidate = Candidate(left=building.left, right=None, height=building.height)
        self.candidate_list.append(new_candidate)
        self.active_buildings.add(building)

    def end(self, building):
        self.active_buildings.remove(building)
        new_max_height = self._get_max_height()
        # If increasing in size, we can't kill any candidates, so only do so when decreasing
        if new_max_height < self.current_max_height:
            self._update_candidate_list(new_max_height, building.right)
        self.current_max_height = new_max_height

    def _update_candidate_list(self, new_height, location):
        for candidate in self.candidate_list:
            if candidate.height > new_height:
                candidate.right = location
                self.candidate_list.remove(candidate)
                if candidate.get_size() > self.current_best_candidate.get_size():
                    self.current_best_candidate = candidate

    def _get_max_height(self):
        # Keeping candidates sorted may help here
        max_h = 0
        for building in self.active_buildings:
            max_h = max(building.height, max_h)
        return max_h

    def get_largest_rect(self):
        return self.current_best_candidate






def get_loc(point):
    # For ties, we want to sort by Type (start then end), then X (asc) then height desc
    type_priority = 0 if point.type == 'start' else 1
    location_priority = point.location
    height_priority = -1 * point.Building.height

    return tuple((type_priority, location_priority, height_priority))

def algo(buildings):
    all_points = []
    for b in buildings:
        all_points.append(Point('start', b.left, b))
        all_points.append(Point('end', b.right, b))

    # For ties, we want to sort by Type (start then end), then X (asc) then height desc
    sorted_points = sorted(all_points, key=get_loc)

    candidates = CandidateRectangles()
    for point in sorted_points:
        if point.type == 'start':
            candidates.add(point.Building)
        else:
            candidates.end(point.Building)

    rect = candidates.get_largest_rect()
    print("Left %s, Right %s, Height %s, Size %s" % (rect.left, rect.right, rect.height, rect.get_size()))




algo(test_buildings)