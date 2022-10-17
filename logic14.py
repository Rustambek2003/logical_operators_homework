def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    answer = 0
    m = a % 10
    n = (a // 10) % 10
    if (m + n) % 2 != 0:
        answer = True
    else:
        answer = False
    return