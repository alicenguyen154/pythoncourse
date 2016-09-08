__author__ = 'alicenguyen154'
# Viet chuong trinh nhap vao ngay thang nam, tim ngay truoc ngay vua nhap
# input: ngay, thang, nam  (int)
# output: ngay, thang, nam (int)

def find_previous_day(day, month, year):
    if day == 1 and month == 3:
            if year % 4 == 0:
                previous_day = (29, month - 1, year)
            else:
                previous_day = (28, month - 1, year)
    if day == 1 and month == 1:
        previous_day = (31, 12, year - 1)
    if day == 1 and month in (2, 4, 6, 8, 9, 11):
        previous_day = (31, month - 1, year)
    if day == 1 and month in (3, 5, 7, 10, 12):
        previous_day = (30, month - 1, year)
    elif day != 1:
        previous_day = (day - 1, month, year)
    return previous_day
print find_previous_day(2, 2, 2002)
print find_previous_day(1, 1, 2001)
print find_previous_day(1, 10, 2010)
print find_previous_day(30, 4, 2009)
