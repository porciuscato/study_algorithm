class Node:
    def __init__(self, letter=None):
        self.letter = letter
        self.children = {}
        self.count = 0

    def __repr__(self):
        return f"<{self.letter}>"


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        current = self.head
        for char in word:
            if char not in current.children:
                current.children[char] = Node(char)
            current.count += 1
            current = current.children[char]

    def search(self, word):
        current = self.head
        length = len(word)
        for i in range(length):
            char = word[i]
            if char == "?":
                return current.count
            else:
                if char in current.children:
                    current = current.children[char]
                else:
                    return 0


def solution(words, queries):
    tries = [Trie() for _ in range(10001)]
    tries_reverse = [Trie() for _ in range(10001)]
    answer = []
    for word in words:
        tries[len(word)].insert(word)
        tries_reverse[len(word)].insert(word[::-1])
    for query in queries:
        if query[0] == "?":
            answer.append(tries_reverse[len(query)].search(query[::-1]))
        else:
            answer.append(tries[len(query)].search(query))
    return answer


testcases = [
    (["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
]

for case in testcases:
    print(solution(*case))