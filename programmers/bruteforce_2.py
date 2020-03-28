def get_prime_list(n):
    numbers = [True] * n
    numbers[0], numbers[1] = False, False
    mx = int(n ** 0.5)
    for i in range(2, mx + 1):
        if numbers[i] == True:
            for j in range(i + i, n, i):
                numbers[j] = False
    return numbers


def permu(arr, depth, aim, total_length, numbers):
    global answer, visited, result
    if depth == aim:
        val = int(''.join(arr))
        if prime_list[val]:
            result.append(val)
    else:
        for i in range(total_length):
            if not visited[i]:
                ar = arr[:]
                ar.append(numbers[i])
                visited[i] = 1
                permu(ar, depth + 1, aim, total_length, numbers)
                visited[i] = 0

answer, visited, prime_list, result = 0, [], [], []

def solution(numbers):
    global answer, visited, prime_list, result
    answer = 0
    prime_list = get_prime_list(10 ** len(numbers))
    visited = [0] * len(numbers)
    numbers = list(numbers)
    for i in range(1, len(numbers) + 1):
        permu([], 0, i, len(numbers), numbers)
    return len(list(set(result)))