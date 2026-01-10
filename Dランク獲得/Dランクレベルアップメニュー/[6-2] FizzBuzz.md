# FizzBuzz

https://paiza.jp/works/mondai/d_rank_level_up_problems/d_rank_level_up_problems__loop_boss

<details><summary>ヒント: "割り切れる"かどうかを判定する方法</summary><br>

"$`n`$ で割り切れる" = "$`n`$ で割った時の余りが0"

<br></details>

<details><summary>Python3 解答</summary><br>

`i % 3 == 0 and i % 5 == 0` の部分は、`i % 15 == 0` でも正解です。

```python
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

```python
for i in range(1, 101):
    if i % 15 == 0: print("FizzBuzz")
    elif i % 3 == 0: print("Fizz")
    elif i % 5 == 0: print("Buzz")
    else: print(i)
```

**三項演算子ver.**

```python
for i in range(1, 101):
    print("FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i)
```

流石に読みにくいので、適切に改行を入れて読みやすくしましょう。<br>
結局改行しているので、ふつうにif文を書くのとあまり変わらないです…。

```python
for i in range(1, 101):
    print(
        "FizzBuzz" if i % 15 == 0
        else "Fizz" if i % 3 == 0
        else "Buzz" if i % 5 == 0
        else i
    )
```

<br></details>

<details><summary>C++ 解答</summary><br>

`i % 3 == 0 && i % 5 == 0` の部分は、`i % 15 == 0` でも正解です。

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 100; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
        } else if (i % 3 == 0) {
            cout << "Fizz" << endl;
        } else if (i % 5 == 0) {
            cout << "Buzz" << endl;
        } else {
            cout << i << endl;
        }
    }
}
```

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 100; i++) {
        if (i % 15 == 0) cout << "FizzBuzz" << endl;
        else if (i % 3 == 0) cout << "Fizz" << endl;
        else if (i % 5 == 0) cout << "Buzz" << endl;
        else  cout << i << endl;
    }
}
```

```cpp
#include <iostream>
using namespace std;

int main() {
    int i = 0;
    while (i < 100) {
        i++;
        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
        } else if (i % 3 == 0) {
            cout << "Fizz" << endl;
        } else if(i % 5 == 0) {
            cout << "Buzz" << endl;
        } else {
            cout << i << endl;
        }
    }
}
```

<br></details>
