def isThuanNghich(n):
    str1 = str(n);     # ep kieu so n thanh chuoi
    str2 = str1[::-1]; # dao nguoc chuoi str1
    if (str1 == str2):
        return True;
    else:
        return False;
name='Đỗ Hồng Quân'
print(name)
n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n , "là", isThuanNghich(n));
