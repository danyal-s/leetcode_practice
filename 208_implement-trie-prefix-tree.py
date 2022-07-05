# https://leetcode.com/problems/implement-trie-prefix-tree/
class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.is_last = False


class Trie:
    
    def __init__(self):
        self.head = Node()
        

    def insert(self, word: str) -> None:
        cur_node = self.head

        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = Node(c)
            
            cur_node = cur_node.children[c]
        
        cur_node.is_last = True


    def _find_node(self, word: str) -> Node:
        cur_node = self.head
        for c in word:
            if c in cur_node.children:
                cur_node = cur_node.children[c]
            else:
                return None
        
        return cur_node


    def search(self, word: str) -> bool:
        found = self._find_node(word)
        return found.is_last if found else False


    def startsWith(self, prefix: str) -> bool:
        found = self._find_node(prefix)
        return True if found else False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
