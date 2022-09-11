from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        deq = collections.deque()
        bank = set(wordList)
        deq.append(beginWord)
        count = 0
        n = len(beginWord)
        while deq:
            for _ in range(len(deq)):
                cur_word = deq.popleft()
                if cur_word == endWord:
                    return count + 1
                for i in range(n):
                    for ch in [chr(ord('a') + i) for i in range(26)]:
                        new_word = f'{cur_word[:i]}{ch}{cur_word[i + 1:]}'
                        if new_word in bank:
                            deq.append(new_word)
                            bank.discard(new_word)
            count += 1
        return 0
        
#         if endWord not in wordList:
#             return 0
        
#         queue = deque()
#         visited = set()
        
#         queue.append(beginWord)
#         visited.add(beginWord)
#         alphabet = list("abcdefghijklmnopqrstuvwxyz")
#         # adj_list = self.findNeighbours(wordList+[beginWord])
#         level = 1
#         # BFS traversal of the word graph
#         while queue:
#             for i in range(len(queue)):
#                 curr = queue.popleft()
#                 if curr == endWord:
#                     return level
#                 for i in range(len(curr)):
#                     for char in alphabet:
#                         new_word = curr[:i]+char+ curr[i+1:]
#                         if new_word not in visited and new_word in wordList:
#                             queue.append(new_word)
#                             visited.add(new_word)
#             level += 1
#         return 0
    
    