'''#tim so nguyen duong nho nhat sao cho 1+2+3+...n > 10000
#input: none
#output: n
def tongso(n):
    if n > 1:
        return n + tongso(n-1)
    else:
        return 1

for n in range (1,10000):
    if tongso(n)<10000:
        if tongso(n+1)>10000:
            print n+1
            break '''
sum = 0
n = int(raw_input('Nhap so:'))
for i in range (1, n+1):
    sum += i

print 'Tong so tu 1 toi', n, sum









