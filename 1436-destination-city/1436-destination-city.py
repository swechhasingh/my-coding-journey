class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Time complexity: O(N^2)
        source_to_destination = dict()
        visited = dict()
        for path in paths:
            source_to_destination[path[0]] = path[1]
        destination_city = None
        for s, d in source_to_destination.items():
            if s in visited:
                continue
            visited[s] = True
            curr = d
            while curr in source_to_destination:
                visited[curr] = True
                curr = source_to_destination[curr]
            curr_destination_city = curr
            if destination_city == None:
                destination_city = curr_destination_city
            elif destination_city != curr_destination_city:
                return None
        return destination_city
            