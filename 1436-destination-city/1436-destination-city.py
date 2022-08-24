class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Time complexity: O(N^2)
        # Space complexity: O(N)
        source_to_destination = dict()
        for path in paths:
            source_to_destination[path[0]] = path[1]
        destination_city = None
        for s, d in source_to_destination.items():
            curr = d
            while curr in source_to_destination:
                curr = source_to_destination[curr]
            if destination_city == None:
                destination_city = curr
            elif destination_city != curr:
                return None
        return destination_city
            