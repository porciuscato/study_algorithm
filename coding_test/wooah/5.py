def solution(penter, pexit, pescape, data):
    answer = penter
    w_len = len(penter)
    for i in range(0, len(data), w_len):
        datum = data[i:i + w_len]
        if datum == penter or datum == pexit or datum == pescape:
            answer += pescape + datum
        else:
            answer += datum
    answer += pexit
    return answer


cases = [
    ("1100", "0010", "1001", "1101100100101111001111000000"),
    ("10", "11", "00", "00011011"),
]

for case in cases:
    print(solution(*case))
