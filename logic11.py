def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
     answer = 0
    if a > 99 and a < 1000:
        answer = True
    else:
        answer = False
    return answer