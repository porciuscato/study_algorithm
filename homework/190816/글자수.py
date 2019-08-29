for T in range(1,int(input())+1):
    N = input()
    M = input()
    N_dict = {}
    for char in N:
        N_dict[char] = 0
    for char in M:
        if N_dict.get(char) != None:
            N_dict[char] += 1
    print('#{} {}'.format(T,max(N_dict.values())))
