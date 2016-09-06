#tinh S(n) = 1^3+2^3+.. + n^3
#input:n
#output: S(n)
def tongbac3(n):
    if n > 1:
        return n^3+tongbac3(n-1)
    else:
        return n

print tongbac3(3)
print tongbac3(1)



