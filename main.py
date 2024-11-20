import os
ascii_table = {chr(i): i for i in range(256)}

class CompactTrieNode:
    def __init__(self, end):
        self.children = {}
        self.end = end

class CompactTrie:
    def __init__(self):
        self.root = CompactTrieNode(True)

    def insert(self, key):
        # if self.root.children == {}:
        #     self.root.children[word] = CompactTrieNode()
        #     self.root.children[word].end = True
        #     return 
        
        # current = self.root.children
        # for key in current:
        #     common = os.path.commonprefix([key, word])
        #     if common:
        #         if current[key].end == True:
        #             if current[key].children == {}:
        #                 current.pop(common)
        #                 current[word] = CompactTrieNode()
        #                 current[word].end = True
        #                 break
        #             else:
        #                 ...
        #     return
        current = self.root
        while True:
            # Busca um prefixo que coincide parcialmente com a chave, se existir
            found_prefix = None
            for prefix in current.children:
                common_len = len(os.path.commonprefix([prefix, key]))
                if common_len > 0:
                    found_prefix = prefix
                    break

            if found_prefix is None:
                # Nenhum prefixo em comum: cria um novo nó folha com a chave
                current.children[key] = CompactTrieNode(end=True)
                self.compact_tree(self.root)
                return

            common_len = len(os.path.commonprefix([found_prefix, key]))
            common_prefix = found_prefix[:common_len]

            if common_len == len(found_prefix):
                # O prefixo encontrado é completamente igual ao início da chave
                if common_len == len(key):
                    # A chave já está na árvore, então não precisa inseri-la novamente
                    current.children[found_prefix].end = True
                    return
                else:
                    # Avança para o próximo nó e reduz a chave restante
                    key = key[common_len:]
                    current = current.children[found_prefix]
            else:
                # O prefixo encontrado precisa ser dividido
                remaining_prefix = found_prefix[common_len:]
                new_internal_node = CompactTrieNode()

                # Move o nó existente para ser filho do novo nó interno
                new_internal_node.children[remaining_prefix] = current.children.pop(found_prefix)
                
                # Insere o novo nó interno na árvore
                current.children[common_prefix] = new_internal_node
                
                # Insere a parte restante da chave como um novo nó folha
                key_suffix = key[common_len:]
                new_internal_node.children[key_suffix] = CompactTrieNode(end=True)
                self.compact_tree(self.root)
                return
    
    def common_prefix_length(s1, s2):
        length = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                break
            length += 1
        return length

    def search(self, word):
        node = self.root
        while word:
            found = False
            for key in node.children.keys():
                if word.startswith(key):
                    word = word[len(key):]
                    node = node.children[key]
                    found = True
                    break
            if not found:
                return False
        return node.end

    def remove(self, word):
        if not self.search(word):
            return False

        def _remove(node, word):
            if not word:
                if node.end:
                    node.end = False
                return len(node.children) == 0

            for key in node.children.keys():
                if word.startswith(key):
                    remaining_word = word[len(key):]
                    child_node = node.children[key]
                    if _remove(child_node, remaining_word):
                        del node.children[key]
                        return not node.end and len(node.children) == 0
            return False

        _remove(self.root, word)
        return True

    def compact_tree(self, node):
        # Compacta a árvore removendo nós intermediários sem ramificações
        for prefix in list(node.children):
            child = node.children[prefix]
            if len(child.children) == 1 and not child.end:
                # Compacta o nó se ele tem apenas um filho e não é um nó folha
                sub_prefix, sub_node = next(iter(child.children.items()))
                node.children[prefix + sub_prefix] = sub_node
                del node.children[prefix]
            # Recursivamente compacta os filhos
            self.compact_tree(child)

# ENCODER

origin = "origin.txt"
destination = "destination.txt"
compact_tree = CompactTrie()

with open(origin, "r") as origem, open(destination, "w") as destino:
    text = origem.read()
    string = text[0]
    compact_tree.insert(string)
    
    for i in range(1, len(text)):
        symbol = text[i]
        find = compact_tree.search(string + symbol)
        if find:
            string = string + symbol
        else:
            destino.write(str(ascii_table[string]))
            ascii_table[string + symbol] = len(ascii_table)
            compact_tree.insert(string + symbol)
            string = symbol
    destino.write(str(ascii_table[string]))