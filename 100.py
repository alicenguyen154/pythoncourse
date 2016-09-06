__author__ = 'alicenguyen154'
#Viet chuong trinh giai phuong trinh bac 2 ax2 + bx = c, a khac 0

a = float(raw_input('Nhap a: '))
b = float(raw_input('Nhap b: '))
c = float(raw_input('Nhap c: '))


delta = b**2 - 4*a*c

if delta == 0:
    x = -b/(2*a)
    print 'Phuong trinh co nghiem duy nhat x =', x
elif delta <0:
    print 'Phuong trinh vo nghiem thuc'
else:
    import math
    squaredelta = math.sqrt(delta)
    x1 = (-b + squaredelta)/(2*a)
    x2 = (-b - squaredelta)/(2*a)
    print 'Phuong trinh co 2 nghiem la:', x1, x2
