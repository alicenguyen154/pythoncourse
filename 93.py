__author__ = 'alicenguyen154'
import math
#Viet chuong trinh kiem tra xem 1 so co phai la so nguyen to hay khong
#input : n
#output: True/ False

def kiemtrasonguyento(n):
    if n == 2:
        return True
    else:
        limit = int(math.sqrt(n))
        for i in range (2, limit):
            if n % i == 0:
                return False
            else:
                return True

print kiemtrasonguyento(7)
print kiemtrasonguyento(2)
print kiemtrasonguyento(10)
print kiemtrasonguyento(63)