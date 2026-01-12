# XNOR 演算の基本

https://paiza.jp/works/mondai/logical_operation/logical_operation__basic_step7

<details><summary>Python3 解答</summary><br>

XNORはNOT XORなので、XORを `not` で否定する。<br>
否定の部分の別解は、"否定( NOT )の基本"を参照。

```python
A, B = map(int, input().split())
print(int(not(A ^ B)))
```

**別解**

```python
A, B = map(int, input().split())
print(int(A == B))
```

ほかにもド・モルガンの法則やxorの式変形を用いて別解を導けるが、キリがないため省略。

<br></details>

<details><summary>C++ 解答</summary><br>

XNORはNOT XORなので、XORを `!` や `not` で否定する。<br>
否定の部分の別解は、"否定( NOT )の基本"を参照。

```cpp
#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    cout << !(A ^ B) << endl;
}
```

**別解**<br>
ここでも、`()` をつけないとエラーになるため注意。

```cpp
#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    cout << (A == B) << endl;
}
```

ほかにもド・モルガンの法則やxorの式変形を用いて別解を導けるが、キリがないため省略。

<br></details>
