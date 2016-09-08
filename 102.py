__author__ = 'alicenguyen154'
# Viet chuong trinh nhap vao 1 ngay (ngay, thang, nam), in ra ngay ke cua (ngay, thang, nam)
#input: tuple
#output: tuple ngay thang nam

'''import day_in_month_101
print day_in_month_101.day_in_month(4,2008) '''

def find_next_day(day, month, year):
    if month == 2:
        if year % 4 == 0:
            if day == 29:
                next_date = (1, 3, year)
            else:
                next_date = (day + 1, month, year)
        else:
            if day == 28:
                next_date = (1, 3, year)
            else:
                next_date = (day+1, month, year)

    if month in (1, 3, 5, 7, 8, 10):
        if day == 31:
            next_date = (1, month + 1, year)
        else:
            next_date = (day + 1, month, year)
    if month in (4, 6, 9, 11):
        if day == 30:
            next_date = (1, month + 1, year)
        else:
            next_date = (day + 1, month, year)
    if month == 12:
        if day == 31:
            next_date = (1, 1, year + 1)
        else:
            next_date = (day + 1, month, year)
    return next_date

print find_next_day(1,1,2011)
print find_next_day(28,2,2000)
print find_next_day(31,12,2009)
print find_next_day(30,9,2006)

