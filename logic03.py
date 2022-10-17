def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is negative".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    if a < 0 and b < 0:
        answer = "Each of the numbers 'a' and 'b' is negative"
    else:
        answer = "Each of the numbers 'a' and 'b' is not negative"
    return answer
print(main(-4,-6))