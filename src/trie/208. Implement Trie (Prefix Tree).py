class TrieNode:

    def __init__(self):
        self.children = {}
        self.isTheEndOfWord = False  # notes if it's the end of a word


class Trie:

    def __init__(self):
        self.__root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.__root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isTheEndOfWord = True  # notes the end of the word

    def search(self, word: str) -> bool:
        node = self.__root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isTheEndOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.__root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
