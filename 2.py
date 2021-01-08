# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations


def solve(KEY, VALUES, depth, array):
    if numberOfAttribute == depth:
        cnt = 0
        for line in input_data:
            find = True
            for k, v in array:
                if line.get(k):
                    if line[k] != v:
                        find = False
                        break
                else:
                    find = False
                    break
            if find:
                cnt += 1
        if threshold <= cnt / numberOfRows:
            ans = ''
            for k, v in array:
                ans += (k + '=' + v + ',')
            print(ans[:-1])
    else:
        for v in VALUES[depth]:
            arr = array[:]
            arr.append((KEY[depth], v))
            solve(KEY, VALUES, depth + 1, arr)


if __name__ == "__main__":
    numberOfAttribute = int(input())
    threshold = float(input())
    numberOfRows = int(input())
    input_data = []
    database = {}
    for idx in range(numberOfRows):
        row = {}
        attris = input().split(',')
        for att in attris:
            k, v = att.split('=')
            row[k] = v
            if database.get(k):
                if database[k].get(v):
                    database[k][v] += 1
                else:
                    database[k][v] = 1
            else:
                database[k] = {v: 1}
        input_data.append(row)

    possible_hubos = {}
    for attri, values in database.items():
        for k, v in values.items():
            if (v / numberOfRows) >= threshold:
                if possible_hubos.get(attri):
                    possible_hubos[attri].append(k)
                else:
                    possible_hubos[attri] = [k]
    hubos = [k for k in possible_hubos]
    attribute_combi = []
    for combi in combinations(hubos, numberOfAttribute):
        attris = [[] for _ in range(6)]
        for i in range(numberOfAttribute):
            attris[i] = possible_hubos[combi[i]]
        solve(combi, attris, 0, [])

# 2
# 0.6
# 10
# age=Middle-aged,sex=Male,education=Bachelors,native-country=United-States,race=White,marital-status=Never-married
# age=Senior,sex=Male,education=Bachelors,native-country=United-States,race=White,marital-status=Married-civ-spouse
# age=Middle-aged,sex=Male,education=HS-grad,native-country=United-States,race=White,marital-status=Divorced
# age=Senior,sex=Male,education=11th,native-country=United-States,race=Black,marital-status=Married-civ-spouse
# age=Middle-aged,sex=Female,education=Bachelors,native-country=Cuba,race=Black,marital-status=Married-civ-spouse
# age=Middle-aged,sex=Female,education=Masters,native-country=United-States,race=White,marital-status=Married-civ-spouse
# age=Senior,sex=Female,education=9th,native-country=Jamaica,race=Black,marital-status=Married-spouse-absent
# age=Senior,sex=Male,education=HS-grad,native-country=United-States,race=White,marital-status=Married-civ-spouse
# age=Middle-aged,sex=Female,education=Masters,native-country=United-States,race=White,marital-status=Never-married
# age=Middle-aged,sex=Male,education=Bachelors,native-country=United-States,race=White,marital-status=Married-civ-spouse