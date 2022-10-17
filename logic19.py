def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    answer = 0
    a = x % 10
    x //= 10

    b = x % 10
    X = a * 10 + b
    if X == x:
        answer = True
    else:
        answer = False

    return answer