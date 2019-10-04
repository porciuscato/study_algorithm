#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
using namespace std;


int T, max_val, chance;
int **visited;

string info;


void backtrack(int k) {
	if (visited[k][stoi(info)] == 1) {
		return;
	}
	visited[k][stoi(info)] = 1;
	if (k == chance) {
		int val = stoi(info);
		if (max_val < val) {
			max_val = val;
		}
	}
	else {
		for (int i = 0; i < int(info.length() - 1); i++) {
			for (int j = i + 1; j < int(info.length()); j++) {
				char temp = info[i];
				info[i] = info[j];
				info[j] = temp;
				backtrack(k + 1);
				temp = info[i];
				info[i] = info[j];
				info[j] = temp;
			}
		}
	}
}



int main() {
	ios::sync_with_stdio(false);
	cin.tie();
	freopen("input.txt", "r", stdin);
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> info;
		cin >> chance;
		max_val = 0;
		visited = new int*[chance + 1];
		for (int i = 0; i < chance + 1; i++) {
			visited[i] = new int[1000000];
			for (int j = 0; j < 1000000; j++) {
				visited[i][j] = 0;
			}
		}
		backtrack(0);
		for (int i = 0; i < chance + 1; i++) {
			delete visited[i];
		}
		delete visited;
		cout << "#" << t << " " << max_val << "\n";
	}
}