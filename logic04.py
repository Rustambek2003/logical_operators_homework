def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is even".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    answer = 0
    if a % 2 == 0 and b % 2 == 0:
        answer = "Each of the numbers 'a' and 'b' is even"
    else:
        answer = "Each of the numbers 'a' and 'b' is not even"
    return answer
print(main(44,13))