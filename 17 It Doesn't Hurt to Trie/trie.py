class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def search(self, word):
        current_node = self.root
        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                return None
        return current_node
    
    def insert(self, word):
        current_node = self.root
        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                new_node = TrieNode()
                current_node.children[char] = new_node
        current_node.children["*"] = None
    
    def collectAllWords(self, words, node = None, word = ""):
        current_node = node or self.root
        for key, child_node, in current_node.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collectAllWords(words, child_node, word + key)
        return words
    
    def autocomplete(self, prefix):
        current_node = self.search(prefix)
        if not current_node:
            return None
        return self.collectAllWords([], current_node)
    
    def print_keys(self, node):
        current_node = node or self.root
        for key, child_node in current_node.children.items():
            print(key)
            if key != "*":
                self.print_keys(child_node)
    
    def autocorrect(self, word):
        current_node = self.root
        in_trie = ""
        for char in word:
            if current_node.children.get(char):
                in_trie += char
                current_node = current_node.children.get(char)
            else:
                return in_trie + self.collectAllWords([], current_node)[0]
        return word

