# 알고리즘 공부 팁

### 코딩 전에 분석부터

- 좁은 것에서부터 확장해 나갈 것
- 코딩부터 하는 건 나쁜 습관
- 슈도 코드로 먼저 짜서 손으로 직접 돌려봐라
- 문제를 **꼼꼼히** 읽어라. 처음부터 꼼꼼히 읽어서 한 번에 짜내는 것이 훠어얼씬 빠르다. 디자인은 *한 큐*에
  - 디버깅이 생각보다 오래걸린다.

- 파이썬을 세컨드 언어로 가지는 것
  - 파이썬으로 로직을 간단히 짜본 이후 C언어로 번역



### IM

- 함수를 쓰기보다 그냥 메인에서 한 번에 작성하자.
- 코드 길이, 시간 이런 거 신경 쓸 필요 전혀 없다.





# 7월 31일

백경원 선생님

삼성전자 인재개발원(수원 서천동). 



APS 기본. Algorithm Problem Solving 

APS는 자료구조를 앞, 알고리즘을 뒤. 

IM,Ad,Pro,Ex

APS는 어드를 fully 커버를 못하는 상태. 인터와 어드 조금



APS 응용. 2주 과정

어드에서 프로 조금 커버.



Pro 사전과정. 1주 과정

Pro (본)과정. 3주 과정. 많이 못 따라와



Pro 실습응용(pair)

Pro 실전. 문제만 풀어



엑스퍼트. 문제가 한 줄. 프로그램 자체를 짤 수 있어야....



이런 과정이 있는데도 어렵다.



ad는 3시간. pro, expert는 4시간







로드맵

P.L 프로그램 랭귀지

- type : 자료의 형태와 필요한 연산에 대해
- 제어 : 프로그램 제어란 무엇인지 이해하는 것
  - 주로 3가지. 
    - 순차 구조. 선택 구조. 반복 구조



- IM : for문 쓸 수 있냐? 순차, 선택, 반복으로 제어할 줄 아는지 평가





### 자료구조 

- ADT : 자료, 연산(삽입, 삭제, **순회**)
  - 순회 반드시 알아야 함!



product, 검정... 자료구조를 사용. ''이땐 이 자료구조가 필요하겠구먼' -> 구현을 하는데, 구현은 **선택**의 문제다. 

검정에서만 쓰는 구현이 있다. product에서 쓰는 구현을 검정에서 쓰면 시간이 모자란다.



자료구조는 크게 2부류. 

- 선형: 엘리먼트간 관계가 1대1. 2차 배열도 그냥 선형으로 봄. 

  - 배열. (같은 자료형을 여러개 묶어서 저장하는 것)

  - 리스트. (리스트는 삽입 삭제가 빈번하게 일어나는 자료를 처리할 땐 리스트)

  - 스택. 

  - 큐. 

    등등

- 비선형 자료구조: element간 1대1일지 1대 다일지 모름. 

  - 트리. (트리는 그래프 중 사이클이 없는 무방향 그래프). 즉 트리는 그래프의 부분집합
  - 그래프. 

  그래프는 인접행렬(메모리를 많이 먹음), 인접리스트(동적으로 메모리를 할당)

  트리. 1차 배열? 혹은 리스트 구조. 선택을 해야 함



#### 순회

반드시 알아야 함.

traversal

- 순회: 빠짐없이 중복없이 조회할 수 있어야 함. DFS(스택 사용), BFS(큐 사용)
- 삼성에서 어드 시험 보려면... 백 트래킹을 제일 많이 씀. 그런데 이건 DFS 방식.



조건에 따라 적당한 알고리즘이 달라짐. 



*** 이진트리, 이진탐색트리, AVL트리, B트리, 트라이, 허프만 트리, 아웃코라식 트리, 세그먼트 트리 => 이런 트리들에 대해서도 다 알아야 함

=> 얘네들에 대한 탐색: 미니멈 스패닝 트리, 최단경로 찾기(다익스트라 알고리즘, TSP 트래벌링 세일즈맨, 플로이드 알고리즘, 델만 알고리즘, AoV, AoE 등등)



기본을 다 해놓고 하나씩 배워나감. 





알고리즘 입장.... 프로그램이란? `검색`. 



설계기법. 주로 4가지 얘기

- 그리드 (탐욕 알고리즘). pro도 이걸 적용하는 건 위험. expert나 되야... 검증이 되야하기 때문
- ***분할정복. pro와 ad의 덕목! 분할정복을 써야만 문제가 풀리는 문제를 디자인 하기가 어렵다. 
- 백 트래킹(상태 공간 트리. DFS or stack or recursion). 백 추적. 
- DP. 
  - 재귀적 DP. 백트래킹을 기본으로 메모리 처리. 
  - 반복적 DP. 

이러한 설계기법을 알기 전 반드시 알아야 하는 것, 구현할 수 있어야 하는 것? => `**완전검색** ` 

어드 문제가 완전검색. 

-> 조합론

- 순열, 조합, 부분집합 : 이런 것들을 생성해서 다 조사하는 것이 완전검색
  - 순열로서 완전검색은 TSP. 시간복잡도가 팩토리얼 의존적. 
  - 부분집합(배낭 문제). O(2^n).  => 지수승의 시간 복잡도를 가지는 알고리즘



NP 클래스 문제, P 클래스 문제

P 클래스 문제는 시간 내 풀 수 있는 문제

NP는 인간이 견딜 수 없는 시간 내  풀게 됨. -> 근사 알고리즘, 인공지능. (이때 자료구조는 트리)





실습 문제 푼 게 포인트가 쌓임

시작이 중요(타입과 `제어`) => 머릿속 생각이 제어로 쫘악 나올 것. 

라이브러리를 쓰면 안의 `제어`가 하나도 연습이 안 됨.

강력 권장하기로는... 실습 문제 낼 때 라이브러리를 쓰지 말고 구현해 볼 것

프로는 당연히 쓰지 말 것.

라이브러리 못 씀. 밑에서부터 구현. 연습을 할 것



------

IM : 타입과 제어

Ad: 완전검색. 

=> 생각나는대로 A4 용지에 적어라.

자기가 만든 라이브러리를 가지고 다니는 것. 얼마나 멋있는가!



------

# 1. 알고리즘

순서도, flowchart



알고리즘 판단 기준

1) 정확성

2) 작업량: 연산횟수. 기계 수준으로 내려가면 연산자마다 연산횟수가 다르다.

- 명령어의 갯수로 표현. 빅오 노테이션. (코드 실행 환경에 따라 속도가 다르기 때문)

3) 메모리: 

- 우주 항공기에서는 굉장히 제한되어 있음
- 그러나 검정에서는 걱정할 필요 없음

4) 단순성: 가독성. (프로젝트에서 재귀함수는 쓰면 안됨....)

5) 최적성



검정 시에는 정확성과 시간복잡성만 고려. 그러나 `정확성`이 최고 중요. 시간 줄이는 건 다음 문제





## (1) 배열

1. gravity 문제
   - 맨 위 상자가 가장 이동 거리가 김 -> 맨 위만 생각.
2. Baby-gin Game : 완전 검색이 먼저 들어야 함. 정렬이 아니라 -> 어떻게 뽑느냐에 따라 답이 있을 수도 없을 수도. 핵심은: 모든 케이스를 조사하는 방법이 뭐냐!
   - Brute Force의 의미: '컴퓨터의 괴물같은 연산력을 믿고 컴퓨터에게 맡겨라! '라는 것
   - generate_and_Test: 모든 경우를 생성해서 테스트해봐라.

=> 6팩토리얼 만큼 다 조사하겠다는 것. 예외가 없는 것.

=> 6팩토리얼 만큼 다 나열한 뒤, 뒤와 앞이 런인지 트레플릿인지 파악하면 됨



=> 백트래킹으로 돌린다....

#### 순열

순열을 생성하는 알고리즘?

nPr

기본적인 접근법 2가지. 

재귀로 코딩하려면 어렵다...



=> 백트래킹으로 돌린다...



#### 탐욕 알고리즘 설계기법

- 굉장히 위험하다... 쓰면 안 된다...
- 검증이 필요하다. 평소에 걸리지 않는 corner case를 넣기 때문

예) 거스름돈 문제

​	: 문제 셋의 범위를 조그맣게 만드는 것

일단 완전 검색을 해라....

{100,50,10} 으로 동전셋이 나오면 탐욕이 끝나는데, {50,40,20,10} 이런 식의 corner  case가 나오면 답이 달라짐. 

- 완전 검색이더라도 중복순열은 제거하고 조합으로 수를 줄인다. 그리고 해답은 DFS가 아니라 BFS로 찾는다. 



탐욕이 더 효율적이더라도 완전검색으로 갈 것. 탐욕은 커버하지 못하는 케이스가 있을 수 있기 때문

만약 탐욕 알고리즘으로 가더라도, triplet과run 탐색의 순서가 바뀌면 답이 바뀔 수 있다.





#### 정렬 알고리즘

O(n^2) : 버블, 삽입, 선택

O(n logn): 퀵, 병합

O(n): 카운팅 정렬 (그러나 아무 때나 쓸 순 없다.)



##### 카운팅 정렬

전제조건

​	1) 범위, 개수가 있어야 한다.

​	2) 구성하고 있는 타입이 정수형이어야 한다. 혹은 소수점 몇째 자리까지인지 알려준다면 가능! 

​		- 만약 소수점 2째 자리까지 한다면, 0과 1 사이일 경우 101 개의 배열을 만들면 됨



? 왜 카운팅 정렬에서는 왜 인덱스를 저장할까?

** => 순서가 중요하기 때문! 먼저 온 수가 먼저 저장된다!! **

무조건 퀵 정렬을 쓸 게 아니라, 카운팅 정렬을 쓸 수도 있다.





view



내일은?

소스를 메일로 보낸다. 4문제의 소스를 메일로 보낸다.

beeback@daum.net



파이참 프로도 아니다. 파이참





# 8월 1일

### 1206 문제 : 1000개의 케이스 -> **많은 게 아니구나!** 라고 생각할 수 있어야 한다. 

- max를 구하는 방법!
  - 처음 값을 max로 설정한 뒤 나머지 값과 비교하여 바뀌는지 확인. -> 선택 정렬
- 굳이 정렬을 하지 않고, 케이스가 5개 밖에 되지 않으니 이 중에서 선택 정렬을 통해 찾아도 상관 없다.



파이참 디버깅 모드. stdin처럼 redirction을 하는 코드가... 

```python
import sys
sys.stdin = open("input.txt", "r")
```

디버깅 실행 이후 F8 누르면 가능



분석하고 디자인 할 때....

자꾸 패칭해 나가면 꽝이 됨.

그럴 땐 코딩하지 말고, 슈도 코딩해서 손으로 코드를 다 돌려보는 것



무조건 분석부터 할 것!! 일단 짜면서 생각하는 건 굉장히 나쁜 습관. 한 번 오류가 생기면 잡기가 굉장히 어려워진다.



오늘 총 5문제. 4문제는 소스를 보내고 1문제는 그냥 풀고







# 8월 7일

## 저번주 문제



#### 전기버스 문제

정보 처리 입장에서는, 내가 작성한 코드처럼 사전에 제어를 하는 건 좋지 않은 방식

```python
def test(K, N, M, stop, jido):
    ####################################
    #이 부분이 먼저 제어를 하는 부분. 이런 건 하지 말자.
    if (M < N // K) or (stop[0] > K) or (N - stop[-1] > K):
        return 0
    ####################################
    for i in range(len(stop) - 1):
        if stop[i + 1] - stop[i] > K:
            return 0
    now, count = 0, 0
    while True:
        if now + K >= N:
            break
        for i in range(K, 0, -1):
            if jido[now + i] == 1:
                now += i
                count += 1
                break
    return count


for T in range(1, int(input()) + 1):
    K, N, M = list(map(int, input().split()))
    stop = list(list(map(int, input().split())))
    jido = [0 for i in range(N+K)]
    for i in stop:
        jido[i] = 1
    result = test(K, N, M, stop, jido)
    print('#{} {}'.format(T, result))
```



- 이중 반복문에서 break를 통해 나오려면 flag 설정을 해야함. 복잡해질 수 있다.



#### 숫자카드

카운팅 정렬을 활용



#### 구간합

선형 자료가 주어졌을 때.... 

- 프로의 중요한 덕목: `Do not recompute!!`
  - 한 번 정보 처리할 때 정보를 잘 저장해놓고 쓰는 것. raw한 데이터에 계속 접근하면 시간이 많이 소요됨
  - 만약 배열 길이가 1억개고 범위가 1000이라면?
    - 1억개 탐색으로만 끝낼 수 있다!
      - *** 슬라이딩 윈도우 기법. 한 번의 선형 처리로 끝내는 방법!!! 카포라빈의 아이디어
      - 처음 값을 빼고 맨 뒤에 값을 넣는다.
    - 혹은 애초에 배열에 구간합을 저장하여 구간합의 처음과 끝 값의 차이만으로 구할 수 있다.



#### flatten

카운팅 정렬을 사용할 수도 있다!







## 수업

### 2차원 배열

선형 자료형의 확장

- 주의할 점: runtime error 의 대다수는 자신이 설정한 자료형의 범위를 넘어서는 것. => 인덱스를 의심할 것. 



#### 순회

- 많이 쓰는 게 행 우선 순회  -> outer가 행을 control, inner가 열을 control
- 열 우선 순회 -> 밖에서 열을, 안에서 행을 제어
- 지그재그 순회
  - 짝수 번째는 정순으로 돌고 홀수 번째는 역순으로 돌겠다는 것



#### 델타

- 2차 배열 구조를 가장 많이 사용한다.

- 한 좌표 상에서 인접 배열을 탐색하는 방법

  - 상대적인 위치를 계산하면 됨

    ```python
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for I in range(4):
        testX = x + dx[I]
        testY = y + dx[I]
        test(ary[testX][testY])
    ```



#### 전치행렬

가로방향과 세로 방향을 바꾸는 것!

```python
for i in range(3):
    for j in range(3):
        if i < j:
            # 대각선은 바꾸지 않고, 위의 삼각형만 바꾸겠다는 논리
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```



맨 끝 줄은 이웃이 3개이고, 꼭짓점은 이웃이 2개인데 이때는 어떻게 제어해야하는가?



#### 연습문제 1 : 4방향 탐색

```python
def isWall(x,y):
    if x < 0 ir x >= 5: return True
    if y < 0 or y >= 5: return True
    return False

def calAbs(x,y):
    if y - x > 0: return y - x
	return x - y

sum = 0
for x in range(len(arr)):
    for y in range(len(arr[0])):
        for i in rnage(4):
            textX = x + dx[i]
            textY = Y + dx[i]
            if isWall(testX, testY) == False:
                sum += calAbs(arr[x][y],arr[testX][testY])
```





#### 연습문제2 : 부분집합 생성

{1,2,3}의 부분집합은?

{}, {1}, {2}, {3}, {1,2}, {1,3}, {1,2}, {1,2,3}

=> 총 8개 생성

입력값 N이 3일 때 총 8개가 됨 -> 2^3 -> 2^n 지수승으로 경우의 수가 생성된다.

- 대표적으로 배낭문제: O(2^n)



`+` 혹은 1,2,3 중 선택할지 말지에 의해 결정

=> 트리 구조로 만든 다음, 생성되는 경우를 본래 집합에서 가져온다.



###### 어떻게 코드로 구현할 수 있겠는가?

1) for문으로 구현: n개 만큼 중첩적으로 구현

- 이 경우는 n개의 동적 입력을 커버하지 못함
- 하지만 각 트리에서 하는 일은 비슷하기 때문에 이걸 재귀로 짤 수가 있다. (`백트래킹`)



##### 다른 방법에 대해서 생각해보자....

- bit (binary digit) 연산에 대한 이해가 필요하다.

  - 비트논리연산자

    | operator          | Description          |
    | ----------------- | -------------------- |
    | & : ampersand     | AND 연산             |
| \| : vertical bar | OR 연산              |
    | ^ : caret         | XOR 연산             |
    | ~ : tilde         | 보수 연산            |
    | <<                | 왼쪽 시프트(2배)     |
    | >>                | 오른쪽 시프트(1/2배) |
    
  
  
  
  ################################################
  
  - `i & ( 1 << j)` : i는 어떤 수, j는 i 안의 몇 번째 비트(어떤 비트가 0인지 1인지 확인하는 코드 조각이다.)
  
    - ex) 6 & (1<<2) : 3번째 비트가 뭐냐는 것.
      - 1<<2 -> 100. 이걸 6과 &를 시키면 -> (110 & 100) : `masking`한다.
  
    ```
    6 & (1 << j)
    if (2**j):
    	어쩌구 저쩌구....
    ```
  
    
  
  이걸 통해서 부분집합을 만들어보자.



##### **binary counting algorithm**

2) 비트 연산을 활용해보자 (바이너리 카운팅 알고리즘)

아래 수를 2진이라 생각해보자. 이 수들은 < 8 = 2^3 = 2^n

111 : 7

110 : 6

101 : 5

100 : 4

011 : 3

010 : 2

001 : 1

000 : 0



#### 연습문제

다음 집합에서 부분집합을 뽑았을 때 0이 되는 부분집합은?

{1,-1,0,4,5,-3,-2..........}

어떻게 검색을 할지는 모를 땐? `완전검색` 어떤 구성의 집합이 0을 만족시킬지 알 수가 없다. greedy가 낄 틈이 없다.

- 부분집합을 생성하는 방법

  **binary counting** : 비트연산을 활용하자.

  ```python
  arr = [3,6,7,1,5,4]
  n = len(arr)
  for i in range(1<<n): # 1<<n 은 부분집합의 개수
      for j in range(n): # 원소의 수만큼 비트를 비교함
          if i & (1<<j): # 0이 아닌 경우 참. 즉 i의 j번째 비트가 1이면 j 번째 원소 출력
              print(arr[j], end=', ')
      print()
  print()
  ```

  > 돌아가는 과정을 보면
  >
  > j = 0 -> 000001 -> 1
  >
  > j = 1 -> 000010 -> 10
  >
  > ....
  >
  > ....

| size=16 \ len=4 | 1    | 10   | 100  | 1000 |
| --------------- | ---- | ---- | ---- | ---- |
| 0               | 0    | 0    | 0    | 0    |
| 1               | 1    | 0    | 0    | 0    |
| 10              | 0    | 1    | 0    | 0    |
| 11              | 1    | 1    | 0    | 0    |
| 100             | 0    | 0    | 1    | 0    |
| 101             | 1    | 0    | 1    | 0    |
| 110             | 0    | 1    | 1    | 0    |
| 111             | 1    | 1    | 1    | 0    |
| 1000            | 0    | 0    | 0    | 1    |
| 1001            | 1    | 0    | 0    | 1    |
| 1010            | 0    | 1    | 0    | 1    |
| 1011            | 1    | 1    | 0    | 1    |
| 1100            | 0    | 0    | 1    | 1    |
| 1101            | 1    | 0    | 1    | 1    |
| 1110            | 0    | 1    | 1    | 1    |
| 1111            | 1    | 1    | 1    | 1    |

바이너리 카운팅의 의미: 

- 1개 이상이 시작되는 지점 : 2 - 1 
- 2개 이상이 시작되는 지점: 4 - 1
- 3개 이상이 시작되는 지점: 8 - 1

.....

- n개 이상이 시작되는 지점: 2^n - 1 





- 그러나 이것의 안 좋은 점?

  - 어떤 문제에 대해서는 제어할 필요가 있다. 6개 중 4,5개 까지만 할 필요가 없는 경우가 있음. 그러나 이땐 제어가 어렵다. 그래서 `백트래킹`을 활용

  

  #### 연습문제 2

  ```python
  a = [-2,-4,9,3,-6,5,7,-6,1,8]
  n = len(a)
  count = 0
  for i in range(1,1<<n): # 1부터 시작해야 공집합을 처리하지 않는다.
      temp = []
      for j in range(n):
          if i & (1<<j):
              temp.append(a[j])
      if sum(temp) == 0:
          count += 1
          print(temp)
  print(count)
  ```

  



### 검색 search

##### 순차 검색(sequential search)

- 되게 느려서 안 함

- 최악의 경우 n번 조사를 해봐야 한다. O(n)

  ```python
  def sequentialSearch(a, n, key):
      i = 0
      while i < n and a[i] != key:
          i += 1
      if i < n: return i
      else: return -1
  ```

  

- 정렬되어있는 경우, 원하는 값보다 클 경우 뒷단은 검사할 필요도 없다. (이것이 프로의 덕목)

  ```python
  def sequentialSearch(a, n, key):
      i = 0
      while i < n and a[i] < key:
          i += 1
      if i < n and a[i] == key: return i
      else: return -1
  ```



##### 이진 검색(Binary Search) 

-  **엄청 중요**한 알고리즘. 그러나 IM에서는 안 나온다. Pro에서 즐겨씀. 퍼포먼스가 좋다.
- 그 전에... 보간 검색?
  - 전화번호부를 뒤지는 방식. 잘 안 쓴다. 정확히 1/2 위치에서 검색하는 것이 이진검색

```python
def binarySearch(a,key):
    start = 0
    end = len(a)-1
    while start <= end:
        middle = (starrt + end)//2
        if a[middle] == key:
            return True
        elif a[middle] > k3y:
            end = middle -1
        else: start = middle + 1
   return False
```

- 재귀함수로도 구현이 가능하다

  ```python
  def binarySearch(a, low, high, key):
      if low > high:
          return False
      else:
          middle = (low + high) // 2
          if key == a[middle]:
              reutnr True
  		elif key < a[middle]:
              return binarySearch(a, low, middle-1,key)
          elif a[middle] < key:
              return binarySearch(a, middle+1, high,key)
  ```



##### 인덱스

- 이진 검색을 하기 위해서는 추가 삭제가 이루어질 때마다 정렬을 해줘야 한다.
- 정렬은 값을 비교하고 옮기는 일. 레코드 단위로 값을 옮기면 시간이 상당히 오래 걸림. 그러면 어떻게?
  - 원본데이터는 막 쌓고... array index와 original index를 정렬할 뿐. 
  - 검색을 빨리하는 방법 중 하나



테이블의 집합을 릴레이셔널 DB(RDB)





### 선택 알고리즘 Selection Algorithm

배열에서 n 번째 큰 값을 찾기 위해서는? 정렬한 다음 n 번째 값을 return하면 되는데

꼭 그렇게 해야했나!

선택정렬은 시간 복잡도가 O(kn)

방법은?

1) 처음부터 끝까지 일단 min을 찾아. 

2) 찾은 값을 가장 맨 앞으로 옮겨

3) 그리고 첫번째를 제외한 영역에서 가장 작은 값을 찾아.

```python
def select(list, k):
    for i in range(0,k):
        minIndex = i
        for j in range(i+1,len(list)):
            if list[minIndex] > list[j]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
	return list[k-1]
```



### 선택 정렬

선택 정렬은 선택 알고리즘은 n번까지 수행하는 것





#### 연습문제 3

1) 배열에서 min을 찾고 찾아낸 위치는 100 혹은 여타의 기호로 marking한다.

2) 델타를 이용해서 한다.





# 8월 8일

#### 달팽이 문제 (연습문제 3)

```python
def iswall(x,y):
    if x<0 or x>= 5: return True
    if y <0 or y>=5: return True
    if sorted_ar[x][y] != 0: return True
    return False

def sel_min():
    minx, miny = 0, 0
    for i in range(5):
        for j in rnage(5):
            if ar[minx][miny] > ar[i][j]:
                minx, miny = i, j
    mini = ar[minx][miny]
    ar[minx][miny] = 99
    return mini

x, y =0, 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
############
dir_stat = 0
############

for i in range(25):
    cur_min = sel_min()
    sorted_ar[x][y] = cur_min
    x += dx[dir_stat]
    y += dy[dir_stat]

    if iswall(x,y):
        x -= dx[dir_stat]
        y -= dy[dir_stat]
        # 반복을 컨트롤하는 방법으로서 modula!!
        dir_stat = (dir_stat +1) % 4
        x += dx[dir_stat]
        y += dy[dir_stat]

for i in range(5):
    for j in range(5):
        print(sorted_arp[i][j], end=" ")
    print()
```



#### 금속막대 문제

한 시퀀스만 나온다. 

맨 앞에 걸 찾아서 붙여나가면 된다. 중간에 나오는 건 수나사에 대응되는 앞에 것이 있어야 한다. 맨 앞에는 꽂을 수 있는 암나사가 없기 때문에 맨 앞이다라는 것.





어드쁠

완전검색류, 시뮬레이션 문제 ( 대회에서는 시뮬레이션을 안 냄. 삼성에서 냄)

''모의''라고 치면 어려운 문제 나옴





# 8월 14일

### 부분집합 구하기

- 모든 정보의 선택 유무를 통해 부분집합을 생성한다.

  **binary counting을 활용**

- subset의 합 혹은 subset의 원소의 개수를 구하는 문제

```python
A = [i for i in range(1, 13)]

for T in range(1, int(input()) + 1):
    count = 0
    N, K = map(int, input().split())
    size = len(A)

    for i in range(2**N - 1, 1 << size):
        temp = []
        for j in range(size):
            if i & (1 << j):
                temp.append(A[j])
        if len(temp) == N and sum(temp) == K:
        	count += 1
    print('#{} {}'.format(T, count))
```



### 이진탐색

- 문제를 꼼꼼히 읽자

```python
for T in range(1, int(input()) + 1):
    P, A, B = list(map(int, input().split()))

    l, r, count_A = 1, P, 1
    while True:
        c = int((l + r) / 2)
        if c == A:
            break
        elif c < A:
            l = c
            count_A += 1
        else:
            r = c
            count_A += 1

    l, r, count_B = 1, P, 1
    while True:
        c = int((l + r) / 2)
        if c == B:
            break
        elif c < B:
            l = c
            count_B += 1
        else:
            r = c
            count_B += 1
    if count_A < count_B:
        result = 'A'
    elif count_A > count_B:
        result = 'B'
    else:
        result = 0
    print('#{} {}'.format(T, result))

```



### 화학문제 팁

- 행렬 곱에서는 어떻게 곱하느냐에 따라 연산 수가 달라진다.

  ex) 2 x 3 / 3 x 4 / 4 x 5

  이때 앞에 두 개를 먼저 하느냐, 뒤에 두 개를 먼저 하느냐에 따라 속도가 달라진다.

  완전 탐색하면 도저히 속도가 안 나온다. => **DP**를 쓴다. 



## 문자열

알파넷. 최초의 네트워크



- big endian 과 little endian?
  - 오름 차순 혹은 내림 차순. BE 혹은 LE라고 쓰여있다.



#### 문자열의 타입

C 언어. 문자열의 시작 포인트를 가지고 있다. 어디까지 읽어야 할 지 모름. 그래서 예외적인 문자를 하나 두어서 마커로 둔다. '\0'  : null character (delimiter)

```c++
char ary[] = {'a','b','c','\0'}; # 또는
char ary[] = "abc";
```

문자열 처리에 필요한 연산

```c++
strlen(), strcpy(), strcmp(), ...
```

프로 정도 준비하려면... 위의 연산을 쓰지 못하니... 일일 구현

문자열 길이, 문자열 카피, 비교, 수치로 바꾸기... 5가지 연산이 바로 코딩이 되야함

파이썬은 필요가 없다. 



##### 파이썬에서의 문자열 처리

- 파이썬 문자열은 immutable하다. 각각에 접근해서 변경할 수는 없다.



### C, python의 string 처리

```c
char * name = "홍길동";
int count = strlen(name);
printf("%d", count);
// 6 출력
```

```python
name = "홍길동"
print(len(name))
# 3 출력
```





##### Python에서 reverse 함수나 slicing을 사용하지 않고 문자열을 뒤집으려면 어떻게 해야할까?

```python
s = "Reverse this string"
sr = ''
for i in range(len(s)-1,-1,-1):
  sr = sr + s[i]
print(sr)
```



#### c언어에서 itoa(), atoi() 함수

: integer to ascii 

```c
int atoi(const char *string){
  int value = 0, digit, c;
  while((c = *string++) != '\0'){
    if (c >= '0' && c <= 9)
      digit = c - '0';
    else
      break;
    value = (value * 10) + digit;
  }
  return value;
}
```



그 반대는?

1234라는 숫자를 10으로 나누면 4가 나오고 4에다가 '0'을 더하면 4가 나옴



#### python 에서는 ord(), chr()

str() 함수를 사용하지 않고 itoa()를 구현해보자

내 코드

```python
n = 1000
re = 0
result = ''
for i in range(4):
    re = n % 10
    n = n // 10
    re = chr(re + 48)
    result = re + result
print(result)
```

선생님 코드

```python
def itoa(x):
    sr = ''
    while 1:
        r = x % 10
        sr = sr + chr(r + ord('0'))
        x //= 10
        if x == 0: break

    s = ''
    for i in range(len(sr) - 1, -1, -1):
        s = s + sr[i]

    return s
```











## 패턴 매칭 알고리즘

### 1. 고지식한 패턴 검색 알고리즘(Brute Force)

```python
p = 'is'
t = 'this is a book'
m = len(p)
n = len(t)
def BruteForce(p,t):
  i = 0
  j = 0
  while j < m and i <= n - m:
  	if t[i] != p[j]:
    	i = i - j
      j = -1
    i = i + 1
    j = j + 1
  if j == m: return i - m
  else: return -1
```

- 최악의 경우 시간 복잡도 O(mn)







### 2. KMP 알고리즘

- 패턴으로 정보처리를 할 때, 패턴 매칭을 실패할 때 패턴을 활용할 정보가 충분히 있다??
- 시간 복잡도가 O(M + N)

- 접두어, 접미어를 활용

  - ex) abcdabcd 라면

  - 접두어는 a, ab, abc, abcd, abcda, abcdab
  - 접미어는 c,cb, cba



### 3. 보이어-무어 알고리즘

- 뒤에서 부터 보고, 스킵
- 만약 오른쪽 끝에 있는 문자가 찾아야 하는 문자 중에 있다면 그 문자 위치로 이동



### 암호화

##### 시저 암호화

##### bit열 암호화



### 문자열 압축

- BMP 압축 로직. (RRRRGGGGBB) => R4G4B2



허프만 트리??





# 8월 16일

### GNS 문제

딕셔너리는 해시 테이블

딕셔너리가 없다면 어떻게 풀겠는가?

#### 방법 1

```c
if (strcmp(arr,"zro")){
  int x = 0;
}
elif (strcmp(arr,"one")){
  x = 1;
} ..... 등등
```

일단 숫자로 매핑한 뒤, 퀵정렬로 정렬.  그리고 대응되는 문자열을 출력

- 이러면 과거엔 어드 못 땄음
- 어드 통과한 사람은 카운팅 정렬 사용 (범위가 다 정수형이고 범위가 정해져있는 경우에 카운팅 정렬이 더 빠른!!)



#### 방법 2. 카운팅 정렬

```python
def getidx(num):
  for i in range(10):
    if num[0] == p[i][0] and num[1] == p[i][1] and num[2] == p[i][2]:
      return i

for tc in range(1, TC + 1):
  temp = input()
  nums = input().split()
  cnt = [0] * 10
  for num in nums:
    cnt[getidx(num)] += 1
    
  ans = ''
  for i in range(10):
    ans += p[i] * cnt[i]
  print("#%d "% tc, ans)
```

시간을 줄일 수 있는 방법?



**공간을 팔아서 시간을 번다**



#### 방법 3. 공간을 파는 방법

```python
numidx = [[0] * 100 for _ in range(100)]
numidx[ord('Z')][ord('R')] = 0
numidx[ord('O')][ord('N')] = 1
numidx[ord('T')][ord('W')] = 2
numidx[ord('T')][ord('H')] = 3
numidx[ord('F')][ord('O')] = 4
numidx[ord('F')][ord('I')] = 5
numidx[ord('S')][ord('I')] = 6
numidx[ord('S')][ord('V')] = 7
numidx[ord('E')][ord('G')] = 8
numidx[ord('N')][ord('I')] = 9

p = ["ZRO ", "ONE ", "TWO ", "THR ", "FOR ", "FIV ", "SIX ", "SVN ", "EGT ", "NIN "]

TC = int(input())

for tc in range(1, TC + 1):

  temp = input()
  nums = input().split()

  cnt = [0] * 10

  for num in nums:
    cnt[numidx[ord(num[0])][ord(num[1])]] += 1

    ans = ''
    for i in range(10):
      ans += p[i] * cnt[i]
      print("#%d "%tc, ans)
```

자료를 잘 정리해서 빨리 뽑아내는 방법을 고안하는 것이 프로적인 마인드

만 개의 공간을 확보해서 열 개만 쓰겠다는 것

이진탐색이 계속 되면 차라리 이진탐색 트리를 쓰는 게 낫지 않을까? 라는게 프로의 마인드



