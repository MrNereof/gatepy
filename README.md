# gatepy

**gatepy** is a Python implementation of a logical gate.

## Installation

Open console and run the following command:
```
pip install gatepy
```
Done.

## Examples

### Adder

```python
import gatepy

def adder(a,b):
    c = '0'
    a = list(format(a, '016b'))[::-1]
    b = list(format(b, '016b'))[::-1]
    out = []
    for i in range(16):
        S = gatepy.toint(gatepy.XOR(gatepy.XOR(gatepy.tobool(a[i]), gatepy.tobool(b[i])), gatepy.tobool(c)))
        c = gatepy.OR(gatepy.AND(gatepy.XOR(gatepy.tobool(a[i]), gatepy.tobool(b[i])), gatepy.tobool(c)),gatepy.AND(gatepy.tobool(a[i]),gatepy.tobool(b[i])))
        out.append(str(S))
    return int(''.join(out[::-1]), 2)

print(adder(1,2))
```

Return:

```
3
```