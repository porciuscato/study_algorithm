#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

void testcase() {
	freopen("input.txt", "w", stdout);
	srand(unsigned int(time(NULL)));
	int T = 10;
	cout << T << "\n";
	for (int t = 0; t < T; t++) {
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cout << rand() % 10 << " ";
			}
			cout << "\n";
		}
	}
}

void dfs(int& visited, int ** board, int *ans, int r, int c);

int dx[4] = { -1,0,1,0 };
int dy[4] = { 0,1,0,-1 };

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	//testcase();
	freopen("input.txt", "r", stdin);

	int T;
	int *ans = new int;
	*ans = 0;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int **board = new int*[4];
		for (int i = 0; i < 4; i++) {
			board[i] = new int[4];
			for (int j = 0; j < 4; j++) {
				cin >> board[i][j];
			}
		}

		int *visited = new int[10000000];

		for (int r = 0; r < 4; r++) {
			for (int c = 0; c < 4; c++) {
				dfs(visited, board, ans, r, c);
			}
		}

		for (int i = 0; i < 4; i++) {
			delete board[i];
		}
		delete board;
		delete visited;
		cout << "#" << t << " " << ans << "\n";
	}
}

class node {
public:
	int row, col, depth, value;
	node() {
		row = 0;
		col = 0;
		depth = 0;
		value = 0;
	}

	node(int row, int col, int depth, int value) {
		this->row = row;
		this->col = col;
		this->depth = depth;
		this->value = value;
	}
};


void dfs(int* visited, int** board, int* ans, int r, int c) {
	node stack[30];
	int sp = 0;
	stack[sp] = node(r, c, 1, board[r][c]);
	while (sp >= 0) {
		int tr, tc, td, tvalue;
		tr = stack[sp].row;
		tc = stack[sp].col;
		td = stack[sp].depth;
		tvalue = stack[sp].value;
		sp--;
		for (int i = 0; i < 4; i++) {
			int dr, dc, dd, dvalue;
			dr = tr + dx[i];
			dc = tc + dy[i];
			if (dr >= 0 && dr < 4 && dc >= 0 && dc < 4) {
				dd = td + 1;
				dvalue = tvalue * 10 + board[dr][dc];
				if (dd == 7) {
					if (visited[dvalue] = 1) {
						continue;
					}
					else {
						visited[dvalue] = 1;
						*ans++;
						stack[++sp] = node(dr, dc, dd, dvalue);
					}
				}
			}
		}
	}
}