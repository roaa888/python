
num = int(input("الرجاء إدخال رقم أكبر من 0: "))

if num <= 0:
    num = int(input("الرجاء إدخال رقم أكبر من 0: "))

sum = 0
for i in range(1, num+1):
    sum += i

print("مجموع الأرقام من 1 إلى", num, "هو:", sum)
