"""
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
The cheapest price from city 0 to city 2 with at most 1 stop costs 200
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
The cheapest price from city 0 to city 2 with at most 0 stop costs 500
Constraints:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""

from heapq import heappush, heappop
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        heap = []
        minimum_price = float("inf")
        for i in range(len(flights)):
            graph[flights[i][0]].append((flights[i][1],flights[i][2]))
        heappush(heap, (0, src, -1))
        while heap:
            price, city, number_of_stops = heappop(heap)
            if city == dst:
                return price
            if number_of_stops < K:
                for neighbor, cost in graph[city]:
                    heappush(heap, (price + cost, neighbor, number_of_stops + 1))
        return -1
 """
 Time Complexity: O(N^2 lgN)
 Space Complexity: O(N^2)
 """