# 알고리즘 공부 팁

### 코딩 전에 분석부터

- 좁은 것에서부터 확장해 나갈 것

- 코딩부터 하는 건 나쁜 습관

- 슈도 코드로 먼저 짜서 손으로 직접 돌려봐라

- 문제를 **꼼꼼히** 읽어라. 처음부터 꼼꼼히 읽어서 한 번에 짜내는 것이 훠어얼씬 빠르다. 디자인은 *한 큐*에
  
  - 디버깅이 생각보다 오래걸린다.
  
- 파이썬을 세컨드 언어로 가지는 것
  
  - 파이썬으로 로직을 간단히 짜본 이후 C언어로 번역
  
- 처음과 끝을 생각하자.

- 신뢰할 수 있는 단위의 코드를 만들어라.
  
  - 평탄하게 만들어야 실수를 방지할 수 있다.
  
- 평이하게 짜야 디버깅하기도 편하고 나중에 보기도 편하다.

- 문제 범위를 꼼꼼히 읽어라. 최소값도 코너 케이스로 들어갈 수 있다. 
  
  - 반 이상을 최대 범위로 넣어서 견디는지 확인한다.
  
- 코드의 백업본을 반드시 만들어라

- 먼저 완전 검색으로 만들고, 가지치기는 이후에 생각하라

- 랜덤 함수로 tc를 다수 생성하여 에러를 확인하라

  ```python
  import sys
  import random
  sys.stdout = open("input.txt", "w")
  
  N = 8
  arr = [[0] * N for i in range(N)]
  
  print(N, N)
  for i in range(N):
      for j in range(N):
          t = random.randint(0, 2)
          if t == 2 and (i * j) % 10:
              t = 0
          elif t == 1 and (i * j) % 5:
              t = 0
          print(t, end = ' ')
      print()
  ```

  

- 실행시간을 확인해보라

  - Python

    1)

    ```python
    import time
    start = time.time() # 코드 시작시 시간을 기록
    # 코드 진행
    print(time.time() - start) # 종료 시간에서 시작 시간을 뺌
    ```

    2)

    ```python
    from datetime import datetime
    start = datetime.now()
    print(dtetime.now() - start)
    ```

  - CPP 실행시간 확인하기

    ```cpp
    #include <iostream>
    #include <ctime>
    using namespace std;
    int main() {
    	clock_t start = clock();
    	// 코드 실행
        // clock_t 를 int나 double로 바꿔도 상관 없음
    	cout << clock_t(clock() - start) << " ms";
    }
    ```

    

- DP 이전에 먼저 완전검색으로 통과될 수 있는 코드를 작성하라. 그리고 시간을 더 줄이기 위해 가지치기가 되었을 때, 재귀를 반복문으로 바꿀 것 (+ 메모이제이션)
- 완전탐색을 할 땐, 전처리를 어떻게(자료구조 생성), 후처리를 어떻게 해야할까.... 를 분리해서 생각하면 퍼포먼스가 좋은 코드를 낼 수 있다.

tc를 맞추고 나서 

완전 검색 하나 짜놓는다

tc 맞는지 확인

random 함수 확인해서 tc를 만들어라. 



### IM

- 함수를 쓰기보다 그냥 메인에서 한 번에 작성하자.
- 코드 길이, 시간 이런 거 신경 쓸 필요 전혀 없다.



### AD

- 완전탐색에서 가지치기를 해서 연산을 줄일 수 있는가(TSP, 배낭 문제)
  - 백트래킹의 완전탐색을 심도 깊게 이해하고, 거기서 정보를 제어하여 불필요한 연산을 줄이는 것
  - 필요한 정보를 계속 전달하여 가지치기에 활용하는 것이 어드의 덕목
- 테스트 케이스 중 정답의 개수를 알려주지 않는다. 그러므로 내가 정답인지 알 수 있을 정도로 로우하게 짜야 한다.

### Pro

- Do not Repeat



# 테스트케이스 생성하기

### python

```python
import sys
import random

sys.stdout = open('input.txt', 'w')

scope = 1000000

N = 100
T = 10
print(T)
for _ in range(T):
    print(N)
    for n in range(N):
        su = random.randint(1, 100)
        print(su, end=' ')
    print()
```



### CPP

```c++
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

void testcase() {
    // seed 생성
	srand(unsigned int(time(NULL)));
	freopen("input.txt", "w", stdout);
	int scope = 100;
	int T = 10;
	cout << T << "\n";
	for (int i = 0; i < T; i++) {
		cout << scope << "\n";
		for (int s = 0; s < scope; s++) {
			cout << rand() % 10 + 1 << " ";
		}
		cout << "\n";
	}
}

int main() {
    ios::sync_with_stdio(false);
	cin.tie(0);
    
	testcase();
}	
```







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
ary = [ [ 9, 20, 2, 18, 11 ],
				[ 19, 1, 25, 3, 21 ],
				[ 8, 24, 10, 17, 7 ],
				[ 15, 4, 16, 5, 6 ],
				[ 12, 13, 22, 23, 14 ] ]

sorted_ary = [[0  for _ in range(5)] for _ in range(5)]

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



- binary counting과 재귀를 통해 부분집합을 생성하자

  - 재귀가 더 빠르다. 재귀를 쓰자.

  ```python
  import datetime
  
  M = int(input())
  start = datetime.datetime.now()
  
  ########### binary counting을 통해 부분집합을 생성하는 로직
  lst = [i for i in range(1, M + 1)]
  for i in range(1 << M):
      arr = []
      for j in range(M):
          if i & (1 << j):
              arr += [lst[j]]
      # print(arr)
  
  ########### 재귀를 통해 부분집합을 생성하는 로직
  def subset(arr, depth):
      global count
      if depth == M:
          count += 1
          result = []
          for i in range(M):
              if arr[i]:
                  result += [lst[i]]
          # print(result)
      else:
          ar = arr[:]
          ar += [1]
          # 몇 번째 원소를 선택했을 경우
          subset(ar, depth + 1)
          ar = arr[:]
          ar += [0]
          # 몇 번째 원소를 선택하지 않았을 경우
          subset(ar, depth + 1)
  
  
  ############ 재귀가 더 빠르다.
  count = 0
  subset([], 0)
  print(count)
print(datetime.datetime.now() - start)
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







# 8월 21일

## Stack

### 응용

괄호를 조사하는 알고리즘

- 문자열에 있는 괄호를 차례대로 조사 
  - 왼쪽 괄호를 만나면 스택에 삽입
  - 오른쪽 괄호를 만나면 스택에서 top 괄호를 삭제한 뒤 오른쪽 괄호와 짝이 맞는지 확인
    - 스택이 비어있음 -> 조건 1또는 조건 2에 위배
    - 괄호의 짝이 맞지 않음 -> 조건 3에 위배
    - 문자열 끝까지 조사한 후에도 스택에 괄호가 남아있음 -> 조건 1에 위배



#### Memoization

가령 피보나치를 구하는 함수를 재귀함수로 작성할 경우, 엄청난 중복 호출이 발생한다.

- Memoization이란?

  - 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술 (동적계획법의 핵심)

    ```python
    피보나치의 예
    def fibo(n):
      global memo
      if n>=2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo(n-2))
      return memo[n]
    memo = [0,1]
    ```

    

### Dynamic Programming

- 탐욕 알고리즘처럼 최적화 문제를 해결하는 알고리즘
- 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결 
- 최종적으로 원래 주어진 입력의 문제를 해결

```python
피보나치에 DP를 적용
def fibo(n):
  f = [0,1]
  for i in range(2, n+1):
    f.append(f[i-1]+f[i-2])
  return f[n]
```



##### DP 의 구현 방식

- 재귀 방식
  - 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 overhead가 발생할 수 있음
- 반복 방식
  - Memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 DP를 구현하는 것이 성능 면에서 보다 효율적일 수 있다.





## DFS

스택식 방법

1) 재귀- 시스템 스택을 사용

-> 코드로 보고 대충 눈으로 보면 안 됨. 코드의 흐름을 완벽하게 이해하고 있어야 한다. 리턴 지점.







# 8월 22일

#### 스택구현

- Python

  ```python
  stack = [0] * 10
  top = -1
  
  for i in range(3):
      stack[top + 1] = i
      top += 1
  
  for i in range(3):
      t = stack[top]; top -= 1
      print(t)
  ```

- CPP

  ```cpp
  class node {
  public:
  	int data;
  	node *prev;
  	node *next;
  	node(int data) {
  		this->data = data;
  		this->prev = NULL;
  		this->next = NULL;
  	}
  };
  
  class stack {
  private:
  	int size;
  	node *head;
  	node *tail;
  public:
  	stack() {
  		this->size = 0;
  		this->head = NULL;
  		this->tail = NULL;
  	}
  	void push(int data) {
  		node *element = new node(data);
  		if (size == 0) {
  			this->head = element;
  			this->tail = element;
  			this->size++;
  		}
  		else {
  			element->prev = this->tail;
  			this->tail->next = element;
  			this->tail = element;
  			this->size++;
  		}
  	}
  
  	int SIZE() {
  		return this->size;
  	}
  
  	int pop() {
  		int result;
  		if (this->size == 1) {
  			result = this->head->data;
  			delete this->head;
  			this->head = NULL;
  			this->tail = NULL;
  		}
  		else {
  			result = this->tail->data;
  			this->tail = this->tail->prev;
  			delete this->tail->next;
  		}
  		this->size--;
  		return result;
  	}
  };
  ```



#### 재귀구현

- Python

  ```python
  def DFSr(v):
      visited[v] = True
  
      for i in range(1, 8):
          if G[v][i] and not visited[i]:
              DFSr(i)
  ```

- CPP

  ```cpp
  void DFS(int node) {
  	visited[node] = true;
  	for (int i = 0; i < N; i++) {
  		if (G[node][i] == 1 && visited[i] == false) {
  			DFS(i);
  		}
  	}
  }
  ```

  



#### 괄호검사

```python
stack = [0] * 100
top = -1
str = "(()()))"

wrong = 0
for i in range(len(str)):
    if str[i] == '(':
        top += 1; stack[top] = str[i]
    elif str[i] == ')':
        if top == -1:
            wrong = 1
            break
        if stack[top] == '(':
            top -= 1

if top == -1 and not wrong : print("correct!")
else: print("wrong!")
```



```DFS
def DFS(v):
    visited = [0] * (8)
    stack = [0] * 10
    top = -1

    top += 1
    stack[top] = v

    while top != -1:
        v = stack[top]
        top -= 1
        if visited[v] != 1:
            visited[v] = 1
            print(v)
            for i in range(1, 8):
                if G[v][i] and not visited[i]:
                    top += 1
                    stack[top] = i

edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
G = [[0]* (8) for _ in range(8)]


for i in range(0, len(edges), 2):
    G[edges[i]][edges[i+1]] = 1
    G[edges[i+1]][edges[i]] = 1

DFS(1)


# ------------------------------------------------------------------



def DFSr(v):
    print(v)
    visited[v] = True

    for i in range(1, 8):
        if G[v][i] and not visited[i]:
            DFSr(i)


edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
visited = [0] * 8
G = [[0] * 8 for _ in range(8)]

for i in range(0, len(edges), 2):
    G[edges[i]][edges[i+1]] = 1
    G[edges[i+1]][edges[i]] = 1

DFSr(1)
```





#### 연습문제 3



#### Ladders 1

```python
import sys
sys.stdin = open("input.txt", "r")

def check(x, y):
    if x < 0 or x > 99 : return False
    if y < 0 or y > 99 : return False

    if mat[x][y] : return True
    else : return False

def solve( ):
    s = 0
    while True:
        if mat[99][s] == 2: break
        s += 1

    x = 99
    y = s
    d = 0       # -1(왼쪽), 0(위), 1(오른쪽)

    while x != 0 :
        if   ((d == 0 or d == -1) and check(x, y - 1)) : d = -1; y -= 1
        elif ((d == 0 or d ==  1) and check(x, y + 1)) : d =  1; y +=1
        else :	d = 0; x -= 1

    return y;


for tc in range(1, 11):
    input()
    mat = [0] * 100
    for i in range(100):
        mat[i] = list(map(int, input().split()))

    print('#%d'%tc, solve( ))
```







#### 작업경로

- AOV (Activity on Vertex) : 위상정렬

  작업의 단계에 대한 것.

  1 -> 2 -> 3

  2 작업을 위해선 반드시 1을 끝내야 한다.

  그런데 

  1 -> 2 -> 3

     4 / 

  이런 경우엔 => (1,4,2,3) (4,1,2,3) 두 경우 가능



​		정점에 붙어있는 간선의 개수를 degree(''차수''라 함)

​		-> 방향 그래프의 경우. 진입차수와 진출차수가 있음 -> 진입차수를 소거하며 가면 됨



​		=> 엣지의 방향을 바꾼다!

​		그리고 not visited 부터 출발한다.

- AOE(Activity on Edges) : 임계경로





# 8월 26일 월요일

## 문제 리뷰

### 1. 종이 붙이기

점화식으로 해결

-> DP. 메모이제이션

- 재귀적

  ```python
  def fr(n):
      if n == 1 : return 1
      if n == 2 : return 3
  
      return fr(n - 1) + 2 * fr(n - 2)
  
  
  def fm(n):
      if DP[ n ]: return DP[n]
      DP[ n ] = fm(n - 1) + 2 * fm(n - 2)
      return DP[n]
  
  
  def fi():
      dp = [0] * 101
      dp[1] = 1
      dp[2] = 3
  
      for i in range(2, 101):
          dp[i] = dp[i-1] + 2 * dp[i-2]
  
  DP = [0] * 101
  DP[1] = 1
  DP[2] = 3
  
  T = int(input())
  for tc in range(1, T + 1):
      N = int(input()) // 10
      print('#%d'%tc, fm(N))
  ```



- 메모리로 저장

  
  
  

### 2. 괄호 이어붙이기

1) stack 비어있냐?

2) 같은 종류냐?

3) stack에 남아있냐?

```python
stack = [0] * 100
top = -1

def solve():
    global top
    for i in range(len(str)):
        if str[i] == '{' or str[i] == '(':
            stack[top + 1] = str[i]
            top += 1
        elif str[i] == '}' or str[i] == ')' :
            if top == -1 : return 0
            if (str[i] == '}' and stack[top] == '(') or (str[i] == ')' and stack[top] == '{'):
                return 0
            top -= 1

    if top == -1 : return 1
    else : return 0

T = int(input())
for tc in range(1, T+1):
    s = list()
    str = input()

    print('#%d'%tc, solve())
    top = -1
```







### 3. 그래프 경로

- 타겟정점인지 계속 조사. 맞으면 리턴하고 끝

- 스택과 visited를 만들고 함.

  ```python
  def DFS(v, END):
      visited = [0] * (V + 1)
      stack = []
  
      stack.append(v)
  
      while stack:
          v = stack.pop(-1)
  
          if visited[v] != 1:
              visited[v] = 1
              if v == END: return 1
              for i in range(1, V + 1):
                  if G[v][i] and not visited[i]:
                      stack.append(i)
      return 0
  
  
  T = int(input())
  for tc in range(1, T + 1):
      V, E = map(int, input().split())
  
      G = [[0] * (V + 1) for _ in range(V + 1)]
  
      for _ in range(E):
          s, t = map(int, input().split())
          G[s][t] = 1
      start, end = map(int, input().split())
  
      print('#%d' % tc, DFS(start, end))
  ```

- 재귀로 짜면

  ```python
  def DFSr(v):
      global found
      if v == end : found = 1; return
      visited[v] = True
  
      for i in range(1, V + 1):
          if G[v][i] and not visited[i] and not found:
              DFSr(i)
   
   
  T = int(input())
  for tc in range(1, T + 1):
      V, E = map(int, input().split())
      visited = [0] * (V + 1)
      G = [[0] * (V + 1) for _ in range(V + 1)]
   
      for _ in range(E):
          s, t = map(int, input().split())
          G[s][t] = 1
      start, end = map(int, input().split())
  
      found = 0
      DFSr(start)
      print('#%d'%tc, found)
  ```

  







### 4. 반복문자 지우기

- 스택을 활용해서 만들기
  - 문자들을 하나씩 넣으면서 검사. 이전에 넣은 것과 같으면 pop 하겠다는 것. 다르면 넣음

```python
stack = [0] * 1000
top = -1

T = int(input())
for tc in range(1, T+1):
    str = input()

    top += 1;    stack[top] = str[0]

    for i in range(1, len(str)):
        if stack[top] == str[i] : top -= 1
        else : top += 1;    stack[top] = str[i]

    print('#%d'%tc, top+1)
    top = -1
```





*** 선생님 코드 반드시 확인

### 5. 작업순서



#### 1) C 스타일 식

- 진입 차수
- 진출 차수

를 활용해서 한 번에 처리하기

- 진입차수가 0인 곳에서부터 출발하면 된다!!

```python
for tc in range(1, 11):
    V, E = map(int, input().split())
    G = [[0] * (V + 2) for _ in range(V + 2)] # G[x][0] 진입차수 G[x][1] 진출 차수
    stack = [0] * 1000
    top = -1

    edges = list(map(int, input().split()))
    for i in range(E):
        u, v = edges[i*2: i*2 + 2]
        G[u][1] += 1
        G[u][G[u][1]+1] = v
        G[v][0] += 1

    for i in range(1, V + 1):
        if G[i][0] == 0:
            top += 1
            stack[top] = i

    print("#%d"%tc, end=' ')

    while top != -1:
        x = stack[top]
        top -= 1
        print("%d"%x, end=' ')
        for i in range(G[x][1]):
            G[G[x][2 + i]][0] -= 1
            if G[G[x][2 + i]][0] == 0:
                top += 1
                stack[top] = G[x][2 + i]

    print()
```





#### 2) 재귀로 짜기

- 진입과 진출의 방향을 바꾼다.

```python
def DFSr(v):
    for i in range(cnt[v]):
        if visited[G[v][i]] == 0 : DFSr(G[v][i])

    visited[v] = 1
    print("%d" % v, end=' ')

for tc in range(1, 11):
    V, E = map(int, input().split())
    G = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
    cnt = [0] * (V + 1)

    edges = list(map(int, input().split()))
    for i in range(E):
        u, v = edges[i*2: i*2 + 2]
        G[v][cnt[v]] = u
        cnt[v] += 1

    print("#%d"%tc, end=' ')

    for i in range(1, V+1):
        if visited[i] == 0:
            DFSr(i)

    print()
```





## 스택 2

- 계산기로 스택으로 만들 수 있다?
- 스택을 이용해서 재귀 호출을 할 수 있다?
  - 재귀 호출을 백트래킹으로 만드는데 어떻게 동작하는가?
- 분할정복 프레임
  - 자귀로 작성할 수 있다.



-> 굉장히 좋은 접근 방법. 프로의 덕목. **수행시간을 줄일 수 있는 것**



### 스택을 활용한 계산기

- 토큰 어낼라이징

  - 토큰이란? 의미가 있는 가장 작은 단위

    ex) 4 + 3 * 5에서는 토큰이 5개

- 이항 연산자일 경우

  - 중위 표기법: A + B
  - 전위 표기법: + A B
  - 후위 표기법: A B +

  => 중위 표기법으로 기술한 것을 후위 표기법으로 전환을 해서 계산한다.

  => 이때 사용하는 것이 스택.

  => 후위 표기법을 스택으로 구현



#### 후위표기법으로 바꾸기

1. step1
   1. 입력 받은 중위 표기식에서 토큰을 읽는다.
   2. 토큰이 피연산자이면 토큰을 출력한다.
   3. 토큰이 연산자(괄호 포함)일 때. 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push 하고, 그렇지 않아면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop한 후 토큰의 연산자를 push 한다. 만약 top에 연산자가 없으면 push 한다.
   4. 토큰이 오른쪽 괄호 ')'이면 스택 top에 왼쪽 괄호 '('가 올 때까지 스택에 pop 연산을 수행하고 pop 한 연산자를 출력한다. 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않는다.
   5. 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 1부터 다시 반복한다.
   6. 스택에 남아있는 연산자를 모두 pop하여 출력한다.
      - 스택 밖의 왼쪽 괄호는 우선 순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮다.

- 왼쪽 괄호는 인커밍 스택할 때는 우선순위가 최고인데 스택 안에 들어가면 그냥 호구가 됨
- 오른쪽 괄호가 오면 페어 사이에 있는 연산자들을 모두 빼낸다.

- 연산자가 있으면 무조건 스택에 넣는다.



## 백트래킹

- 백트리캥 기법은 해를 찾는 도중에 '막히면' (즉, 해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법이다.

  - 더이상 해를 생성할 수 없으면 다시 해를 찾아간다. (재귀 DFS와 같다.)

- 백트래킹 기법은 최적화 문제와 결정 문제를 해결할 수 있다.

- 결정 문제: 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes' 또는 'no'가 답하는 문제

  - 미로 찾기
  - n-Queen 문제
  - Map coloring
  - 부분 집합의 합(subset sum) 문제 등

  => 경우의 수를 따지는 문제. 백트래킹을 많이 쓴다.







-- 백트래킹은 DFS와 비슷

#### 미로 찾기

되추적. back-track

- DFS의 재귀 버전과 똑같다.



##### 백트래킹과 깊이우선탐색의 차이?

- 각 노드에서 가능성을 생성해서 가는데... 이 생성하는 노드가 갈 필요가 없으면 진행을 하지 않는 것(가지치기 Prunning) -> 가지치기를 해야 백트래킹이라는데.. 사실상 DFS



##### 가지치기. Prunning

- 백트래킹 기법
  - 어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감
- 절차
  1. 상태 공간 트리의 깊이 우선 검색을 실시
  2. 각 노드가 유망한지를 점검
  3. 만일 그 노드가 유망하지 않으면 그 노드의 부모 노드로 돌아가서 검색을 계속한다ㅏ.



#### N-queen

- 완전 검색을 하려면...  8x8 일때.... 64C8 -> 무지무지 많음

- 백트래킹과 가지치기를 이용해서 조사를 하는 방법이 있다

  - 같은 줄에 2개 이상의 퀸이 있으면 안 되니, 한 줄에는 하나의 퀸만 두자

    -> 4 x 4의 경우엔 총 256가지

  ```python
  def checknode(v):
    if promising(v): # 진행해도 되는지 검사
      if there is a solution at v:# 우리가 찾으려던 것이냐?
        write the solution
      else:
        for u in each child of v: # 자식 노드들을 하나씩 생성해서 그 노드를 기반으로 해를 조사한다ㅏ.
          checknode(u)
  ```

  여기에 4퀸 문제를 대입해보자.

  문제마다 promising의 조건이 모두 다르다.

  



#### 부분집합 구하기

순열을 사용해서 부분집합을 구해보자.

- 선택 유무에 대한 정보를 가지고 있다.
  - APS 응용 174쪽 참고

- 가지치기를 제어할 줄 아느냐? 

 



각 요소들의 포함 여부를 검색하는 게 아니라...







#### 연습문제

{1,2,3,4,5,6,7,8,9,10}의 powerset중 원소의 합이 10인 부분집합을 출력하면?

- 



- 계산 결과.... 2047개가 나온다. 왜? 맨 밑은 2^10이다. 그 위는 무조건 하나 적다.
- 누적되어온 값을 넘겨주게 되면 합이 10보다 커졌을 땐 나머지 부분은 자를 수 있다.
- 







## 분할 정복

- 분할(divide) : 문제를 작은 부분으로 나눈다.
- 정복(conquer) : 나누고 작은 문제로 각각 해결
- 통합(combine) : 해결된 해답을 모은다.

 

### 예제

#### 거듭제곱

- for문으로 작성
- 재귀문으로 작성



#### 퀵 정렬

- 퀵정렬일 땐 nlogn인데.. 악의적인 데이터가 들어올 경우 n^2. 일반적으로는 sorting 알고리즘 중에는 빠른 알고리즘이다.

- pivot을 기준으로 큰 놈은 오른쪽으로, 작은 놈은 왼쪽으로 보내겠다는 것

  -> pivot의 위치는 나중에 정렬되도 그 위치가 맞다.

```python
def quicksort(a, begin, end):
  if begin < end:
    p = partiton(a, begin, end) # 두 부분으로 쪼갬
    quicksort(a, begin, p-1)
    quicksort(a, p+1, end)
```







# 8월 27일

### magnetic







# 8월 28일

## 문제 리뷰

### forth

```python
top = -1
for x in post_exp:
  if x in ('+','-','*','/'):
    if top < 1 : print('error'): break
    if x  == ''
```

코드 복사





### maze

상태 공간 트리를 정확하게 알아야 한다.

=> 생성하는 과정이 자신의 머리 속에 그려져야 한다. 재귀를 깊은 수준으로 돌아가는 것을 이해해야 한다.



### 가위바위보



### 배열 부분 합

-> 순열임을 파악해야 한다! 

`모든 수의 조합을 생성하면 되겠구나` 라는 생각이 들어야 한다. (겹치면 안 되기 때문에 중복 순열, 중복 조합은 아니다.) 그런데 순서가 바뀌면 값이 바뀌기 때문에 `순열`로 해결하면 된다.

백트래킹 : 필요한 정보를 계속 전달하여 가지치기에 활용하는 것이 어드의 덕목



### 계산기

- 중위 연산을 후위 연산으로 바꾸기 위해선, 연산자를 스택에 쌓아야 한다. 스택에 있는 연산자보다 우선순위가  높을 땐 스택에 쌓고 낮을 땐 밑에 있는 연산자를 뺀다.
- 후위 연산을 계산하려면 스택에 숫자를 쌓아야 한다. 연산자를 만나면 스택에서 2개를 꺼내 연산한다.





## 큐

- 큐의 문제를 해결하기 위해 modula 연산을 통해 인덱스를 통제한다.

```python
# Q = [0] * 10
# f = r = -1
# def isEmpty() :
# 	return f == r
#
# def isFull() :
# 	return r == len(Q) - 1
#
# def enQ(item) :
# 	global r
# 	if isFull() : print('Queue_Full')
# 	else :
# 		r += 1
# 		Q[r] = item
#
# def deQ():
#     global f
#     if isEmpty() : print('Queue_Empty')
#     else :
#         f += 1
#         return Q[f]
#
# enQ(1)
# enQ(2)
# enQ(3)
# print(deQ())
# print(deQ())
# print(deQ())


Q = [0] * 10
f = r = -1
r += 1; Q[r] = 1
r += 1; Q[r] = 2
r += 1; Q[r] = 3

f += 1; print(Q[f])
f += 1; print(Q[f])
f += 1; print(Q[f])
```





## 링크드 리스트





## 우선순위 큐







#### 마이쮸 문제

```python
N = int(input())
que = []
que.append(1)
for i in range(2, N + 1):
    t = que.pop(0)
    que.append(t)
    que.append(i)
print(que)
```



```python
q = [0] * 100
f = r = -1
candis = 20
studcan = [1] * 20

sn = 1
nextsn = 2

r += 1; q[r] = sn

while candis > 0:
    f += 1;  sn = q[f]
    candis -= studcan[sn]
    studcan[sn] += 1

    if candis <= 0:
        print("%d번 학생이 마지막 사탕을 받아간다."%sn)
        break

    r += 1; q[r] = sn
    r += 1; q[r] = nextsn

    nextsn += 1


#
# q = [0] * 100
# f = r = -1
# candis = 20
# studcan = [1] * 20
#
# sn = 1
# nextsn = 2
#
# r += 1; q[r] = sn
# print("==>%d번 학생 : 입장하여 줄을 선다."%sn)
# print("학생 줄 : " , q[f+1:r+1])
#
# f += 1; sn = q[f]
# print("%d번 학생 : 줄에서 나와..."%sn)
# print("학생 줄 : " , q[f+1:r+1])
#
#
# while candis > 0:
#     if candis > studcan[sn] : candis -= studcan[sn]
#     else: studcan[sn] = candis; candis -= studcan[sn]
#     print("%d번 학생 : 선생님한테 사탕 %d개를 받는다."%(sn, studcan[sn]))
#     print("===== 남은 사탕의 개수는 %d개다."%candis)
#     print()
#     studcan[sn] += 1
#
#     if candis <= 0:
#         print("%d번 학생이 마지막 사탕을 받아간다."%sn)
#         break
#
#     r += 1; q[r] = sn
#
#     print("%d번 학생 : 다시 줄을 선다."%sn)
#     print("학생 줄 : ", q[f + 1:r + 1])
#     print("==> %d번 학생 : 입장하여 줄을 선다."%nextsn)
#
#     r += 1; q[r] = nextsn;
#     print("학생 줄 : ", q[f + 1:r + 1])
#
#     nextsn += 1
#     f += 1; sn = q[f]
#     print("%d번 학생 : 줄에서 나와..."%sn)
#     print("학생 줄 : ", q[f + 1:r + 1])
```







## BFS Breath First Search

큐에 레벨을 넣어서 처리하자.



어드 카드 셔플 문제. 중복 순열



- front 와 rear를 활용한 que BFS

```python
G = [
 [ 0, 0, 0 ],
 [ 2, 3, 0 ],   #정점 1의 인접정점
 [ 1, 4, 5 ],   #정점 2의 인접정점
 [ 1, 7, 0 ],   #정점 3의 인접정점
 [ 2, 6, 0 ],   #정점 4의 인접정점
 [ 2, 6, 0 ],   #정점 5의 인접정점
 [ 4, 5, 7 ],   #정점 6의 인접정점
 [ 3, 6, 0 ]]   #정점 7의 인접정점

q = [0] * 10
visited = [0] * 8

def BFS(w):
    f = r = -1
    r += 1; q[r] = w

    print("%d"%q[r])
    visited[w] = 1;

    while f != r:
        f += 1; w = q[f]
        for i in range(3):
            if G[w][i] and not visited[G[w][i]]:
                r += 1; q[r] = G[w][i]
                print("%d"%q[r])
                visited[G[w][i]] = 1

BFS(1)


```







# 8월 29일

기본 연습문제 3

- 방문처리를 하는 것... 넣을 때 하는 게 아니라, 뺄 때 하라고?? 리던던시가 생긴다는데 이것이 무슨 의미인가...?
  - 넣는 순간 visited 처리를 해야 리던던시가 안 생기는데??
- 소소한 것으로부터 동작을 손으로 짜봐야 한다.



## 조합 생성하기

- N 개의 수 중, M 개를 선택하기
  - 중복을 피하기 위해 먼저 고른 것보다 무조건 더 큰 수 중에 선택하였다.

```python
import copy

N, M = map(int, input().split())
size = M
count = 0


def select(arr, n):
    global count
    if n == size:
        count += 1
        print('{} : {}'.format(count, arr))
        return
    else:
        depth = n + 1
        if not arr: # arr가 비어있을 경우 아무거나 선택
            for i in range(N): 
                ar = copy.deepcopy(arr)
                ar.append(i)
                select(ar, depth)
        else:
            for i in range(arr[-1] + 1, N):
                ar = copy.deepcopy(arr)
                ar.append(i)
                select(ar, depth)


select([], 0)
```



- 조합 코드

```python
M, N = map(int, input().split())
arr = [i for i in range(1, M + 1)]
visited = [0] * M
count1 = count2 = 0

def combi(lst, depth, last):
    global count2
    if depth == N:
        count2 += 1
        print('c', count2, ':', lst)
    else:
        for i in range(last, M):
            if not visited[i]:
                visited[i] = 1
                ar = lst[:]
                ar.append(arr[i])
                combi(ar, depth + 1, i)
                visited[i] = 0
combi([], 0, 0)
```



- 조합 코드 without visited

```python
M, N = map(int, input().split())
arr = [i for i in range(1, M + 1)]
visited = [0] * M
count = 0

def combi(lst, depth, last):
    global count
    if depth == N:
        count += 1
        print('c', count, ':', lst)
    else:
        for i in range(last + 1, M):
            ar = lst[:]
            ar.append(arr[i])
            combi(ar, depth + 1, i)


combi([], 0, -1)
```



## 중복조합 생성하기

- 중복조합 H(n, r) = C(n + r - 1, r)



- 중복조합 without visited

```python
M, N = map(int, input().split())
arr = [i for i in range(1, M + 1)]
visited = [0] * M
count1 = count2 = 0

def combi(lst, depth, last):
    global count2
    if depth == N:
        count2 += 1
        print('c', count2, ':', lst)
    else:
        for i in range(last, M):
            ar = lst[:]
            ar.append(arr[i])
            combi(ar, depth + 1, i)


combi([], 0, 0)
```







## 순열 생성하기

- N개의 수 중 M개를 선택하되 순서가 중요함

```python
from copy import deepcopy

N, M = map(int, input().split())
size = M
count = 0
visited = [0] * (N + 1)


def select(arr, visit, n):
    global count
    if n == size:
        count += 1
        print('{} : {}'.format(count, arr))
        return
    else:
        depth = n + 1
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                ar = copy.deepcopy(arr)
                ar.append(i)
                select(ar, visit, depth)
                visited[i] = 0


select([], visited, 0)
```





## 중복 순열 생성하기

- N^M 만큼 찾기

```python
import copy

N, M = map(int, input().split())
size = M
count = 0


def select(arr, n):
    global count
    if n == size:
        count += 1
        print('{} : {}'.format(count, arr))
        return
    else:
        depth = n + 1
        for i in range(N):
            ar = copy.deepcopy(arr)
            ar.append(i)
            select(ar, depth)


select([], 0)
```





### 조합 중복조합 순열 중복순열 끝판왕

```python
def permu(arr, depth):
    global count
    if depth == M:
        count += 1
        print('p', count, ':', arr)
    else:
        for i in range(N):
            if not visited[i]:
                ar = arr[:]
                visited[i] = 1
                ar.append(i)
                permu(ar, depth + 1)
                visited[i] = 0


def permu_repet(arr, depth):
    global count
    if depth == M:
        count += 1
        print('pr', count, ':', arr)
    else:
        for i in range(N):
            ar = arr[:]
            ar.append(i)
            permu_repet(ar, depth + 1)


def combi(arr, depth, last):
    global count
    if depth == M:
        count += 1
        print('c', count, ':', arr)
    else:
        for i in range(last, N):
            ar = arr[:]
            ar.append(i)
            combi(ar, depth + 1, i + 1)


def combi_repet(arr, depth, last):
    global count
    if depth == M:
        count += 1
        print('cr', count, ':', arr)
    else:
        for i in range(last, N):
            ar = arr[:]
            ar.append(i)
            combi_repet(ar, depth + 1, i)


N, M = map(int, input().split())
count = 0
visited = [0] * N
# combi([], 0, 0)
# permu([], 0)
# combi_repet([], 0, 0)
# permu_repet([], 0)
```





### 순열 중복 라이브러리

```python
from itertools import permutations
per = permutations([1,2,3],2)
print(list(per))
#[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

from itertools import product
per = product([1,2,3],repeat=2)
print(list(per))
#[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]


from itertools import combinations
print(list(combinations([1,2,3],2) ) )
#[(1, 2), (1, 3), (2, 3)]

from itertools import combinations_with_replacement
print( list ( combinations_with_replacement([1,2,3],2) ) )
#[(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
```



### 순열과 중복. 선생님 조언

```python
'==================== 순열 ========================='
def perm_i():
    for i1 in range(1, N + 1):
        for i2 in range(1, N + 1):
            if i2 != i1:
                print(i1, i2)
'''
1 2
1 3
2 1
2 3
3 1
3 2
'''

def perm_r(k):
    if k == R :
        print(t[0], t[1])
    else:
        for i in range(N):
            if visited[i]: continue
            t[k] = i + 1
            visited[i] = 1
            perm_r(k + 1)
            visited[i] = 0
'''
1 2
1 3
2 1
2 3
3 1
3 2
'''


'==================== 조합 ========================='


def comb_i():
    for i in range(N - 1):
        for j in range(i + 1, N):
            print(a[i], a[j])

'''
1 2
1 3
2 3
'''

def comb_r(k, s):
    if k == R: print(t[0], t[1])
    else:
        for i in range(s, N + (k - R) + 1):
            t[k] = a[i]
            comb_r(k + 1, i + 1)
'''
1 2
1 3
2 3

'''


'===================== 중복 순열 ========================='

def pi_i():
    for i in range(N):
        for j in range(N):
            print(a[i], a[j])

'''
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
'''

def pi_r(k):
    if k == R: print(t[0], t[1])
    else:
        for i in range(N):
            t[k] = a[i]
            pi_r(k + 1)

'''
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
'''


'====================== 중복 조합 ========================'

def H_i():
    for i in range(N):
        for j in range(i, N):
            print(a[i], a[j])

'''
1 1
1 2
1 3
2 2
2 3
3 3
'''

def H_r(k, s):
    if k == R: print(t[0], t[1])
    else:
        for i in range(s, N):
            t[k] = a[i]
            H_r(k + 1, i)
'''
1 1
1 2
1 3
2 2
2 3
3 3
'''

'====================== 호출 ========================'
N = 3
R = 2
a = [1, 2, 3]
t = [0] * R


t = [0] * N
visited = [0] * N
print()
print("순열")
perm_i()
print("----------")
perm_r(0)
print("----------")

print()
print('조합')
comb_i()
print("----------")
comb_r(0, 0)

print()
print("중복 순열")
pi_i()
print("----------")
pi_r(0)

print()
print("중복 조합")
H_i()
print("----------")
H_r(0, 0)
```





# 9월 2일

- 큐의 의미. 최단 거리를 구할 수 있는 BFS를 구현할 수 있다.



## 지난주 문제 풀이

### 회전 문제

모듈라 연산을 사용하면 바로 풀림





노드의 거리, 플로이드-워셔 알고리즘

### 노드의 거리

```python
import sys
sys.stdin = open('input.txt', 'r')

def BFS(v):
    f = r = -1
    r += 1; q[r] = v

    visited[v] = 1;

    while f != r:
        f += 1; v = q[f]
        for i in range(1, V + 1):
            if G[v][i] and visited[i] == 0:
                if end == i:
                    return visited[v]
                r += 1; q[r] = i
                visited[i] = visited[v] + 1
    return 0

q = [0] * 1000
for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    visited = [0] * (V + 1)
    G = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        s, t = map(int, input().split())
        G[s][t] = G[t][s] = 1
    start, end = map(int, input().split())

    print('#%d'%tc, BFS(start))





for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    dist = [[1000] * V for _ in range( V )]

    for _ in range(E):
        s, t = map(int, input().split())
        dist[s - 1][t - 1] = dist[t - 1][s - 1] = 1

    start, end = map(int, input().split())

    for k in range(V):
        for i in range(V):
            if i == k : continue
            for j in range(V):
                if j == k or j == i: continue
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    if dist[start - 1][end - 1] == 1000:
        print("#%d" % tc, 0)
    else:
        print("#%d"%tc, dist[start - 1][end - 1])
```





### 미로의 거리

```python
def bfs1():
    q = []

    maze[sX][sY] = 1
    q.append([sX, sY, 0])

    while q:
        x, y, depth = q.pop(0)
        for dx, dy in (0,1),(0,-1),(1,0),(-1,0):
            xx = x + dx
            yy = y + dy
            if 0 <= xx < N and 0 <= yy < N:
                if maze[xx][yy] == 3:
                    return depth
                if maze[xx][yy] == 0:
                    maze[xx][yy] = 1
                    q.append([xx, yy, depth + 1])
    return 0


def bfs():

    visited = [[0] * N for _ in range(N)]
    q = []
    q.append([sX, sY])
    visited[sX][sY] = 0

    while len(q) != 0:
        x, y = q.pop(0)
        for dx, dy in (0,1),(0,-1),(1,0),(-1,0):
            newX = x + dx
            newY = y + dy
            if 0 <= newX < N and 0 <= newY < N :
                if maze[newX][newY] == 3:
                    return visited[x][y]
                elif maze[newX][newY] == 0 and visited[newX][newY] == 0:
                    q.append([newX, newY])
                    visited[newX][newY] = visited[x][y] + 1
    return 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    maze = [[int(x) for x in input()] for _ in range(N)]
    for i in range(N):
        if 2 in maze[i]:
            sX = i
            sY = maze[i].index(2)
    print('#%d'%tc, bfs1())
```



### 피자굽기

```python
import sys
sys.stdin = open('input.txt', 'r')


# 원형큐
def solve1():
    rq = [0] * (N + 1)
    f = r = 0

    for pid in range(1, N + 1):
        rq[pid] = [pid, pizzas[pid - 1]]

    r = N
    nextp = N

    while f != r:
        f = (f + 1) % (N + 1)
        pid, pcheez = rq[f]
        if pcheez // 2 != 0:
            pcheez //= 2
            r = (r + 1) % (N + 1)
            rq[r] = [pid, pcheez]
        elif nextp < M:
            r = (r + 1) % (N + 1)
            rq[r] = [nextp, pizzas[nextp]]
            nextp += 1

    return pid + 1


# 선형 큐
def solve():
    q = [0] * 1000
    f = r = -1

    for i in range(N): 
        q[i] = i
    r += N
    nextp = N

    while f != r:
        f += 1
        pid = q[f]
        if pizzas[pid] // 2 != 0:
            pizzas[pid] //= 2
            r += 1
            q[r] = pid
        elif nextp < M:
            r += 1
            q[r] = nextp
            nextp += 1

    return pid + 1



for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())    # 화덕의 크기 N, 피자 개수 M
    pizzas = list(map(int, input().split()))
    print('#%d'%tc, solve1())
```





### contact 문제

que에 집어넣을 때 -1을 마커로 활용하여 깊이를 관리

```python
import sys
sys.stdin = open('input.txt', 'r')


def BFS(v):
    ans = f = r = -1
    visited = [0] * 101

    r += 1; q[r] = v
    visited[v] = 1;
    r += 1; q[r] = -1       # 같은 레벨 마크

    while True:
        f += 1; v = q[f]
        if ans < v : ans = v

        if v == -1:
            if f == r : return ans
            r += 1; ans = q[r] = -1
            continue

        for i in range(G[v][0]):
            if not visited[G[v][i + 1]]:
                visited[G[v][i + 1]] = 1
                r += 1; q[r] = G[v][i + 1]

q = [0] * 200
for tc in range(1, 11):
    N, S = map(int, input().split())
    G = [[0] * 100 for i in range(101)]
    edges = list(map(int, input().split()))

    for i in range(N//2):
        u, v = edges[i*2: i*2 + 2]
        G[u][0] += 1
        G[u][G[u][0]] = v

    print('#%d'%tc, BFS(S))
```







## 리스트

- 자료의 논리적인 순서와 메모리 상의 물리적인 순서가 일치하지 않고, 개별적으로 위치하고 있는 원소의 주소를 연결하여 하나의 전체적인 자료구조를 이룬다.

- 링크를 통해 원소에 접근하므로, 순차 리스트에서처럼 물리적인 순서를 맞추기 위한 작업이 필요하지 않다.
- 자료구조의 크기를 동적으로 조정할 수 있어, 메모리의 효율적인 사용이 가능하다.



### 삽입정렬

O(n^2)

자료들을 일일이 옮겨야 하는데, 데이터가 많을 경우 링크드 리스트를 사용한다. 조사하는 건 어쩔 수 없다.



### 병합정렬

O(n log n)



### 우선순위 큐







# 9월 3일

## 문제풀이

#### 치즈문제

신뢰할 수 있는 단위의 코드를 만들어라.

평탄하게 만들어야 실수를 방지할 수 있다.

- 공기를 전부 2로 만듦. 
- 치즈를 찾음. 상하좌우를 조사하며 2를 찾음. 공기에 닿은 치즈는 3으로, 닿지 않은 치즈는 4로 바꿈
- 2나 3으로 된 거를 0으로 바꿈

10,000이면 부담스럽기 때문에 BFS로 돌림

평이하게 짜야 디버깅하기도 편하고 나중에 보기도 편하다.



### 완전탐색 부분집합

```python
def solve(k, sum):
    global cnt
    cnt += 1
    if k == N:
        if sum == 10:
            for i in range(1, 11):
                if a[i] == True:
                    print(i, end=' ')
            print()
    else:
        k += 1
        # if sum + k <= 10 :
        #     a[k] = 1; backtrack(k, sum + k)

        a[k] = 1; backtrack(k, sum + k)
        a[k] = 0; backtrack(k, sum)

N = 10
a = [0] * (N + 1)

cnt = 0
solve(0, 0)
print("cnt : ", cnt)
```



### 퇴사

```python
def solve(k):
    global ans
    if k == N:
        for i in range(N):
            if Si[i]:
                for j in range(i + 1, i + Ti[i]):
                    if j >= N or Si[j] : return

        tsum = 0
        for i in range(N):
            if Si[i]:
                tsum += Pi[i]
        if tsum > ans : ans = tsum

    else:
        Si[k] = 1
        solve(k + 1)
        Si[k] = 0
        solve(k + 1)

N = int(input())

Ti = [0] * N
Pi = [0] * N
Si = [0] * N

for i in range(N):
    Ti[i], Pi[i] = map(int, input().split())

ans = 0
solve(0)

print(ans)







# def solve(k, s):
#     global ans
#     if k == N:
#         ans = max(ans, s)
#         return
#
#     if(k + Ti[k] <= N):
#         solve(k + Ti[k], s + Pi[k])
#
#     solve(k + 1, s)
#
# N = int(input())
#
# Ti = [0] * N
# Pi = [0] * N
#
# for i in range(N):
#     Ti[i], Pi[i] = map(int, input().split())
#
# ans = 0
# solve(0, 0)
#
# print(ans)
```











# 9월 4일

- sum(sum(a))

  sum의 동작 방식

  sum([1,2,3], default=0)

  => 이차 배열의 합 더하기

  sum(sum(a, [])) => 이차 배열로 된 것을 일차 배열로 만들어서 더할 수 있다.

- max(max(a))

  => max(sum(a, []))

### 연구소

```python
def virus_infact():
    q = []
    for i in range(virus_cnt):
        x, y = virus_pos[i]
        q.append((x,y))

        while q:
            x, y = q.pop(0)
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                xx = x + dx
                yy = y + dy
                if not (0 <= xx < N and 0 <= yy < M):
                    continue
                if mat[xx][yy] == 0:
                    mat[xx][yy] = 2
                    q.append((xx, yy))


def count_safe_area():
    global ans
    tans = sum(mat, []).count(0)
    if ans < tans:
        ans = tans
        
def solve(k):
    arr = []
    for i in range(safe_cnt - 2):
        arr.append(i)
        for j in range(i + 1, safe_cnt - 1):
            arr.append(j)
            for k in range(j + 1, safe_cnt):
                arr.append(k)

                for i in range(3):
                    x, y = safe_pos[arr[i]]
                    mat[x][y] = 1

                virus_infact()
                count_safe_area()

                for ii in range(N):
                    for jj in range(M):
                        mat[ii][jj] = copy_mat[ii][jj]

                arr.pop(-1)
            arr.pop(-1)
        arr.pop(-1)





N, M = map(int, input().split())

mat = [0] * N
for i in range(N):
    mat[i] = list(map(int, input().split()))


copy_mat = [[0] * M for i in range(N)]
virus_cnt = 0
virus_pos = [0] * 10
safe_cnt = 0
safe_pos = [0] * (N * M)
for i in range(N):
    for j in range(M):
        if mat[i][j] == 2:
            virus_pos[virus_cnt] = (i, j)
            virus_cnt += 1
        elif mat[i][j] == 0:
            safe_pos[safe_cnt] = (i, j)
            safe_cnt += 1
        copy_mat[i][j] = mat[i][j]


ans = 0
solve(0)
print(ans)
```



```python
def virus_infact():
    q = []
    for i in range(virus_cnt):
        x, y = virus_pos[i]
        q.append((x,y))

        while q:
            x, y = q.pop(0)
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                xx = x + dx
                yy = y + dy
                if not (0 <= xx < N and 0 <= yy < M):
                    continue
                if mat[xx][yy] == 0:
                    mat[xx][yy] = 2
                    q.append((xx, yy))


def count_safe_area():
    global ans
    tans = sum(mat, []).count(0)
    if ans < tans:
        ans = tans
        

def solve(k, s):

    if k == 3:
        for i in range(3):
            x, y = safe_pos[a[i]]
            mat[x][y] = 1

        virus_infact()
        count_safe_area()

        for i in range(N):
            for j in range(M):
                mat[i][j] = copy_mat[i][j]

    else:
        for i in range(s, safe_cnt + (k - 3) + 1):  #N + (k - R) + 1
            a[k] = i
            solve(k + 1, i + 1)
```





# 9월 5일

## 문제풀이

### 





# 9월 20일

## 문제풀이





## 완전검색

1. 반복과 재귀
   - pre-test / post-test
   - 두 파트 : basis case & inductive case



2. 완전검색 기법





### 순열 생성 코드

```python

def perm_i():
    for i1 in range(1, 4):
        for i2 in range(1, 4):
            if i2 != i1:
                for i3 in range(1, 4):
                    if i3 != i1 and i3 != i2:
                        print(i1, i2, i3)


def perm_r_1(n, r):
    if r == 0:
        print(t[0], t[1], t[2])
    else:
        for i in range(n - 1, -1, -1):
            arr[i], arr[n - 1] = arr[n - 1], arr[i]
            t[r - 1] = arr[n - 1]
            perm_r_1(n - 1, r - 1)
            arr[i], arr[n - 1] = arr[n - 1], arr[i]


def perm_r_2(k):
    if k == R:
        print(arr[0], arr[1], arr[2])
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm_r_2(k + 1)
            arr[k], arr[i] = arr[i], arr[k]



def perm_r_3(k):
    if k == N:
        print(t[0], t[1], t[2])
    else:
        for i in range(N):
            if visited[i]: continue
            t[k] = arr[i]
            visited[i] = 1
            perm_r_3(k + 1)
            visited[i] = 0



print('순열 반복문')
perm_i()

N = 3
R = 3

a = [0] * N
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


t = [0] * N
print('순열 재귀문1')
perm_r_1(N, R)


print('순열 재귀문2')
perm_r_2(0)


visited = [0] * N
print('순열 재귀문3')
perm_r_3(0)
```





# 9월 26일 목요일

- 병합정렬: 내가 짜본 코드

  - Python
  
    ```python
    import random
    from datetime import datetime
    
    
    def merge(left, right):
        global m_count
        m_count += 1
        result = []
        llen = len(left)
        rlen = len(right)
        lp = rp = 0
        while lp < llen and rp < rlen:
            if left[lp] < right[rp]:
                result += [left[lp]]
                lp += 1
            else:
                result += [right[rp]]
                rp += 1
        if lp == llen:
            result += right[rp:rlen]
        else:
            result += left[lp:llen]
        return result
    
    
    def merge_sort(L, R):
        global d_count
        d_count += 1
        if L == R - 1:
            return arr[L:R]
        else:
            M = (L + R) // 2
            left = merge_sort(L, M)
            right = merge_sort(M, R)
            return merge(left, right)
    
    
    d_count = 0
    m_count = 0
    N = 99999
    arr = [random.randint(1, 1000000) for _ in range(N)]
    # print(arr)
    start = datetime.now()
    arr = merge_sort(0, N)
    print(datetime.now() - start)
    print('count : {}, {}'.format(d_count, m_count))
    # print(arr)
    ```
  
  - CPP
  
    ```cpp
    #include <iostream>
    #include <ctime>
    #define NUM 1000000
    using namespace std;
    
    int* merge(int* arr, int* result, int* Left, int* Right) {
    	int ls, le, rs, re, idx;
    	ls = Left[0];
    	le = Left[1];
    	rs = Right[0];
    	re = Right[1];
    	idx = ls;
    
    	while (ls <= le && rs <= re) {
    		if (arr[ls] <= arr[rs]) {
    			result[idx++] = arr[ls++];
    		}
    		else {
    			result[idx++] = arr[rs++];
    		}
    	}
    	if (ls > le) {
    		for (int i = rs; i <= re; i++) {
    			result[idx++] = arr[i];
    		}
    	}
    	else {
    		for (int i = ls; i <= le; i++) {
    			result[idx++] = arr[i];
    		}
    	}
    	
    	for (int i = Left[0]; i <= Right[1]; i++) {
    		arr[i] = result[i];
    	}
    
    	int *value = new int[2];
    	value[0] = Left[0];
    	value[1] = Right[1];
    
    	delete Left;
    	delete Right;
    
    	return value;
    }
    
    
    int* merge_sort(int* arr, int* result, int left, int right) {
    	if (left == right) {
    		int *a = new int[2];
    		a[0] = left;
    		a[1] = right;
    		return a;
    	}
    	else {
    		int mid = (left + right) / 2;
    		int* Left = merge_sort(arr, result, left, mid);
    		int* Right = merge_sort(arr, result, mid + 1, right);
    		return merge(arr, result, Left, Right);
    	}
    }
    
    
    void sorted(int *arr, int size) {
    	int *result = new int[size];
    
    	merge_sort(arr, result, 0, size - 1);
    
    	for (int i = 0; i < size; i++) {
    		arr[i] = result[i];
    	}
    
    	delete result;
    }
    
    
    int main() {
    	ios::sync_with_stdio(false);
    	cin.tie(0);
    	srand(unsigned long(time(0)));
    
    	
    	int *arr = new int[NUM];
    	for (int i = 0; i < NUM; i++) {
    		arr[i] = rand();
    	}
    
    	clock_t st = clock();
    	sorted(arr, NUM); // mergesort 호출
    	cout << clock() - st << " ms\n";
    }
    ```
  
    
  
  




- 퀵정렬: 내가 짜본 코드. quick sort, quicksort, 퀵소트

  - 내장함수보다 월등하게 느리다

  - Python

    ```python
    def quick_sort(arr, left, right):
        if left < right:
            pivot = left
            lp = left
            rp = right
            while lp < rp:
                while lp < right and arr[lp] <= arr[pivot]:
                    lp += 1
                while rp > 0 and arr[rp] > arr[pivot]:
                    rp -= 1
                if lp < rp:
                    arr[lp], arr[rp] = arr[rp], arr[lp]
            if arr[pivot] >= arr[rp]:
                arr[rp], arr[pivot] = arr[pivot], arr[rp]
            p = rp
            quick_sort(arr, left, p - 1)
            quick_sort(arr, p + 1, right)
    
    
    def q_sort(arr):
        quick_sort(arr, 0, len(arr) - 1)
    
    
    for T in range(1, int(input()) + 1):
        N = int(input())
        arr = list(map(int, input().split()))
        q_sort(arr)
        print('#{} {}'.format(T, arr[N // 2]))
    ```

  - CPP

    ```cpp
    #include <iostream>
    #include <ctime>
    using namespace std;
    
    void q_sort(int * arr, int left, int right, bool reverse = false) {
    	if (left < right) {
    		int pivot, left_p, right_p, partition, temp;
    		pivot = left;
    		left_p = left;
    		right_p = right;
    		if (reverse == false) {
    			while (left_p < right_p) {
    				while (left_p <= right && arr[pivot] >= arr[left_p]) {
    					left_p++;
    				}
    				while (right_p >= 0 && arr[pivot] < arr[right_p]) {
    					right_p--;
    				}
    				if (left_p < right_p) {
    					temp = arr[left_p];
    					arr[left_p] = arr[right_p];
    					arr[right_p] = temp;
    				}
    			}
    		}
    		else {
    			while (left_p < right_p) {
    				while (left_p <= right && arr[pivot] <= arr[left_p]) {
    					left_p++;
    				}
    				while (right_p >= 0 && arr[pivot] > arr[right_p]) {
    					right_p--;
    				}
    				if (left_p < right_p) {
    					temp = arr[left_p];
    					arr[left_p] = arr[right_p];
    					arr[right_p] = temp;
    				}
    			}
    		}
    		temp = arr[right_p];
    		arr[right_p] = arr[pivot];
    		arr[pivot] = temp;
    		partition = right_p;
    		q_sort(arr, left, partition - 1, reverse);
    		q_sort(arr, partition + 1, right, reverse);
    	}
    }
    
    void quick_sort(int *arr, const int size, bool reverse = false) {
    	q_sort(arr, 0, size - 1, reverse);
    }
    
    int main() {
    	srand(unsigned long(time(NULL)));
    	ios::sync_with_stdio(false);
    	cin.tie(NULL);
    	
    	clock_t start = clock();
    	int num = 1000000;
    
    	int *arr = new int[num];
    	for (int i = 0; i < num; i++) {
    		arr[i] = rand() % 10000;
    	}
    
    	quick_sort(arr, num, true);
    
    	cout << clock() - start << " ms\n";
    }
    ```

    

  

- 이진탐색

  ```python
  def search(b):
      L = 0
      R = N - 1
      d = -1
      while True:
          M = (L + R) // 2
          if A[M] == b:
              return 1
          if L == R:
              return 0
          if b < A[M]:
              if d == 0:
                  return 0
              d = 0
              R = M - 1
          else:
              if d == 1:
                  return 0
              d = 1
              L = M + 1
  
  
  for T in range(1, int(input()) + 1):
      N, M = map(int, input().split())
      A = list(map(int, input().split()))
      B = list(map(int, input().split()))
      A.sort()
      ans = 0
      for b in B:
          ans += search(b)
      print('#{} {}'.format(T, ans))
  ```

  



# 9월 30일

### 3752 가능한 시험점수

- 부분집합 문제이지만 부분집합으로는 시간 초과가 발생
- 그러므로 DP를 활용하여 문제를 해결

```python
import sys
from datetime import datetime

sys.stdin = open('input.txt', 'r')

start = datetime.now()
for T in range(1, int(input()) + 1):
    N = int(input())
    num = list(map(int, input().split()))
    save = [1] + ([0] * sum(num))
    ans = 1
    temp = [0]
    for n in num:
        for i in range(ans):
            if save[n + temp[i]] == 0:
                save[n + temp[i]] = 1
                ans += 1
                temp += [n + temp[i]]
    print('#{} {}'.format(T, ans))
print(datetime.now() - start)
```





# 10월 1일

TSP의 DP 해결



# 10월 4일

disjoint-set -> 크루스칼 알고리즘 할 때 사용(최종 부모를 설정)



# 10월 10일 

## 트리

1) 트리의 표현 방식 : 이진탐색 트리, 힙트리, 허프만 트리, 트라이, 서픽스트리(서픽스 어레이),  AVL(B-tree, 다진트리, 2-3-4 트리), 세그먼트 트리, 인덱스트리, 아호코라식 트리,  + 완전 트리

- 필요에 의해 트리가 계속 만들어짐
- 각각의 트리를 어떨 때 쓰는 지 알고 있어야 됨

2) 순회방식 : preorder, inorder, postorder

	- DFS, BFS 도 가능하지만 트리에 비해 너무 무겁다.



### 트리의 개념

- 비선형 구조

- 형제끼리는 간신을 갖지 않음(recursive 하지 않다.)

- 트리는 root를 가짐

- 서브트리를 가짐(트리의 가장 작은 단위는 노드 하나다.)
- 단말노드(leaf 노드, terminal)
- 간선, 부모노드, 형제노드, 조상노드
- 서브트리를 잘라서 관리하는 것을 forest라고 함



- ***차수
  - 그래프 입장에서, 자식으로가는 간선의 개수만 차수로 따진다. (그래프와 차수를 따지는 것이 다르다. 그래프는 연결된 노드의 개수)
- 높이
  - 루트로부터 해당 정점으로 가는 길이
  - 높이가 같은 노드들을 레벨이 같다고 표현 



#### 이진트리

- 2개의 서브트리를 가지는 트리
  - 왼쪽 자식노드
  - 오른쪽 자식노드
- 레벨 i 에



##### 이진트리 종류

- 포화 이진 트리(full binary tree)

  - 완전 이진 트리와 혼용으로 쓰임
  - 모든 노드가 꽉참

- 완전 이진 트리(complete binary tree)

  	- 빈 자리가 없는 이진 트리

  - 힙 트리는 완전 이진 트리

- 편향 이진 트리(skewed binary tree)

  - 한쪽 방향의 자식 노드만을 가진 이진 트리
    - 왼쪽 편향 이진 트리
    - 오른쪽 편향 이진 트리
  - 최소 개의 노드 개수로 최대 높이를 만들 때



#### 표현

간선의 배열로 받을 때...

##### 1) 1차 배열

- 배열에 그 인덱스를 저장하는 것
  - 자기 인덱스의 X 2는 왼쪽 자식, X 2 + 1이 오른쪽 자식
  - 자기 인덱스를 2로 나누면 부모를 찾아갈 수 있다.
- 문제는....
  - 언제 어떤 값이 들어올 지 모르기 때문에 메모리 효율이 떨어진다.
  - 그러므로 필요한 메모리를 필요할 때마다 할당하는 것
  - 그래서 연결리스트를 활용

##### 2) 연결 리스트

- 필요한 개수만큼 노드를 만들어서 활용

##### 3) 2차 배열을 사용할 수도 있음

- 검정에서 활용

- 노드의 개수만큼 row를 만들고 col을 세 개 둔다
  - 왼쪽 자식노드, 오른쪽 자식노드, 부모



####  순회

- 전위순회(preorder traversal) : VLR
- 중위순회(inorder traversal) : LVR
- 후위순회(postorder traversal) : LRV



- 이진 트리의 배열 구현

  ```python
  def preorder(node):
      print(node, end=' ')
      if graph[node][0]:
          preorder(graph[node][0])
      if graph[node][1]:
          preorder(graph[node][1])
  
  
  def inorder(node):
      if graph[node][0]:
          inorder(graph[node][0])
      print(node, end=' ')
      if graph[node][1]:
          inorder(graph[node][1])
  
  
  def postorder(node):
      if graph[node][0]:
          postorder(graph[node][0])
      if graph[node][1]:
          postorder(graph[node][1])
      print(node, end=' ')
  
  
  data = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
  graph = [[0] * 3 for _ in range(max(data) + 1)]
  for d in range(0, len(data), 2):
      a = data[d]
      b = data[d + 1]
      if graph[a][0] == 0:
          graph[a][0] = b
      else:
          graph[a][1] = b
      graph[b][2] = a
  
  print('pre  : ', end=' ')
  preorder(1)
  print()
  print('in   : ', end=' ')
  inorder(1)
  print()
  print('post : ', end=' ')
  postorder(1)`
  ```

  



#### 수식 트리

- 수식을 표현하는 이진 트리
- 수식 이진트리(Expression Binary Tree)



#### 이진 탐색 트리

- 이진 탐색을 자료구조화한 것
- 루트를 기준으로 작은 것이 왼쪽 서브트리에 배정, 큰 것이 오른쪽 서브트리



자료구조는 왜 쓰지?

자료를 논리적 구조로 저장했다가 필요에 따라 쓰기 위해

삽입 삭제가 기본. 필요할 때 쓰고 빼고. 이 연산 이후에도 이 논리적 구조는 깨지면 안 된다.



- 이진 탐색트리는 추가적으로 탐색이 들어감



##### 삽입과 삭제

- 삽입은 있을 위치에 그냥 넣으면 됨

  - 

- 삭제. 자식을 입양시켜야 함

  - 자식이 없는 경우
- 노드 하나만 날리면 됨
  - 자식이 하나인 경우
- 부모와 자식을 이으면 됨
  - 자식이 둘인 경우
    - 루트는 중앙값의 의미를 가짐
      - 왼쪽 서브트리에서 가장 큰 놈 혹은 오른쪽 서브트리에서 가장 작은 놈
        - 가장 큰 놈? 오른쪽 자식이 없는 놈
        - 가장 작은 놈? 왼쪽 자식이 없는 놈
      - 혹은 inorder를 하게 되면 순서대로 되는 것을 알 수 있음. root 값에 바로 옆에 있는 값들을 선택하면 됨



- 그런데 이진 트리가 선형적으로 구성된다면?
  - 크게 2가지 접근 방식
    - `다진 트리`로 가든지 : ex) 레드 블럭 트리, 2-3-4 트리, B 트리
    - `자가 균형 트리`를 만들든지 ex) AVL



##### 2-3-4 트리

- 하나의 노드가 자식을 2~4개까지 가질 수 있다.

  ex) 1 0 6 9 5 8 1 6 7 2 4 3



##### AVL 트리

- 세 명이서 만듦
- balance factor를 관리: 왼쪽 서브트리 높이 - 오른쪽 서브트리 높이 -1 ~ 1 사이를 유지하도록 만든다.
  - 모든 노드가 -1부터 1까지의 balance facotr를 가진다.
  - LL, LR, RR, RL 패턴 등으로 나뉨
    - 균형이 깨진 걸 재조정



##### heap 트리

- 완전 이진 트리여야 함

- 부모가 자식들보다 크면 max heap

- 부모가 자식들보다 작으면 mini heap



- 힙에서의 삽입은? 
  - 자기보다 큰 놈 만날 때까지 교환교환... -> 최종적으로 가장 큰 놈 혹은 가장 작은 놈이 루트에 있는 것
- 삭제는?
  - 지울 놈을 임시로 루트로 옮김. 그러면서 자기 자리를 찾아간다.



##### heap sort 연습

- data : 6 5 3 2 8 7 1 4

  => 배열로 많이 씀

  priority que의 자료구조로 씀



##### 허프만 트리

- 압축 인코딩과 디코딩
- 빈도수 많은 것



##### Trie 트라이

- 문자열의 집합을 표현하는 트리
- 구글 검색에서 연관 검색을 관리하는 자료구조
- re`trie`val => 트라이 
- 노드 하나당 문자 하나로 대체
  - 노드 하나당 알파벳 수만큼 노드를 가지고 있어야 한다.



##### Compressed Trie

- 



##### Suffix Trie

- 접미어 트라이

  ex) abc의 접미어는 c, bc, abc 3 종류가 됨

- 전처리를 좀 해놓겠다는 것. (문서들을)

  ex) minimize



##### Suffix Array

- sorting 된 순서로 숫자만 가지고 있겠다는 것.
- 이미 고정된 문서들에 대해 단어들을 전처리할 수 있는 자료구조
- LCP : 두 접미사의 최대 공통 접두사의 길이(Longest common prefix))

- 이걸로 회문 검사도 할 수 있다.



##### 아호-코라식

- failure link를 따라간다...?
- KMP를 트리로 만들어 놓은 것
- SDS 프로 문제에서 나온 적 있음...



##### ***인덱스 트리

- 이게 가장 중요
- 상급편 제일 뒷부분에 있음
- 누적합을 구한 뒤, 인덱스로 차이를 구함



임의의 정수 n을 입력받은 후, q 개의 2가지 쿼리에 대해서 답을 출력하는 프로그램을 작성하시오.

1) 구간합 쿼리, 갱신쿼리 2가지가 있을 때

+++ 세그먼트 트리. segment tree, interval tree(구간 트리)

- 노드 안에 있는 값들이 value, 즉 데이터를 의미.
- 그런데 세그먼트 트리는 데이터가 단말에만 있음. 중간에 있는 노드들은 메타 정보만 담고 있음
  - 중간에는 자기 구간 하에서 정의된 정보만들 담고 있음.
  - 이것이 다진으로 가거나 이진으로 갈 수 있다. 
  - 유연성이 높은 트리 -> `인덱스 트리`, `full binary tree`, 펜익 트리(비트 처리를 함)



##### 인덱스 트리 index tree

- complete binary tree로 구성된 segment  tree

  ex) 5개의 데이터로 IDT를 구성해보려면?

  - 5
  - 9, 8, 1, 7, 2

- 일반적으로 IDT는 complete binary tree를 가장 효율적으로 표현할 수 있는 일차원 배열을 이용하고, 그 배열의 크기는 원본 data가 5개 이므로 5 이상인 가장 작은 2^k값을 기준으로 설정한다.

- 여기서는 8이 되므로 이 값의 2배에서 1을 뺀 15개의 원소를 가지는 배열로 구성할 수 있다.



- 데이터들은 맨 마지막에 집어 놓고...

- 나머지 노드들이 요약 정보를 가지고 있는다(구간들의 합)

- 변경 연산이 어떻게 이루어지는가?

  - 자식 노드가 변경이 되면 부모만을 따라가서 수정하면 된다.

- 구간합은 어떻게 구하는가?

  - 구간의 시작 포인터 a, 끝 포인터 b를 쥐고 있는다.
  - 두 포인터를 2로 나누면서 부모를 찾다가 a와 b가 같은 부모를 가리킬 때 구간합이 된다.

  - 시작 포인터는 무조건 a짝수에서 시작, 끝 포인터는 홀수에서 시작해야 한다.



=> RMG(Range Minimum Query) -> DP의 이진트리화와 같다. 굉장히 파워가 강함

(문제해결을 위한 창의적 알고리즘 - 고급편)









클래스로 트리를 구현해보자

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def search(self, node, parent):
        if node.data == parent:
            return node
        if not node.left and not node.right:
            return
        else:
            if node.left:
                result = self.search(node.left, parent)
                if result:
                    return result
            if node.right:
                result = self.search(node.right, parent)
                if result:
                    return result

    def append(self, parent, data):
        if not self.root:
            node = Node(parent)
            self.root = node
        par = self.search(self.root, parent)
        if par:
            node = Node(data)
            if not par.left:
                par.left = node
            else:
                par.right = node

    def pre_order(self, node):
        if node:
            print(node.data, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.data, end=' ')
            self.in_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end=' ')

    def preorder(self):
        self.pre_order(self.root)

    def inorder(self):
        self.in_order(self.root)

    def postorder(self):
        self.post_order(self.root)


data = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
tree = Tree()
for d in range(0, len(data), 2):
    tree.append(data[d], data[d + 1])

print('preorder  : ', end='')
tree.preorder()
print()
print('inorder   : ', end='')
tree.inorder()
print()
print('postorder : ', end='')
tree.postorder()
print()
```





BST(Binary Search Tree): 이진 탐색 트리 구현 / 삽입 / 삭제

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BST:
    def __init__(self):
        self.root = None

    def append(self, data):
        self._append(self.root, data)

    def _append(self, node, data):
        if self.root is None:
            self.root = Node(data)
        else:
            if data <= node.data:
                if node.left is None:
                    node.left = Node(data)
                else:
                    self._append(node.left, data)
            else:
                if node.right is None:
                    node.right = Node(data)
                else:
                    self._append(node.right, data)

    def delete(self, data):
        self._delete(self.root, self.root, data)

    def _delete(self, parent, sibling, data):
        # 부모노드를 반드시 알아야 한다
        # 지우려는 값이 노드와 동일할 경우
        if data == sibling.data:
            # 자식 노드가 몇개인지 봐야한다.
            # 자식이 둘 인 경우
            # 자식 노드가 없는 경우
            # 자식 노드가 하나인 경우
            pass
        # 지우려는 값이 노드와 다를 경우
        else:
            if data < parent.data:
                if parent.left.data == data:
                    return parent, parent.left
                else:
                    pass
            else:
                if parent.right.data == data:
                    return parent, parent.right
                else:
                    pass

import random

lst = [random.randint(1, 100) for _ in range(20)]
tree = BST()
for item in lst:
    tree.append(item)
```



# 10월 16일

## 그래프

MST, 다익스트라(최단경로), AOE, AOV, SCC, 플로이드, 크루스칼

상호배타 집합

disjoint-set



### 서로소 집합 disjoint-set

- MST 구할 때 사용

- 주요 로직

  - make_set()
  - find_set()
  - union()

- make_set()

  ```python
  def make_set(node):
      node.parent = node
  ```

- find_set(node) : 시간 효율을 높이기 위해 노드들을 돌며 대표 노드로 부모노드를 바꾼다.

  ```python
  def find_set(node):
      if G[node][0] != node:
          G[node][0] = find_set(G[node][0])
          return G[node][0]
     	else:
          return node
  ```

- union(x, y)

  ```python
  def union(x, y):
      v1 = find_set(x)
      v2 = find_set(y)
      if v1 < v2:
          G[v2][0] = v1
      else:
          G[v1][0] = v2
  ```

  



### MST 최소 신장 트리

- 크루스칼 : 간선 중심
- 프림 : 정점 중심



### 최단거리

- 다익스트라
- 플로이드-워셜
- 순열(TSP, 가지치기, DP, BFS .... 인공지능)





