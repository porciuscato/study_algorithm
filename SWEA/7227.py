#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
typedef long long llong;
using namespace std;

int N;
int ans;
class Warm {
public:
	llong x;
	llong y;
	int num;
	Warm() :x(0), y(0), num(0) {

	}
	Warm(llong in_x, llong in_y, int in_num) {
		this->x = in_x;
		this->y = in_y;
		this->num = in_num;
	}
};

Warm Warms[20];

class node {
public:
	int num1;
	int num2;
	llong vector;
	node() {
		this->num1 = 0;
		this->num2 = 0;
		this->vector = 0;
	}
	node(int in1, int in2) {
		llong xcha = Warms[in1].x - Warms[in2].x;
		llong ycha = Warms[in1].y - Warms[in2].y;
		this->num1 = in1;
		this->num2 = in2;
		this->vector = xcha * xcha + ycha * ycha;
	}
};

node nodes[190];
int idx = 0;

void combi(int ssang[2], int depth, int last) {
	if (depth == 2) {
		nodes[::idx++] = node(ssang[0], ssang[1]);
	}
	else {
		for (int i = last; i < N; i++) {
			int arr[2];
			arr[0] = ssang[0];
			arr[1] = ssang[1];
			arr[depth] = i;
			combi(arr, depth + 1, last + 1);
		}
	}
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie();
	///*
	freopen("input.txt", "r", stdin);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		::ans = 0;
		cin >> ::N;
		Warm Warms[20];
		for (int i = 0; i < ::N; i++) {
			llong x, y;
			cin >> x;
			cin >> y;
			Warms[i] = Warm(x, y, i);
		}
		int ssang[2] = { 0, 0 };
		combi(ssang, 0, 0);


		// Warm 인풋 확인
		///*
		for (int i = 0; i < N; i++) {
			cout << nodes[i].num1 << " " << nodes[i].num2 << " " << nodes[i].vector << endl;
		}
		//*/
		//cout << "#" << t << " " << ::ans << "\n";
	}
	//*/
}