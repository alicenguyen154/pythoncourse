__author__ = 'alicenguyen154'
''' Lap chuong trinh giai he ax + by = c
                             dx + ey = f
    Cac he so nhap tu ban phim '''

a = float(raw_input('Nhap a: ' ))
b = float(raw_input('Nhap b: ' ))
c = float(raw_input('Nhap c: ' ))
d = float(raw_input('Nhap d: ' ))
e = float(raw_input('Nhap e: ' ))
f = float(raw_input('Nhap f: ' ))


if b*d - e*a == 0:
    if c*d - a*f != 0:
        print 'He vo nghiem'
    else:
        print 'He vo so nghiem'
else:
    y = (c*d - a*f)/(b*d-e*a)
    if a != 0:
        x = (c - b*y)/a
    else:
        x = (f -e*y)/d
    print 'x =', x
    print 'y =', y


