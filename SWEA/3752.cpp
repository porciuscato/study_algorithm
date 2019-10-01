#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

void testcase() {
	srand(unsigned int(time(NULL)));
	freopen("input.txt", "w", stdout);
	int scope = 100;
	int T = 10;
	cout << T << "\n";
	for (int i = 0; i < T; i++) {
		cout << scope << "\n";
		for (int s = 0; s < scope; s++) {
			cout << rand() % 100 + 1 << " ";
		}
		cout << "\n";
	}
}

int main() {
	// testcase()

	ios::sync_with_stdio(false);
	cin.tie(0);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, ans, sum;
		cin >> N;
		int *data = new int[N];
		sum = 0;
		for (int i = 0; i < N; i++) {
			cin >> data[i];
			sum += data[i];
		}
		int *save = new int[sum + 1];
		save[0] = 1;
		for (int i = 1; i < sum + 1; i++) {
			save[i] = 0;
		}

		ans = 1;
		int ans_temp = 1;
		int idx = 0;
		int *temp = new int[sum + 1];
		for (int i = 0; i < sum + 1; i++) {
			temp[i] = 0;
		}
		for (int n = 0; n < N; n++) {
			for (int j = 0; j < ans; j++) {
				int val = data[n] + temp[j];
				if (save[val] == 0) {
					save[val] = 1;
					ans_temp++;
					temp[++idx] = val;
				}
			}
			ans = ans_temp;
		}
		cout << "#" << t << " " << ans << "\n";
	}
}