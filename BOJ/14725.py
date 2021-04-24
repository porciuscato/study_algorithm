def structure_print(dict_data, depth):
    keys = [k for k in dict_data.keys()]
    if len(keys) > 0:
        keys.sort()
        for key in keys:
            s_print(f"{'--' * depth}{key}\n")
            structure_print(dict_data[key], depth + 1)


if __name__ == "__main__":
    import sys

    s_input = sys.stdin.readline
    s_print = sys.stdout.write

    N = int(s_input())
    trie = {}
    for _ in range(N):
        input_data = list(s_input().split())
        length = int(input_data[0])
        data = input_data[1:]
        node = trie
        for i in range(length):
            if not node.get(data[i]):
                node[data[i]] = {}
            node = node[data[i]]
    structure_print(trie, 0)
