__author__ = 'alicenguyen154'
#viet chuong trinh nhap 3 so thuc, hay thay tat ca cac so am bang gia tri tuyet doi cua no
#input: a,b,c
#output: |a|, |b|, |c|

def ttd(a,b,c):
    if a >= 0:
        print a,
    else:
        print -a,
    if b >= 0:
        print b,
    else:
        print -b,
    if c >= 0:
        print c,
    else:
        print -c,

ttd (5,7,-10)
ttd (0,9,-3)
