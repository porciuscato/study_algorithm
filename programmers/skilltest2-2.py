number = list(map(int, list("1231234")))
k = 3
length = len(number)
choice = length - k

TABLE = [[-1] * 1000000 for _ in range(10)]

# 위치와 최대 값을 저장
mx_list = []

for idx in range(length - 1, -1, -1):
    num = number[idx]
    start = 0
    while TABLE[num][start] != -1 or start < 1000000:
        start += 1
    TABLE[num][start] = idx

for i in range(10):
    print(TABLE[i][0])


# for num in range(length):
#     val = number[num]
#     if val == mx:
#         mx_list.append((num, val))
#     elif val > mx:
#         mx_list = []
#         mx_list.append((num, val))

# # 이제 mx_list에 대한 확인

        


# # def combi(arr, depth, last):
# #     global mx
# #     if depth == choice:
# #         to_num = int(''.join(arr))
# #         mx = max(mx, to_num)
# #     else:
# #         for num in range(last, length):
# #             ar = arr[:]
# #             ar.append(number[num])
# #             combi(ar, depth + 1, num + 1)


# # combi([], 0, 0)


# # print(mx)



