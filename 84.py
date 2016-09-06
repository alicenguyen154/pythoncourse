#viet chuong trinh giai va bien luan phuong trinh bac nhat ax + b = 0
#input: a, b
#output: ham 1 nghiem duy nhat  x = -b/a, vo nghiem = False, vo so nghiem = True

def phuongtrinhbacnhat(a, b):
    if a == 0:
        if b == 0:
            return True
        else:
            return False
    else:
        return -b/a

print phuongtrinhbacnhat (1,3)
print phuongtrinhbacnhat (0,3)
print phuongtrinhbacnhat (0,0)



