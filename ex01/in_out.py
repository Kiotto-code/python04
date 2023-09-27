def square(x: int | float) -> int | float:
    """square"""
    return x * x


def pow(x: int | float) -> int | float:
    """power"""
    return x ** x


def outer(x: int | float, function) -> object:
    """set the count to 0 and return function that will increment the count"""
    count = 0

    def inner() -> float:
        """called the func inside as many times as it was being called"""
        nonlocal count
        count += 1
        val = x
        for i in range(count):
            val = function(val)
        return val
    return inner
