from collections import deque

class Solution: 
  def ladderlength(self, beginWord, endWord, wordList):
    if endWord not in wordList:
      return 0
    
    queue = deque()
    queue.append((beginWord,1))
    print(f"Initial queue: {queue}")

    while queue:
      word, level = queue.popleft()

      for i in range(len(word)):
        for c in 'abcdefghijklmnopqrstuvwxyz':
          newWord = word[:i] + c + word[i+1:]

          if newWord == endWord:
            return level +1
          
          if newWord in wordList:
            wordList.remove(newWord)
            queue.append((newWord, level + 1))
            print(f"Added new word '{newWord}' at level {level + 1}, queue now: {queue}")
    return 0
  



beginWord = "hit"
endword = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Result = Solution()
Word_Ladder = Result.ladderlength(beginWord, endword, wordList)
print(f"Length of the shortest transformation sequence: {Word_Ladder}")
