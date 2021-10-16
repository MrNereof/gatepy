import gatepy


def test_NOT():
    assert not gatepy.NOT(True)
    assert gatepy.NOT(False)


def test_OR():
    assert gatepy.OR(True, True)
    assert gatepy.OR(False, True)
    assert gatepy.OR(True, False)
    assert not gatepy.OR(False, False)


def test_AND():
    assert gatepy.AND(True, True)
    assert not gatepy.AND(False, True)
    assert not gatepy.AND(True, False)
    assert not gatepy.AND(False, False)


def test_NAND():
    assert not gatepy.NAND(True, True)
    assert gatepy.NAND(False, True)
    assert gatepy.NAND(True, False)
    assert gatepy.NAND(False, False)


def test_NOR():
    assert not gatepy.NOR(True, True)
    assert not gatepy.NOR(False, True)
    assert not gatepy.NOR(True, False)
    assert gatepy.NOR(False, False)


def test_XOR():
    assert not gatepy.XOR(True, True)
    assert gatepy.XOR(False, True)
    assert gatepy.XOR(True, False)
    assert not gatepy.XOR(False, False)


def test_XNOR():
    assert gatepy.XNOR(True, True)
    assert not gatepy.XNOR(False, True)
    assert not gatepy.XNOR(True, False)
    assert gatepy.XNOR(False, False)
