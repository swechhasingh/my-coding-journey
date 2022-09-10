from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        word_set = set(wordList)
        queue.append(beginWord)
        # word_set.remove(beginWord)
        level = 0
        
        # if endWord not in word_set:
        
        # BFS traversal of the word graph
        while queue:
            level += 1
            length = len(queue)
            for i in range(length):
                curr = queue.popleft()
                if curr == endWord:
                    return level
                neighbours = self.findNeighbours(curr)
                for word in neighbours:
                    if word in word_set:
                        word_set.remove(word)
                        queue.append(word)
        return 0
    
    def findNeighbours(self, word):
        # time complexity: O(M*26)
        neighbour_nodes = []
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        
        for i in range(len(word)):
            word_chars = list(word)
            for char in alphabet:
                word_chars[i] = char
                neighbour_nodes.append("".join(word_chars))
        return neighbour_nodes
        