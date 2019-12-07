# Strings

### Initialization

```python
string = ""
```

### Runtime Analysis

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| index            | O(1)             |

```python
string = "hi! how are you"

string[4] 
# returns "h"
```

| Function | Big O Complexity |
| --- | --- |
| length | O(1) |

```python
string = "hi! how are you"

len(string)
# returns 15
```

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| concatenation | O(N)   | 

```python
string = "hi! how are you"

string2 = "?"
string += string2
# string = "hi! how are you?"
```

| Function         | Big O Complexity |
| ---------------- | ---------------- |
| slicing          | O(K)             | 

```python
string = "hi! how are you"

string[:3]
# returns "hi!"

string[8:]
# returns "are you"

string[2:7]
# returns "! how"
```

| Function | Big O Complexity |
| --- | --- |
| equal to | O(N) |
| not equal to | O(N) |

```python
string = "hi! how are you"

string2 = "hi! how are you"
string == string2
# returns True

string3 = "what's up?"
string != string3
# returns True
```

| Function | Big O Complexity |
| --- | --- |
| iteration | O(N) |

```python
string = "hi! how are you"

for i in string:
    print(i, end=" ")
# returns "h i !   h o w   a r e   y o u "
```