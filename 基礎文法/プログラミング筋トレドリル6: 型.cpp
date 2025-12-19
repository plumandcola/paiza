#include <iostream>
#include <string>
using namespace std;

int main(void) {
	// 型 - 型変換 1
	string s = "813";
	int a = atoi(s.c_str()); // atoiを使用する
	int a = stoi(s);
	
	cout << a << endl;


	// 型 - 型変換 2
	int a = (int)66.6666;
	
	cout << a << endl;


	// 型 - 型変換 3
	string a = to_string(11813); // to_stringを使用する
	
	cout << a << endl;


	// 型 - 型変換 4
	string a = to_string(118.13);
	
	cout << a << endl;


	// 型 - 型変換 5
	string s = "1.11111";
	double a = atof(s.c_str()); // atofを使用する
	
	cout << a << endl;


	// 型 - 型変換 6
	double a = (double)7; // 値の前に(double)と書く
	
	cout << fixed << setprecision(1) << a << endl;


	// 型 - 少数点以下の切り捨て 1
	int a = (int)3.14;
	
	cout << a << endl;


	// 型 - 少数点以下の切り捨て 2
	int a = (int)8.94;
	
	cout << a << endl;
}
