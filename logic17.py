def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    answer = 0
    n = a % 10
    a //= 10

    m = a % 10
    a //= 10

    p = a % 10
    a //= 10

    k = a % 10
    a //= 10

    l = a % 10
    if l > k and k > p and p > m and m > n:
        answer = True
    else:
        answer = False
    return answer 