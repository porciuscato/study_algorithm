#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie();
	freopen("input.txt", "r", stdin);
	int T, ans;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		ans = 0;
		string a, b;
		cin >> a;
		cin >> b;
		int *a_arr = new int[101];
		int *b_arr = new int[101];
		for (int i = 0; i < 101; i++) {
			a_arr[i] = 0;
			b_arr[i] = 0;
		}
		int idx = 100;
		int a_size = a.size();
		for (int i = 0; i < unsigned(a.size()); i++) {
			a_arr[idx--] = int(a[--a_size]) - 48;
		}
		idx = 100;
		int b_size = b.size();
		for (int i = 0; i < unsigned(b.size()); i++) {
			b_arr[idx--] = int(b[--b_size]) - 48;
		}

		int a_start = 0;
		for (int i = 0; i < 101; i++) {
			if (a_arr[i] != 0) {

			}
		}
		cout << "\n";
		for (int i = 0; i < 101; i++) {
			cout << b_arr[i];
		}
		cout << "\n";




		//cout << "#" << t << " " << ans << "\n";
	}
}