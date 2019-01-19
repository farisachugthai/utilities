def gcdRecur(a, b):
    if b == 0:
        return a
    if b > a:
        tmp = b
        b = a
        a = tmp
    return gcdRecur(b, a % b)
