# 4828
def find_max(ai):
    maxi = ai[0]
    for i in range(1,len(ai)):
        if maxi < ai[i]: maxi = ai[i]
    return maxi

def find_min(ai):
    mini = ai[0]
    for i in range(1,len(ai)):
        if mini > ai[i]: mini = ai[i]
    return mini

for T in range(1,int(input())+1):
    N = int(input())
    ai = list(map(int,input().split()))
    print('#{} {}'.format(T, find_max(ai) - find_min(ai)))
