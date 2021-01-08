# Enter your code here. Read input from STDIN. Print output to STDOUT
def simil(x, y):
    global simil_table
    sigma_x = 0
    sigma_y = 0
    sigma_xy = 0

    for itm in range(1, num_items + 1):
        sigma_x += datatable[x][itm] ** 2
        sigma_y += datatable[y][itm] ** 2
        if datatable[x][itm] > 0 and datatable[y][itm] > 0:
            sigma_xy += datatable[x][itm] * datatable[y][itm]
    try:
        simil_table[x][y] = (sigma_xy / ((sigma_x ** 0.5) * (sigma_y ** 0.5)), y)
    except ZeroDivisionError:
        pass


def calc_avg():
    global r_avg_u
    for i in range(1, num_users + 1):
        cnt = 0
        tot = 0
        for j in range(1, num_items + 1):
            if datatable[i][j] > 0:
                cnt += 1
                tot += datatable[i][j]
        if cnt:
            r_avg_u[i] = tot / cnt


def calc_Rui():
    global Rui
    for u in range(1, num_users + 1):
        # k 구하기
        temp_sigma = 0
        for val, _ in simil_table[u]:
            # for val, _ in set_U[u]:
            if val != -100:
                temp_sigma += abs(val)
        try:
            k = 1 / temp_sigma
        except ZeroDivisionError:
            k = 0

        for j in range(1, num_items + 1):
            if chosen[u][j]:
                if k != 0:
                    simil_sigma = 0
                    for val, u_prime in set_U[u]:
                        if u_prime != 0 and val != -100:
                            simil_sigma += val * (datatable[u_prime][j] - r_avg_u[u_prime])
                Rui[u][j] = (r_avg_u[u] + k * simil_sigma, j)


if __name__ == "__main__":
    num_sim_user_topk = int(input())
    num_item_rec_topk = int(input())
    num_users = int(input())
    num_items = int(input())
    num_rows = int(input())
    datatable = [[0 for _ in range(num_items + 1)] for __ in range(num_users + 1)]
    for _ in range(num_rows):
        u, i, r = input().split()
        datatable[int(u)][int(i)] = float(r)

    reco_users = []
    num_reco_users = int(input())
    for _ in range(num_reco_users):
        reco_users.append(int(input()))

    simil_table = [[(-100, 0) for _ in range(num_users + 1)] for __ in range(num_users + 1)]
    for i in range(1, num_users + 1):
        for j in range(1, num_users + 1):
            if i != j:
                simil(i, j)

    r_avg_u = [0 for _ in range(num_users + 1)]
    calc_avg()

    set_U = [[0 for _ in range(num_sim_user_topk + 1)] for __ in range(num_users + 1)]
    for u in range(1, num_users + 1):
        arr = sorted(simil_table[u], reverse=True)
        set_U[u] = arr[:num_sim_user_topk]

    Rui = [[(-100, 0) for _ in range(num_items + 1)] for __ in range(num_users + 1)]

    chosen = [[False for _ in range(num_items + 1)] for __ in range(num_users + 1)]
    for i in range(1, num_users + 1):
        for ele in set_U[i]:
            n = ele[1]
            for idx in range(1, num_items + 1):
                if datatable[n][idx] > 0 and not chosen[i][idx]:
                    chosen[i][idx] = True

    calc_Rui()

    # print(chosen)

    # for _ in set_U:
    #     print(_)
    for _ in simil_table:
        print(_)
    # print()
    result = [[0 for _ in range(num_item_rec_topk)] for __ in range(num_users + 1)]
    for i in range(1, num_users + 1):
        arr = sorted(Rui[i], reverse=True)
        # print(arr[:5])
        pos = 0
        for ele in arr:
            i_num = ele[1]
            if datatable[i][i_num] == 0 and chosen[i][i_num]:
                result[i][pos] = i_num
                pos += 1
            if pos == num_item_rec_topk:
                break

    for num in reco_users:
        for n in result[num]:
            if n != 0:
                print(n, end=" ")
        print()
