__author__ = 'alicenguyen154'
''' viet chuong trinh nhap gia tri x sau khi tinh gia tri cua ham so
f(x) = 5x^2 + 2x + 9 when x >= 5
f(x) = -2x^2 + 4x - 9 when x < 5 '''
#input: x
#output: gia tri f(x)


x = float(raw_input('Nhap x:', ))
if x >= 5:
    hamso = 5*x**2 + 2*x + 9
else:
    hamso = -2*x**2 + 4*x - 9
print 'Gia tri cua f(x) la:', hamso





