#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

void qsort(int *arr, int size);
void quick_sort(int *arr, int left, int right);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		int * arr = new int[N];
		for (int i = 0; i < N; i++) {
			cin >> arr[i];
		}
		qsort(arr, N);
		cout << "#" << t << " " << arr[N / 2] << "\n";
	}
}

void qsort(int *arr, int size) {
	quick_sort(arr, 0, size - 1);
}

void quick_sort(int *arr, int left, int right) {
	if (left < right) {
		int pivot, lp, rp, temp;
		pivot = left;
		lp = left;
		rp = right;
		while (lp < rp) {
			while (lp < right && arr[pivot] >= arr[lp]) {
				lp++;
			}
			while (rp > 0 && arr[pivot] < arr[rp]) {
				rp--;
			}
			if (lp < rp) {
				temp = arr[lp];
				arr[lp] = arr[rp];
				arr[rp] = temp;
			}
		}
		temp = arr[pivot];
		arr[pivot] = arr[rp];
		arr[rp] = temp;

		quick_sort(arr, left, rp - 1);
		quick_sort(arr, rp + 1, right);
	}
}