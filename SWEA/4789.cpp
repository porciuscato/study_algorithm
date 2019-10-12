#include <iostream>
#include <string>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie();
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int hire = 0, go = 0;
		string data;
		cin >> data;
		int size = int(data.length());
		int *change = new int[size];
		for (int i = 0; data[i] != '\0'; i++) {
			change[i] = int(data[i]) - 48;
		}
		for (int i = 0; i < size; i++) {
			go += change[i];
			if (go == 0) {
				++hire;
				++go;
			}
			--go;
		}
		delete[] change;
		cout << "#" << t << " " << hire << "\n";
	}
}