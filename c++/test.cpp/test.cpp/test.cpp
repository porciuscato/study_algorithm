#pragma once
#include <iostream>
#include <vector>
#include <malloc.h>
using namespace std;

[[noreturn]] static void move(int a) {

}


class node {
public:
	node * left;
	node * right;
	int data;
};

class binaryTree {
private:
	node * head;
	int data;
public:
	binaryTree() {
		head = NULL;
	}
	void move(int a) {
		node *HEAD = new node;
		head = HEAD;
	}
};


int main() {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		char * words = new char[N];
		cin >> words;
		auto temp = strtol(words, NULL, 16);
		cout << hex << uppercase << temp << endl;
	}
}
