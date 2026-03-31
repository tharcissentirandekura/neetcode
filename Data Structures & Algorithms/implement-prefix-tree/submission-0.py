class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word #whether we reached end or not
    def startsWith(self, prefix: str) -> bool:
        # to check if the trie has a word starts with prefix
        curr = self.root
        for p in prefix:
            if p not in curr.children:
                return False
            curr = curr.children[p]
        return True
        