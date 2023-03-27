num1 = int(input("الرجاء إدخال الرقم الأول: "))
num2 = int(input("الرجاء إدخال الرقم الثاني: "))
num3 = int(input("الرجاء إدخال الرقم الثالث: "))

if num1 >= num2 and num1 >= num3:
    print("الرقم الأكبر هو:", num1)
elif num2 >= num1 and num2 >= num3:
    print("الرقم الأكبر هو:", num2)
else:
    print("الرقم الأكبر هو:", num3)
