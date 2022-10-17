def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    answer = 0
    if a > 9 and a < 100:
        answer = True
    else:
        answer = False
    return answer