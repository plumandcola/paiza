# 論理積( AND )の基本

https://paiza.jp/works/mondai/logical_operation/logical_operation__basic_step1

<details><summary>Python3 解答</summary><br>

`and` もしくは `&` を用います。

```python
A, B = map(int, input().split())
print(A and B)
```

```python
A, B = map(int, input().split())
print(A & B)
```

<br></details>

<details><summary>C++ 解答</summary><br>

`()` をつけないと、`<<` がシフト演算子として認識されてしまい、エラーになる。<br>
以下の解答ではビット演算子 `&` を用いているが、論理演算子 `&&` や `and` を用いても良い。

```cpp
#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    cout << (A & B) << endl;
}
```

<br></details>
