"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""
from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        answer_list = []
        for i in range(len(equations)):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1/values[i]))

        for i in range(len(queries)):
            query = queries[i]
            if query[0] not in graph or query[1] not in graph:
                answer_list.append(-1.0)
                continue
            answer_list.append(self.dijkstra(query[0], query[1], graph))

        return answer_list
    
    def dijkstra(self, start, end, graph):
        heap = [(1.0, start)]
        visited_set = set()
        while heap:
            answer, variable = heappop(heap)
            if variable == end:
                return answer

            for neighbor, value in graph[variable]:
                if neighbor not in visited_set:
                    visited_set.add(neighbor)
                    heappush(heap, (answer * value, neighbor))
        return -1.0

"""
Time Complexity: O(ElogV) E is total number of edges in graph and V is vertices 
Space Complexity: O(V)
"""