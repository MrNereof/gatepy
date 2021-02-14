# gatepy

[![ForTheBadge built-by-developers](http://ForTheBadge.com/images/badges/built-by-developers.svg)](https://GitHub.com/MrNereof/)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI license](https://img.shields.io/pypi/l/gatepy.svg)](https://pypi.python.org/pypi/gatepy/)
[![PyPI version fury.io](https://badge.fury.io/py/gatepy.svg)](https://pypi.python.org/pypi/gatepy/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/gatepy.svg)](https://pypi.python.org/pypi/gatepy/)

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
