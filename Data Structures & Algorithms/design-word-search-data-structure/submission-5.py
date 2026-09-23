class TrieNode:
    def __init__(self):
        self.chars = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.chars:
                curr.chars[char] = TrieNode()
            curr = curr.chars[char]
        curr.isEnd = True
            

    def search(self, word: str) -> bool:
        return self.searchHelper(word, self.root, 0)
    
    def searchHelper(self, word, currNode, index):
        if index == len(word):
            return currNode.isEnd

        currChar = word[index]
        if currChar != "." and currChar not in currNode.chars:
            return False
        
        if word[index] != ".":
            return self.searchHelper(word, currNode.chars[currChar], index+1)
        
        for node in currNode.chars.values():
            res = self.searchHelper(word, node, index+1)
            if res:
                return res
        
        return False
        
