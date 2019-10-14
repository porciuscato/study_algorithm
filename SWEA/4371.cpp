#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie();
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, ans;
		ans = 1;
		cin >> N;
		// 데이터 입력 받기
		int *days = new int[N];
		for (int i = 0; i < N; i++) {
			cin >> days[i];
		}
		// ships 초기화
		int *ships = new int[N];
		for (int i = 0; i < N; i++) {
			ships[i] = 0;
		}
		// ships가 0이 될 때 까지 계속 도는 것
		int idx = 1;
		ships[0] = days[1] - 1;
		for (int i = 2; i < N; i++) {
			bool check = 1;
			for (int j = 0; ships[j] != 0; j++) {
				if ((days[i] - 1) % ships[j] == 0) {
					check = 0;
					break;
				}
			}
			if (check) {
				ships[idx++] = days[i] - 1;
				ans++;
			}
		}
		delete[] ships;
		delete[] days;
		cout << "#" << t << " " << ans << "\n";
	}
}