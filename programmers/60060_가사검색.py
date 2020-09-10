from collections import deque


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
        cnt = 0
        current = self.head
        deq = deque([(current, -1)])
        length = len(word)
        current, layer = deq.popleft()
        for i in range(length):
            char = word[i]
            while layer == i - 1:
                if char == "?":
                    for child in current.children.values():
                        deq.append((child, i))
                else:
                    if char in current.children:
                        deq.append((current.children[char], i))
                try:
                    current, layer = deq.popleft()
                except:
                    return cnt
                if layer == length - 1:
                    cnt += 1
        while deq:
            if layer == length - 1:
                cnt += 1
            c, layer = deq.popleft()
        return cnt


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
