def make_bricks(small, big, goal):
    """
    Make bricks
    https://codingbat.com/prob/p118406
    """
    if big > 0 and small < goal % 5:
        return False
    elif small + (big * 5) >= goal:
        return True
    
    return False

def lone_sum(a, b, c):
    """
    lone_sum
    https://codingbat.com/prob/p143951
    """
    if a == b and b == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    return a + b + c

def lucky_sum(a, b, c):
    """
    locky_sum
    https://codingbat.com/prob/p107863
    """
    if a == 13: return 0
    if b == 13: return a
    if c == 13: return a + b
    return a + b + c