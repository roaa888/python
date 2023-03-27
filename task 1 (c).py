num = int(input("الرجاء إدخال رقم أكبر من 5: "))

if num <= 5:
    num = int(input("الرجاء إدخال رقم أكبر من 5: "))

sum = 0
for i in range(1, num+1):
    sum += i

print("مجموع الأرقام من 1 إلى", num, "هو:", sum)
