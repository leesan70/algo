from heapq import *
from typing import List


class Node(object):
    def __init__(self, end_location: int, num_passengers: int):
        self.end_location = end_location
        self.num_passengers = num_passengers

    def __repr__(self):
        return f'"{self.end_location} : {self.num_passengers}"'

    def __lt__(self, other):
        return self.end_location < other.end_location

# O(NlogN) Solution with sorting and priority queue
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda node: node[1])
        first_trip = trips[0]
        hq = [Node(first_trip[2], first_trip[0])]
        total_passengers = first_trip[0]

        for trip in trips[1:]:
            num_passengers, start_location, end_location = trip
            total_passengers += num_passengers

            while hq:
                min_trip = hq[0]
                if min_trip.end_location <= start_location:
                    heappop(hq)
                    total_passengers -= min_trip.num_passengers
                else:
                    if total_passengers > capacity:
                        return False
                    else:
                        break
            heappush(hq, Node(trip[2], trip[0]))

        if total_passengers > capacity:
            return False
        return True

# O(N) solution with bucket sort
# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         timestamp = [0] * 1001
#         for trip in trips:
#             timestamp[trip[1]] += trip[0]
#             timestamp[trip[2]] -= trip[0]
#
#         used_capacity = 0
#         for passenger_change in timestamp:
#             used_capacity += passenger_change
#             if used_capacity > capacity:
#                 return False
#
#         return True