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
    s = 0
    if a > b and b > c:
        s = "The number b is between a and c"
    elif c > b and b > a:
        s = "The number b is between a and c"
    else:
        s = "The number b is not between a and c"

    return s
print(main(9,3,5))