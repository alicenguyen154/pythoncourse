# tim so lon nhat trong 3 so a, b, c

def findMax(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

print findMax(3,3,1)