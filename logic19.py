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
    b = (x // 10) % 10
    c = x // 100
    X = a * 100 + b * 10 + c
    if X == x:
        answer = True
    else:
        answer = False
    return answer
print(main(525))