from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        queue = deque()
        visited = set()
        
        wordList = set(wordList)
        
        queue.append(beginWord)
        visited.add(beginWord)
        
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        level = 1
        # BFS traversal of the word graph
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == endWord:
                    return level
                for i in range(len(curr)):
                    for char in alphabet:
                        new_word = curr[:i]+char+ curr[i+1:]
                        if new_word in wordList and new_word not in visited:
                            queue.append(new_word)
                            visited.add(new_word)
            level += 1
        return 0
    
    