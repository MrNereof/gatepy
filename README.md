# gatepy

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI license](https://img.shields.io/pypi/l/gatepy.svg)](https://pypi.python.org/pypi/gatepy/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/gatepy.svg)](https://pypi.python.org/pypi/gatepy/)
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


def adder(a, b):
    c = False
    a = list(format(a, "064b"))[::-1]
    b = list(format(b, "064b"))[::-1]
    out = []
    for i in range(64):
        S = int(
            gatepy.XOR(
                gatepy.XOR(int(a[i]), int(b[i])), c
            )
        )
        c = gatepy.OR(
            gatepy.AND(
                gatepy.XOR(int(a[i]), int(b[i])), c
            ),
            gatepy.AND(int(a[i]), int(b[i])),
        )
        out.append(str(S))
    return int("".join(out[::-1]), 2)


print(adder(1, 2))

```

Return:

```
3
```