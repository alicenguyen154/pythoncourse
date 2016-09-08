__author__ = 'alicenguyen154'
#Viet chuong trinh nhap thang, nam, hay cho biet thang do co bao nhieu ngay

def find_total_day(month, year):

    if month == 2:
        if year % 4 == 0:
            total_day = 29
        else:
            total_day = 28

    if month != 2:
        if month in (1, 3, 5, 7, 8, 10, 12):
            total_day = 31
        else:
            total_day = 30

    return total_day

print find_total_day(4,2016)
print find_total_day(3,2009)
print find_total_day(2,2008)
print find_total_day(7,2009)
