from heapq import heappush, heappop


def dijkstra(start) -> int:
    left_sheeps = [-1 for _ in range(N)]

    que = [(-database[start][1], start)]
    left_sheeps[start] = database[start][1]

    while que:
        left_sheep, island = heappop(que)
        left_sheep = -left_sheep

        if left_sheep < left_sheeps[island]:
            continue
        for adj in islands[island]:
            if 'W' in database[adj]:
                mari = database[adj][1]
                new_left_sheep = 0 if left_sheep - mari <= 0 else left_sheep - mari
            else:
                new_left_sheep = left_sheep
            if new_left_sheep > left_sheeps[adj]:
                left_sheeps[adj] = new_left_sheep
                heappush(que, (-new_left_sheep, adj))
                if adj == 0:
                    return new_left_sheep


if __name__ == "__main__":
    import sys

    s_input = sys.stdin.readline
    s_print = sys.stdout.write

    N = int(s_input())
    islands = [[] for _ in range(N)]
    database = [[]]
    for i in range(1, N):
        in_data = list(s_input().split())
        typ = in_data[0]
        many = int(in_data[1])
        island_to = int(in_data[2]) - 1

        database.append([typ, many])
        islands[i].append(island_to)
        islands[island_to].append(i)

    answer = 0
    for i in range(1, N):
        if 'S' in database[i]:
            answer += dijkstra(i)

    s_print(f'{answer}\n')
