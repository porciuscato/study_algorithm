#include <iostream>
#include <cstdlib>
using namespace std;

class node {
public:
	int r;
	int c;
	int dis;
	node(int r, int c, int dis) {
		this->r = r;
		this->c = c;
		this->dis = dis;
	}
	node() {
		this->r = 0;
		this->c = 0;
		this->dis = 0;
	}
};

int main() {
	//*
	ios::sync_with_stdio(false);
	cin.tie();
	FILE *stream;
	freopen_s(&stream, "input.txt", "r", stdin);

	int N, M, ans;
	ans = 0;
	cin >> N;
	cin >> M;
	// 데이터 초기화
	int **data = new int*[N];
	for (int i = 0; i < N; i++) {
		data[i] = new int[M];
		char arr[101];
		cin >> arr;
		for (int j = 0; j < M; j++) {
			data[i][j] = int(arr[j]) - 48;
		}
	}
	// vis 초기화
	bool **visited = new bool*[N];
	for (int i = 0; i < N; i++) {
		visited[i] = new bool[M];
		for (int j = 0; j < M; j++) {
			visited[i][j] = 0;
		}
	}

	// delta 선언
	int dx[4] = { -1, 0, 1, 0 };
	int dy[4] = { 0, 1, 0, -1 };

	node *q = new node[N * M];
	int front = -1, rear = -1;
	visited[0][0] = 1;
	rear++;
	q[rear] = node(0, 0, 1);
	bool end = true;
	while (front != rear && end) {
		front++;
		int tr, tc, dis;
		tr = q[front].r;
		tc = q[front].c;
		dis = q[front].dis;
		for (int d = 0; d < 4; d++) {
			int dr, dc;
			dr = tr + dx[d];
			dc = tc + dy[d];
			if (dr >= 0 && dr < N && dc >= 0 && dc < M && visited[dr][dc] == 0 && data[dr][dc] == 1) {
				if (dr == N - 1 && dc == M - 1) {
					ans = dis + 1;
					end = false;
					break;
				}
				rear++;
				q[rear] = node(dr, dc, dis + 1);
				visited[dr][dc] = true;
			}
		}
	}



	for (int i = 0; i < N; i++) {
		delete[] data[i];
	}
	delete[] data;
	cout << ans;
	//*/
}