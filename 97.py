__author__ = 'alicenguyen154'
#viet chuong trinh nhap 3 canh cua 1 tam giac, cho biet tam giac do la tam giac gi
#input: a,b,c
#output: tam giac thuong, tam giac can, tam giac deu, tam giac vuong

'''
def max(a,b,c):
    max = a
    if max <= b:
        max = b
    if max <= c:
        max = c
    return max
def min(a,b,c):
    min = a
    if min >= b:
        min = b
    if min >= c:
        min = c
    return min

print max (3,5,7)
print max (2,3,5)
print min (3,5,7)
print min (2,3,5)'''


def tamgiac(a,b,c):
    if a**2 == b**2 + c**2 or b**2 == a**2 + b**2 or c**2 == a**2 + b**2:
            print 'Tam giac ABC la tam giac vuong'
    if a == b:
        if b == c:
            print 'Tam giac ABC la tam giac deu'
        else:
            print 'Tam giac ABC la tam giac can'
    else:
        if b == c:
            print 'Tam giac ABC la tam giac can'
        if a == c:
            print 'Tam giac ABC la tam giac can'
        else:
            print 'Tam giac ABC la tam giac thuong'



tamgiac(3,4,5)
tamgiac(3,4,6)
tamgiac(5,5,7)
tamgiac(5,5,5)
tamgiac(2,3,4)