from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Time complexity: O(N^2)
        # Space complexity: O(N)
        source_to_destination = dict()
        for path in paths:
            source_to_destination[path[0]] = path[1]
        destination_city = None
        ### first solution ###
        # for s, d in source_to_destination.items():
        #     while d in source_to_destination:
        #         d = source_to_destination[d]
        #     if destination_city == None:
        #         destination_city = d
        #     elif destination_city != d:
        #         return None
        ### second solution ###
        for s, d in source_to_destination.items():
            slow, fast = s, s
            while fast in source_to_destination and source_to_destination[fast] in source_to_destination:
                slow = source_to_destination[slow]
                fast = source_to_destination[source_to_destination[fast]]
                if slow == fast:
                    return "Loop exits!"
            destination_city = fast if fast not in source_to_destination else source_to_destination[fast]
        return destination_city

def main():
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"],["Sao Paulo","Lima"]]
    solution = Solution()
    print(f"Destination city: {solution.destCity(paths)}")
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    print(f"Destination city: {solution.destCity(paths)}")
    paths = [["B","C"],["D","B"],["C","A"]]
    print(f"Destination city: {solution.destCity(paths)}")


main()