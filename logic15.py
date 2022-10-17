def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    answer = 0
    m = a % 10
    a //= 10

    n = a % 10
    a //= 10

    p = a % 10

    if (m + n + p) % 2 != 0:
        answer = True
    else:
        answer = False
    return answer