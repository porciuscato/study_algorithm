class Node:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}

    def __repr__(self):
        return f"{self.letter} node"


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        current = self.head
        for char in word:
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]

    def search(self, word):
        current = self.head
        for char in word:
            if char not in current.children:
                return False
            else:
                current = current.children[char]
        return True


names = ['Joe', 'John', 'Johnny', 'Jane', 'Jack', "kakao", "kack"]
new_trie = Trie()
for n in names:
    new_trie.insert(n)

print(new_trie.search('aakac'))

