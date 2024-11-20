"""An example of recursive functions"""


def factorial(n: int) -> int:
    """calculate product of alll postivive integers less than or equal to an int,n"""
    # Base case
    if n == 0 or n == 1:
        return 1
    # recursive cases
    else:
        return n * factorial(n - 1)


# Example usage
print(factorial(3))
