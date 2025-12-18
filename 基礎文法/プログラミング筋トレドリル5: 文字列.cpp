#include <iostream>
#include <string>
using namespace std;

int main(void) {
	// 文字列 - 長さ
	string s = "Hello paiza";
	
	cout << s.length() << endl;
	cout << s.size() << endl;
	

	// 文字列 - 大文字に変換
	char c = 'p';
	
	cout << (char)toupper(c) << endl;


	// 文字列 - 部分文字の取得
	string s = "paiza";

	cout << s[2] << endl; // n個目の文字は、s[n-1]で取得できます


	// 文字列 - 部分文字列の取得
	string s = "abcdefghijklmnopqrstuvwxyz";
	
	// n個目の文字からm文字分の部分文字列はs.substr(n-1, m)で取得できます
	cout << s.substr(9, 3) << endl;


	// 文字列 - 部分文字列の検索
	string s = "aaapaizabbb";
	int index = s.find("paiza"); // findを利用する
	
	cout << index << endl;
}
