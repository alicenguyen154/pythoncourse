__author__ = 'alicenguyen154'
#tim uoc so chung lon nhat cua 2 so nguyen duong
#input: a b
#output: uoc so chung lon nhat

def gcd(a, b):
    for i in range (1, b+1):
           if a % i == 0:
               if b % i ==0:
                    j = i
    print j
gcd(12,7)
gcd(35,15)
gcd(16,20)