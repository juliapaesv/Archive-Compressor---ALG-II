class TrieNode:
    def __init__(self):
        self.children = {}
        self.code = None 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string, code):
        node = self.root
        for char in string:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.code = code

    def search(self, string):
        node = self.root
        for char in string:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.code

    def delete(self, string):
        def _delete(node, string, depth):
            if depth == len(string):
                if node.code is not None:
                    node.code = None
                return len(node.children) == 0  # caso o nó seja vazio, é deletado
            char = string[depth]
            if char in node.children and _delete(node.children[char], string, depth + 1):
                del node.children[char]
                return len(node.children) == 0
            return False

        _delete(self.root, string, 0)
