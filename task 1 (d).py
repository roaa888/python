
num = int(input("الرجاء إدخال رقم أكبر من 5: "))

if num <= 5:
    num = int(input("الرجاء إدخال رقم أكبر من 5: "))

product = 1
for i in range(1, num+1):
    product *= i

print("ضرب الأرقام من 1 إلى", num, "هو:", product)
