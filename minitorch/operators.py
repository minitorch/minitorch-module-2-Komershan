"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable, List
# Tuta ya usau annotasii tipov tipa float int tam vse dela
# Mi tak delaem na raboti soooo ya schitay nado i v ds :)
# Privet Mishan navernoe ili assist

def mul(a: float, b: float) -> float:
    """
    Implements multiplication operation
    
    Args:
        a (float): First number for multipliaction.
        b (float): Second number for multipliaction.

    Returns:
        float: The calculated multiplication of a and b
    """

    return a * b

def id(a: float) -> float:
    """
    Implements identity operator
    
    Args:
        a (float): Number to be identity

    Returns:
        float: Identity return
    """

    return a

def add(a: float, b: float) -> float:
    """
    Implements addition operation
    
    Args:
        a (float): First number for addition.
        b (float): Second number for addition.

    Returns:
        float: The calculated addition of a and b
    """

    return a + b

def neg(a: float) -> float:
    """
    Implements negative operation
    
    Args:
        a (float): Number for operation

    Returns:
        float: Calculated negative of a
    """

    return -float(a)

def lt(a: float, b: float) -> bool:
    """
    Checks if a is less than b
    
    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        bool: True if a < b and False otherwise
    """

    return a < b

def eq(a: float, b: float) -> bool:
    """
    Checks if a is equal to b
    
    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        bool: True if a = b and False otherwise
    """

    return a == b

def max(a: float, b: float) -> float:
    """
    Returns maximum from a and b
    
    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: maximum for a and b
    """

    if lt(a, b):
        return b
    else:
        return a
    
def is_close(a: float, b: float) -> bool:
    """
    Check if a and b are close
    
    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        bool: True if a and b are close (|a - b| < 1e-2)
        and False otherwise
    """

    mod = max(a - b, b - a)
    return lt(mod, 1e-2)

def exp(x: float) -> float:
    """
    Calculates exp(x)
    
    Args:
        x (float): Argument for exponent function.

    Returns:
        float: result of calculation (exp(x))
    """ 

    return math.exp(min(x, 700))



def log(x: float) -> float:
    """
    Calculates log(x)
    
    Args:
        x (float): Argument for logarithm function.

    Returns:
        float: result of calculation (log(x))
    """ 

    return math.log(max(x, 1e-6))

def inv(a: float) -> float:
    """
    Calculates 1 divide a
    
    Args:
        a (float): Number.

    Returns:
        float: result of 1 divide a
    """ 

    return 1 / a

def sigmoid(x: float) -> float:
    """
    Calculates sigmoid(x)
    
    Args:
        x (float): Argument for sigmoid function.

    Returns:
        float: result of calculation (sigmoid(x))
    """ 

    if x >= 0:
        return inv(add(1, exp(-x)))
    else:
        return mul(exp(x), inv(add(1, exp(x))))

def relu(x: float) -> float:
    """
    Calculates relu(x)
    
    Args:
        x (float): Argument for relu function.

    Returns:
        float: result of calculation (relu(x))
    """ 

    return max(0.0, x)

def log_back(a: float, b: float) -> float:
    """
    Calculates ln(a)' * b
    
    Args:
        a (float): First number for operation.
        b (float): Second number for operation.

    Returns:
        float: Calculated mathematical expression
    """

    return mul(inv(a), b)

def inv_back(a: float, b: float) -> float:
    """
    Calculates inv(a)' * b
    
    Args:
        a (float): First number for operation.
        b (float): Second number for operation.

    Returns:
        float: Calculated mathematical expression
    """

    return -inv(mul(a, a)) * b

def relu_back(a: float, b: float) -> float:
    """
    Calculates relu(a)' * b
    
    Args:
        a (float): First number for operation.
        b (float): Second number for operation.

    Returns:
        float: Calculated mathematical expression
    """

    return lt(0.0, a) * b



# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


def map(fn: Callable[[float], float], xs: List[float]) -> List[float]:
    """Apply a function to each element of a list.

    Args:
        fn (Callable[[float], float]): Function to apply.
        xs (List[float]): List of elements.

    Returns:
        List[float]: List with application results.
    """
    return [fn(x) for x in xs]


def zipWith(fn: Callable[[float, float], float], xs: List[float], ys: List[float]) -> List[float]:
    """Combine elements using a function.

    Args:
        fn (Callable[[float, float], float]): Function to combine elements.
        xs (List[float]): First list.
        ys (List[float]): Second list.

    Returns:
        List[float]: List of combined elements.
    """
    return [fn(x, y) for x, y in zip(xs, ys)]


def reduce(fn: Callable[[float, float], float], xs: List[float], start: float) -> float:
    """Reduce a list to value.

    Args:
        fn (Callable[[float, float], float]): Function to combine two elements.
        xs (List[float]): List to reduce.
        start (float): Initial value.

    Returns:
        float: Reduced value.
    """
    result = start
    for x in xs:
        result = fn(result, x)
    return result


# Using higher-order operators

def negList(xs: List[float]) -> List[float]:
    """Turn list to negatives using function neg

    Args:
        xs (List[float]): List of numbers.

    Returns:
        List[float]: Produced list
    """
    return map(lambda x: neg(x), xs)


def addLists(xs: List[float], ys: List[float]) -> List[float]:
    """Add two lists

    Args:
        xs (List[float]): First list.
        ys (List[float]): Second list.

    Returns:
        List[float]: List with c_i = a_i + b_i
    """
    return zipWith(add, xs, ys)


def sum(xs: List[float]) -> float:
    """Compute cumulative sum of list

    Args:
        xs (List[float]): List of numbers.

    Returns:
        float: Sum of all elements.
    """
    return reduce(add, xs, 0.0)


def prod(xs: List[float]) -> float:
    """Compute product of all elements in list

    Args:
        xs (List[float]): List of numbers.

    Returns:
        float: Product of all elements.
    """
    return reduce(mul, xs, 1.0)


