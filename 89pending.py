'''#viet chuong trinh tinh tong cac gia tri le nguyen duong nho hon n
#input n
#output S(n) = 1 + 3 + 5 + ... + (n-1) if n = 2k
#output S(n) = 1 + 3 + 5 + ..  +  n-2 if n = 2k+1

def tonggiatrile(n):
    i = 1
    total = 1
    chantren = 0
    if n%2 == 0:
        chantren = n - 2
    else:
        chantren = n - 1

    while i <= chantren:
        i = i + 2
        total = total + i
    return total


print tonggiatrile(3)
print tonggiatrile(7)
print tonggiatrile(6)

def tonggiatrile(n):
    total = 0
    for i in range (1, n+1):
        if i% 2 == 1:
            total += i
    return total
print tonggiatrile(3)'''

def tonggiatrile(n):
    total = 0
    i = 1
    while i < n:
        total = total + i
        i = i + 2
    return total

print tonggiatrile(3)
print tonggiatrile(5)
print tonggiatrile(1)
print tonggiatrile(8)








''' #include<stdio.h>
#include<conio.h>

int main()
{
	/*int S, i, n;
	printf("\nNhap n: ");
	scanf("%d", &n);

	for(i = 1, S = 0; i < n; i+=2)
	{
		S = S + i;
	}
	printf("\nTong = %d", S);*/

	int S, i, n;
	S = 0;
	i = 1;
	printf("\nNhap n: ");
	scanf("%d", &n);
	for(;;)
	{
		S = S + i;
		i = i + 2;
		if(i >= n)
			break;
	}
	printf("\nTong = %d", S);
	getch();
	return 0;
z}'''

