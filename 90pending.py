#viet chuong trinh tim so nguyen duong m lon nhat sao cho 1 + 2 + 3 + .. + m < N
#input: N
#output: m

def timsolonnhat(n):
    i = 1
    total = 1
    if n == 1:
        return False
    elif n > 1:
        while total < n:
            i += 1
            total += i
        return i-1

print timsolonnhat(5)
print timsolonnhat(1)
print timsolonnhat(10)

“”“
include<stdio.h>
include<conio.h>

int main()
{
	int N, m, S;
	printf("\nNhap N: ");
	scanf("%d", &N);

	S = 0;
	m = 0;
	do
	{
		m = m + 1;
		S = S + m;
	}while(S + m + 1 < N);
	printf("\nSo nguyen duong m la %d", m);
	getch();
	return 0;