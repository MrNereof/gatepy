import gatepy


a = int(input("First number: "))
b = int(input("Second number: "))


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


print(adder(a, b))
