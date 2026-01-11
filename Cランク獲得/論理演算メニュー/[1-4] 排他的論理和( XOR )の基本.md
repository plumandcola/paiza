# 排他的論理和( XOR )の基本

https://paiza.jp/works/mondai/logical_operation/logical_operation__basic_step4

<details><summary>Python3 解答</summary><br>

ビット演算子 `^` を用います。

```python
A, B = map(int, input().split())
print(A ^ B)
```

**別解**<br>
単に `A != B` とするだけでは `True` か `False` が返されるため、int型に変換します。

```python
A, B = map(int, input().split())
print(int(A != B))
```

**そのほかの別解**<br>
xorを変形して、頑張って実装しても良い。(xorの変形についてはWikipediaなどを参照。)

```python
A, B = map(int, input().split())
print(int((A and not B) or (not A and B)))
```

```python
A, B = map(int, input().split())
print(int((A or B) and (not A or not B)))
```

```python
A, B = map(int, input().split())
print(int((A or B) and not (A and B)))
```

<br></details>

<details><summary>C++ 解答</summary><br>

今までと同様、`()` をつけないと、`<<` がシフト演算子として認識されてしまい、エラーになる。<br>
`^` または `xor` を用いる。

```cpp
#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    cout << (A ^ B) << endl;
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
    cout << (A != B) << endl;
}
```

**そのほかの別解**<br>
xorを変形して、頑張って実装しても良い。(xorの変形についてはWikipediaなどを参照。)

```cpp
#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    cout << ((A & !B) | (!A & B)) << endl;
}
```

```cpp
#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    cout << ((A | B) & (!A | !B)) << endl;
}
```

```cpp
#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    cout << ((A | B) & !(A & B)) << endl;
}
```

<br></details>
