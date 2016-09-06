__author__ = 'alicenguyen154'
#Viet chuong trinh nhap thang, nam, hay cho biet thang do co bao nhieu ngay

thang = int(raw_input('Nhap thang: '))
nam = int(raw_input('Nhap nam:'))

if nam % 4 == 0:
    if thang == 2:
        print 'Thang', thang, 'nam', nam, 'co 29 ngay'
    if thang % 2 == 1:
        if thang < 8:
            print 'Thang', thang, 'nam', nam, 'co 31 ngay'
        else:
            print 'Thang', thang, 'nam', nam, 'co 30 ngay'
    elif thang < 8:
        print 'Thang', thang, 'nam', nam, 'co 30 ngay'
    else:
        print 'Thang', thang, 'nam', nam, 'co 31 ngay'