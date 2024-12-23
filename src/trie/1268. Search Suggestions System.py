from sortedcontainers import SortedDict


class Solution(object):
    class Node(object):
        def __init__(self):
            self.children = SortedDict()
            self.is_end = False

    def __init__(self):
        self.root = self.Node()
        self.output = 3
        self.count = 0

    def insert_products(self, products):
        for product in products:
            self.insert_product(product)

    def insert_product(self, product):
        node = self.root
        for char in product:
            if char not in node.children:
                node.children[char] = self.Node()
            node = node.children[char]
        node.is_end = True

    def suggest_products(self, search_word):
        result = []
        node = self.root
        prefix = []
        suggestions = []
        for char in search_word:
            if char in node.children:
                prefix.append(char)
                self.dfs(node.children[char], prefix, suggestions)
                result.append(suggestions)
                suggestions = []
                self.count = 0
                node = node.children[char]
            else:
                result.extend([[]] * (len(search_word) - len(result)))
                break
        return result

    def dfs(self, node, prefix, suggestions):
        if node.is_end:
            suggestions.append(''.join(prefix))
            self.count += 1
            if self.count == self.output:
                return
        for child in node.children:
            if self.count == self.output:
                break
            prefix.append(child)
            self.dfs(node.children[child], prefix, suggestions)
            prefix.pop()

    def suggestedProducts(self, products, searchWord):
        self.insert_products(products)
        return self.suggest_products(searchWord)


if __name__ == '__main__':
    Solution().suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse¬")
