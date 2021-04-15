class DisjointSet:
    '''Disjoint Set without Performance consideration
    
    성능을 고려하지 않고 set을 만든다.
    disjoint_set.py는 성능을 고려해 rank의 길이를 깊게 하지 않는다.
    이 로직은 알고리즘 문제 해결을 위해 준비하는 것으로 rank를 고려하지 않는다.
    parent 역시 set의 대표 노드로 바꾸지 않는다.
    '''

    def __init__(self, node_count: int):  # node_count: 노드의 갯수
        self.parent = [n for n in range(node_count)]

    def find_set(self, x):
        if x != self.parent[x]:
            return self.find_set(self.parent[x])
        return self.parent[x]

    # 두 집합을 하나로 합친다.
    def unite(self, x, y):
        self.parent[y] = x

    # 노드를 분리시킨다.
    def seperate(self, x):
        self.parent[x] = x


if __name__ == "__main__":
    disjoint = DisjointSet(5)
    disjoint.unite(0, 1)
    disjoint.unite(2, 3)
    disjoint.unite(1, 4)
    disjoint.seperate(3)
    print(disjoint.parent)
