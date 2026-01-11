# 否定( NOT )の基本

https://paiza.jp/works/mondai/logical_operation/logical_operation__basic_step3

<details><summary>Python3 解答</summary><br>

ブール演算子(論理演算子) `not` を用います。ただし、単に `not A` とするだけでは `True` か `False` が返されるため、int型に変換します。

```python
A = int(input())
print(int(not A))
```

**別解1**

```python
A = int(input())
print(1 - A)
```

**別解2**<br>
次の問題で扱うXORを用いても良い。

```python
A = int(input())
print(A ^ 1)
```

<br></details>

<details><summary>C++ 解答</summary><br>

`!` または `not` を用いる。

```cpp
#include <iostream>
using namespace std;

int main() {
    int A;
    cin >> A;
    cout << !A << endl;
}
```

**別解1**

```cpp
#include <iostream>
using namespace std;

int main() {
    int A;
    cin >> A;
    cout << not A << endl;
}
```

**別解2**

```cpp
#include <iostream>
using namespace std;

int main() {
    int A;
    cin >> A;
    cout << 1 - A << endl;
}
```

**別解3**<br>
次の問題で扱うXORを用いても良い。

```cpp
#include <iostream>
using namespace std;

int main() {
    int A;
    cin >> A;
    cout << (A ^ 1) << endl;
}
```

<br></details>
