#tim so nguyen duong nho nhat sao cho 1+2+3+...n > 10000
#input: none
#output: n
def tongso(n):
    if n > 1:
        return n + tongso(n-1)
    else:
        return 1

for n in range (1,200):
    if tongso(n)<10000:
        if tongso(n+1)>10000:
            print n+1

i = 0
total = 0
while total <= 10000:
        i += 1
        total += i
print (i)