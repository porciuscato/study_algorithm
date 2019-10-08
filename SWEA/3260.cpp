#include <iostream>
#include <string>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie();
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
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
				a_start = i;
				break;
			}
		}

		int b_start = 0;
		for (int i = 0; i < 101; i++) {
			if (b_arr[i] != 0) {
				b_start = i;
				break;
			}
		}

		int range = 0;
		if (a_start <= b_start) {
			range = a_start;
		}
		else {
			range = b_start;
		}


		int *result = new int[101];
		for (int i = 0; i < 101; i++) {
			result[i] = 0;
		}

		int upper = 0;
		for (int i = 100; i >= range - 1; i--) {
			int temp = a_arr[i] + b_arr[i] + upper;
			if (temp >= 10) {
				result[i] = temp - 10;
				upper = 1;
			}
			else {
				result[i] = temp;
				upper = 0;
			}
		}
		int r_start = 0;
		for (int i = 0; i < 101; i++) {
			if (result[i] != 0) {
				r_start = i;
				break;
			}
		}

		cout << "#" << t << " ";
		for (int i = r_start; i < 101; i++) {
			cout << result[i];
		}
		cout << endl;
		delete[] a_arr;
		delete[] b_arr;
		delete[] result;
	}
}