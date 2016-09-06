#tim uoc so chung lon nhat cua 2 so nguyen duong
#input: a b
#output: uoc so chung lon nhat

def gcd(a, b):
    if a > b:
        while a % b > 0:
            c = a % b
            a = b
            b = c
        return b


print gcd(12,7)
print gcd(35,15)
print gcd(20,16)

