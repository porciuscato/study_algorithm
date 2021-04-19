# 백준 글 참고: https://www.acmicpc.net/blog/view/9
# segment tree. 구간합을 구하기 좋은 자료구조.
# tree는 배열로도 구현이 가능하다. 그런데 tree로 만들 배열 크기는 어떻게 결정하는가?
# node 번호로 그 최대 구간을 알아낼 수 있다.


def get_max_node_number(left: int, right: int, node: int = 1) -> int:
    '''
    세그먼트 트리를 만들 때 tree의 최대 인덱스를 구하는 함수다.
    최종 return 값은 해당 트리의 최대 인덱스므로 tree 크기는 return 보다 큰 값으로 설정해야 한다.

    :param left: 배열의 좌측 인덱스
    :param right: 배열의 우측 인덱스
    :param node: 노드의 번호
    :return: node의 최대값을 반환 -> 트리의 크기는 node + 1로 설정하면 된다.
    '''
    if left == right:
        return node
    else:
        return max(get_max_node_number(left, (left + right) // 2, node * 2),
                   get_max_node_number((left + right) // 2 + 1, right, node * 2 + 1))


def tree_init(arr: list, tree: list, left: int, right: int, node: int = 1) -> int:
    '''
    세그먼트 트리를 초기화하는 함수다. left 부터 right 구간의 합을 저장한다.

    :param arr: 원본 배열
    :param tree: 구간합을 저장할 트리
    :param left: 좌측 인덱스
    :param right: 우측 인덱스
    :param node: 트리의 인덱스(노드 번호)
    :return: 구간합을 반환한다. 최종 return 은 배열의 총합이다.
    '''
    if left == right:
        tree[node] = arr[left]
        return tree[node]
    else:
        tree[node] = tree_init(arr, tree, left, (left + right) // 2, node * 2) + \
                     tree_init(arr, tree, (left + right) // 2 + 1, right, node * 2 + 1)
        return tree[node]


def get_subsum(tree: list, left: int, right: int, start: int, end: int, node: int = 1) -> int:
    '''
    세그먼트 트리로 정리된 값으로 구간합을 구할 수 있다.

    :param tree: 세그먼트 트리
    :param left: 구간의 좌측 인덱스
    :param right: 구간의 우측 인덱스
    :param start: 구할 구간합의 좌측 인덱스
    :param end: 구할 구간합의 우측 인덱스
    :param node: 해당 구간합의 위치
    :return: 구간합을 반환한다.
    '''
    if end < left or right < start:
        return 0
    elif start <= left and right <= end:
        return tree[node]
    else:
        return get_subsum(tree, left, (left + right) // 2, start, end, node * 2) + \
                get_subsum(tree, (left + right // 2 + 1), right, start, end, node * 2 + 1)


def update(tree: list, left: int, right: int, index: int, diff: int, node: int = 1) -> None:
    '''
    특정 index 의 값을 바꾸는 함수다.
    만약 특정 index의 값이 val 이라면 diff 는 다음과 같이 정의된다.
    diff = val - arr[index]
    이 변화량을 해당하는 인덱스의 모든 영역에 적용시켜야 한다.

    :param tree: 세그먼트 트리
    :param left: 구간의 좌측 인덱스
    :param right: 구간의 우측 인덱스
    :param index: 기존 arr 의 바꾸려는 인덱스 
    :param diff: 바꾸려는 값과 기존 값의 차이
    :param node: 현재 세그먼트 트리의 인덱스
    :return: 값만 바꿀 뿐 반환하지 않는다.
    '''
    if index < left or right < index:
        return
    tree[node] += diff
    if left != diff:
        update(tree, left, (left + right) // 2, index, diff, node * 2)
        update(tree, ((left + right) // 2 + 1), right, index, diff, node * 2 + 1)


if __name__ == '__main__':
    from random import randint

    CUSTOM_SIZE = 20
    arr = [randint(0, 100) for _ in range(CUSTOM_SIZE)]
    # arr = [1, 2, 3, 4, 5, 6, 7]
    size = get_max_node_number(0, len(arr) - 1)
    tree = [0] * (size + 1)
    result = tree_init(arr, tree, 0, len(arr) - 1)
    sub_sum = get_subsum(tree, 0, len(arr) - 1, 2, 5)

