# # # a = 100000000
# # # b = 100000000

def solution(S):
    global total, answer

    temp = []
    for s in S:
        temp.append(list(s))

    print(temp)
    total = []
    
    def combi(arr, depth, last, N, length):
        global answer
        if depth == N:
            for ar in arr:
                set_ar = set(ar)
                if len(ar) == len(set_ar):
                    total.append(ar)
                    answer = max(answer, len(ar))
        else:
            for n in range(last, length):
                ar = arr[:]
                ar.append(temp[n])
                combi(ar, depth + 1, n + 1, N, length)
            
    length = len(temp)
    answer = 0

    for n in range(1, length + 1):
        combi([], 0, 0, n, length)
        
    return answer


print(solution(['co', 'dil', 'ity']))

# # ##################

# # a = [1, 2, 3]
# # length = len(a)
# # total = []

# # def combi(arr, depth, last, N):
# #     global total
# #     if depth == N:
# #         total.append(arr)
# #     else:
# #         for n in range(last, length):
# #             ar = arr[:]
# #             ar.append(a[n])
# #             combi(ar, depth + 1, n + 1, N)
    


# # for n in range(1, length + 1):
# #     combi([], 0, 0, n)

# # print(total)


# G = 0
# temp = []
# s = 0
# while s != len(A):
#     ans = ''
#     for i in range(s, len(A)):
#         if len(ans + A[i]) == len(ans + set(A[i])):
#             ans += A[i]
#             temp.append(len(ans))
#     s +=1

# if len(temp):
#     G = max(temp)

# print(G)