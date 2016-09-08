__author__ = 'alicenguyen154'
#viet chuong trinh nhap so nguyen co 3 chu so, in ra cach doc so nguyen nay


chu_so = ('khong', 'mot', 'hai', 'ba', 'bon', 'nam', 'sau', 'bay', 'tam', 'chin')

def triple_digit(n):
    hundread
    so_hang_chuc = int(n/ 10)
    so_hang_don_vi = n % 10
    if so_hang_don_vi != 0:
        cach_doc = 'so' + ' ' + str(chu_so[so_hang_chuc]) + ' ' + str(chu_so[so_hang_don_vi])
    else:
        cach_doc = 'so' + ' ' + str(chu_so[so_hang_chuc]) + ' muoi'
    return cach_doc

print doubledigit(23)
print doubledigit(56)
