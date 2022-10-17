def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is even".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    answer = ""
    if a % 2 == 0:
        answer += "the numbers 'a' is even "
    else:
        answer += "the numbers 'a' is not even "
    if b % 2 == 0:
        answer += "the numbers 'b' is even"
    else:
         answer += "the numbers 'b' is not even"
    return answer
print(main(44,13))