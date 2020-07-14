def solve(position, depth):
    global answer
    if depth == K:
        answer = max(answer, int("".join(list(map(str, number)))))
    else:
        changed = False
        for i in range(position, length):
            if number[position] < number[i]:
                m_idx = position
                for j in range(position + 1, length):
                    if number[m_idx] < number[j]:
                        m_idx = j
                number[position], number[m_idx] = number[m_idx], number[position]
                changed = True
                solve(position + 1, depth + 1)
                break
        if not changed:
            if length == len(set(number)):
                number[-1], number[-2] = number[-2], number[-1]
            solve(position, depth + 1)


def main():
    if length == 1 or (length == 2 and number[1] == 0):
        return -1
    solve(0, 0)
    return answer


if __name__ == '__main__':
    answer = 0
    number, K = input().split()
    K = int(K)
    number = list(map(int, list(number)))
    length = len(number)
    print(main())
