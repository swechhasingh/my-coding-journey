from collections import deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        wordList = set(wordList)

        def bfs(beginWord, wordList):
            queue = deque([beginWord])
            # shortest distance from source to every node
            visited = {beginWord:0}
            parent = collections.defaultdict(set)
            
            alphabet = list("abcdefghijklmnopqrstuvwxyz")
            # BFS traversal of the word graph
            while queue:
                curr = queue.popleft()
                for i in range(len(curr)):
                    for char in alphabet:
                        neigh = curr[:i]+char+ curr[i+1:]
                        if neigh in wordList:
                            if neigh not in visited:
                                queue.append(neigh)
                                visited[neigh] = visited[curr]+1
                                parent[neigh].add(curr)
                            else:
                                # if visited[neigh] > visited[curr]+1:
                                #     parent[neigh] = set()
                                #     queue.append(neigh)
                                #     visited[neigh] = visited[curr]+1
                                #     parent[neigh].add(curr)
                                # el
                                if visited[neigh] == visited[curr]+1:
                                    parent[neigh].add(curr)
                                
            return parent
        
        parent = bfs(beginWord, wordList)
        
        # reconstruct path from s->e
        ladders = []
       
        def makeLadder(word, ladder):
            if word == beginWord:
                ladders.append(ladder[::-1])
            else:
                for p in parent[word]:
                    makeLadder(p, ladder+[p])
                    
        makeLadder(endWord, [endWord])
        return ladders
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    