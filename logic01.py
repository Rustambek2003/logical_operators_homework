def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    answer = 0
    if a > b and b > c:
        answer = True
    elif c > b and b > a:
        answer = True
    else:
        answer = False
    
    return answer
print(main(14,13,12))