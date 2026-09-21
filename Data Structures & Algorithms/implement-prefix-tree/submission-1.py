class TrieNode:
    def __init__(self):
        self.chars = {}
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.chars:
                curr.chars[char] = TrieNode()
            curr = curr.chars[char]
        curr.isEnd = True 

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.chars:
                print(char)
                return False
            curr = curr.chars[char]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.chars:
                return False
            curr = curr.chars[char]
        return True
        
        