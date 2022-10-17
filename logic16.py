def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    answer = 0
    if a > 9999 and a < 100000:
        answer = True
    else:
        answer = False
    return answer