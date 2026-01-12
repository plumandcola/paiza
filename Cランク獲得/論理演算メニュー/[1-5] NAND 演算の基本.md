# NAND 演算の基本

https://paiza.jp/works/mondai/logical_operation/logical_operation__basic_step5

<details><summary>Python3 解答</summary><br>

NANDはNOT ANDなので、ANDを `not` で否定する。<br>
否定の部分の別解は、"否定( NOT )の基本"を参照。<br>
また、"論理積( AND )の基本"で述べた通り、`and` の部分は `&` を用いても良い。

```python
A, B = map(int, input().split())
print(int(not(A and B)))
```

**別解**<br>
ド・モルガンの法則より、`not(A and B)` = `not A or not B` を用いても良い。

```python
A, B = map(int, input().split())
print(int(not A or not B))
```

<br></details>

<details><summary>C++ 解答</summary><br>

NANDはNOT ANDなので、ANDを `!` や `not` で否定する。<br>
否定の部分の別解は、"否定( NOT )の基本"を参照。<br>
また、"論理積( AND )の基本"で述べた通り、`&` の部分は `&&` や `and` を用いても良い。

```cpp
#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    cout << !(A & B) << endl;
}
```

**別解**<br>
ド・モルガンの法則より、`!(A & B)` = `!A | !B` を用いても良い。<br>
`()` をつけ忘れないこと。<br>
また、"論理和( OR )の基本"で述べた通り、`|` の部分は `||` や `or` を用いても良い。

```cpp
#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    cout << (!A | !B) << endl;
}
```

<br></details>
