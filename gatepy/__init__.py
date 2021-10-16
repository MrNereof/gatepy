def NOT(a: bool) -> bool:
    """NOT logical gate
    
    Args:
        a (bool): First input signal
    
    Returns:
        bool: Output signal
    """
    return not a


def OR(a: bool, b: bool) -> bool:
    """OR logical gate
    
    Args:
        a (bool): First input signal
        b (bool): Second input signal
    
    Returns:
        bool: Output signal
    """
    return a or b


def AND(a: bool, b: bool) -> bool:
    """AND logical gate
    
    Args:
        a (bool): First input signal
        b (bool): Second input signal
    
    Returns:
        bool: Output signal
    """
    return a and b


def NAND(a: bool, b: bool) -> bool:
    """NAND logical gate
    
    Args:
        a (bool): First input signal
        b (bool): Second input signal
    
    Returns:
        bool: Output signal
    """
    return NOT(AND(a, b))


def NOR(a: bool, b: bool) -> bool:
    """NOR logical gate
    
    Args:
        a (bool): First input signal
        b (bool): Second input signal
    
    Returns:
        bool: Output signal
    """
    return NOT(OR(a, b))


def XOR(a: bool, b: bool) -> bool:
    """XOR logical gate
    
    Args:
        a (bool): First input signal
        b (bool): Second input signal
    
    Returns:
        bool: Output signal
    """
    return OR(AND(NOT(a), b), AND(a, NOT(b)))


def XNOR(a: bool, b: bool) -> bool:
    """XNOR logical gate
    
    Args:
        a (bool): First input signal
        b (bool): Second input signal
    
    Returns:
        bool: Output signal
    """
    return NOT(XOR(a, b))
