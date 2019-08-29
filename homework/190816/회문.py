for T in range(1,int(input())+1):
    N, M = map(int,input().split())
    board = [list(input()) for i in range(N)]
    result = 0
    x = 0
    point = True
    while point:
        idx = 0
        while idx <= N - M:
            start = idx
            end = idx + M - 1
            for i in range(int(M/2)):
                if board[x][start] == board[x][end]:
                    start += 1
                    end -= 1
                    continue
                else:
                    idx += 1
                    break
            else:
                result = board[x][start - int(M/2): end + int(M/2) + 1]
                point = False
                break
        if x < N - 1:
            x += 1
        else:
            break

    if result == 0:
        y = 0
        point = True
        while point:
            idx = 0
            while idx <= N - M:
                start = idx
                end = idx + M - 1
                for i in range(int(M/2)):
                    if board[start][y] == board[end][y]:
                        start += 1
                        end -= 1
                        continue
                    else:
                        idx += 1 
                        break
                else:
                    result = []
                    for word in range(start - int(M/2),end + int(M/2) + 1):
                        result.append(board[word][y])
                    point = False
                    break
            if y < N - 1:
                y += 1
            else:
                break
    
    print('#{} {}'.format(T,''.join(result)))
