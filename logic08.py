def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one of the numbers 'a' and 'b' is even".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    answer = 0
    if a % 2 == 0 or b % 2 == 0:
        answer = True
    else:
        answer = False
    return answer
print(main(15,-16))