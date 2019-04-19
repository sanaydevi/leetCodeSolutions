"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

from collections import deque
class Solution:
    def __init__(self):
        self.d = {}

    def construct_dic(self, wordlist):
        for word in wordlist:
            for i in range(len(word)):
                key = word[:i] + '_' + word[i + 1:]
                if key not in self.d:
                    self.d[key] = [word]
                else:
                    self.d[key].append(word)

    def bfs_ladder(self,begin,end,wordlist):
        visited = []
        queue  = deque()
        queue.append((begin,1))

        while queue:
            word,step = queue.popleft()
            if word == end:
                return step
            if word not in visited:
                visited.append(word)
                for i in range(len(word)):
                    key = word[:i]+'_'+word[i+1:]
                    if key in self.d:
                        neigh = self.d[key]
                        for j in neigh:
                            if j not in visited:
                                if j not in queue:
                                    queue.append((j,step+1))
        return 0


    def ladderLength(self, begin, end, wordlist):
        self.construct_dic(set(wordlist))
        return self.bfs_ladder(begin,end,wordlist);
        #print(self.d)


if __name__ == "__main__":
    ob = Solution()
    res = ob.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    print(res)

"""
test cases:
1. "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
2. 'TOON', 'PLEA',['POON', 'PLEE', 'SAME', 'POIE', 'PLEA', 'PLIE', 'POIN']

"""