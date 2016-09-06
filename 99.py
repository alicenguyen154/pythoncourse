__author__ = 'alicenguyen154'
# viet chuong trinh nhap 3 so thuc, in ra man hinh 3 so ay theo thu tu tang dan ma chi dung 1 bien phu
# input a b c
# output  a b c thu tu tang dan
a = float(raw_input('Nhap a: '))
b = float(raw_input('Nhap b: '))
c = float(raw_input('Nhap c: '))


min = a
if min >= b:
    min = b
if min >= c:
    min = c

if min == a:
    if b <= c:
        print min, b, c
    else:
        print min, c, b
if min == b:
    if a <= c:
        print min, a, c
    else:
        print min, c, a
if min == c:
    if a <= b:
        print min, a, b
    else:
        print min, b, a
