class Solution(object):
    class Node(object):
        def __init__(self):
            self.children = {}
            self.suggestions = []

    def __init__(self):
        self.root = self.Node()

    def insert(self, product):
        node = self.root

        for letter in product:
            if letter not in node.children:
                node.children[letter] = self.Node()
            node = node.children[letter]

            node.suggestions.append(product)
            node.suggestions.sort()
            if len(node.suggestions) > 3:
                node.suggestions.pop()

    def suggestedProducts(self, products, searchWord):
        for product in products:
            self.insert(product)

        result = []

        node = self.root
        for char in searchWord:
            if char not in node.children:
                result.append([])
                break

            result.append(node.children[char].suggestions)
            node = node.children[char]

        result_len = len(result)
        search_word_len = len(searchWord)
        if result_len < search_word_len:
            result.extend([[] for _ in range(search_word_len - result_len)])

        return result
