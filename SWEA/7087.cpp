#include <iostream>
#include <string>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie();
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, ans;
		cin >> N;
		bool *alpha = new bool[26];
		for (int n = 0; n < N; n++) {
			string word;
			cin >> word;
			alpha[int(word[0]) - 65] = true;
		}
		ans = 0;
		for (int n = 0; n < 26; n++) {
			if (alpha[n] == false) {
				break;
			}
			ans++;
		}
		cout << "#" << t << " " << ans << "\n";
	}
}