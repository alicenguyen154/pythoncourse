__author__ = 'alicenguyen154'
# Viet chuong trinh nhap ngay thang nam, tinh xem ngay do la ngay thu bao nhieu trong nam
# input: ngay thang nam
# output: vi tri ngay trong nam

def date_position(day, month, year):
    day_in_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_in_normal_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0:
        position_day = day + sum(day_in_leap_year[0: month-1])
    else:
        position_day = day + sum(day_in_normal_year[0:month-1])
    return position_day
print date_position(3, 1, 2000)
print date_position(1, 2, 2000)
print date_position(1, 3, 2000)
print date_position(31, 12, 1999)


