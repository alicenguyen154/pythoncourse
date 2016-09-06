#in tat ca cac so nguyen duong le nho hon 100
#input: none
#output: day cac so le
"""
def indaysole(n):
    i = -1
    if n % 2 == 0:
        while i <= n-2:
            i = i + 2
            print i
    else:
        while i <= n-3:
            i += 2
            print i

print indaysole(5)
print indaysole(1)
print indaysole(100) """

def indaysole(n):
    i = 1
    while i < n:
        print i
        i += 2

indaysole(7)
indaysole(14)
indaysole(8)