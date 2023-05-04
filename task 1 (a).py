#task 1
n = int(input("أدخل عدد عناصر المصفوفة: "))
while n <= 0:
    n = int(input("يجب أن يكون عدد عناصر المصفوفة أكبر من صفر، أدخلها مجدداً: "))

arr = []
for i in range(n):
    element = int(input(f"أدخل العنصر رقم {i+1}: "))
    arr.append(element)

print("عدد عناصر المصفوفة:", n)
print("القيم المخزنة في المصفوفة:", end=" ")
for element in arr:
    print(element, end=" ")

#task 2
def PrintSecondLowest(arr):
    # تحقق من أن الطول يكون أكبر من 2
    if len(arr) < 2:
        print("لا يمكن العثور على العنصر الثاني الأصغر")
        return
    # ترتيب المصفوفة بترتيب تصاعدي
    arr.sort()
    # طباعة العنصر الثاني في المصفوفة
    print("العنصر الثاني الأصغر هو: ", arr[1])

#task 3
for i in range(1, 13):
    for j in range(1, 13):
        print(i*j, end='\t')
    print('\n')

#task 4
# تعريف المتغيرين الأول والثاني
a, b = 0, 1
count = 0

# استخدام الحلقة while loop لإنشاء السلسلة
while count < 20:
    print(a, end=' ')
    c = a + b
    a, b = b, c
    count += 1

#تمرين التاني
# (1)
n = int(input("أدخل عدد الأسطر: "))
while n <= 0:
    n = int(input("يجب أن يكون عدد الأسطر أكبر من صفر. أعد المحاولة: "))

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

#(2)
# طلب عدد الأسطر والأعمدة من المستخدم
num_rows = int(input("أدخل عدد الأسطر: "))
num_columns = int(input("أدخل عدد الأعمدة: "))

# التأكد من أن عدد الأسطر والأعمدة أكبر من صفر
if num_rows <= 0 or num_columns <= 0:
    print("يجب أن يكون عدد الأسطر والأعمدة أكبر من صفر!")
else:
    # الحلقتان الداخليتان تقومان بطباعة النجوم والمسافات لكل سطر
    for i in range(num_rows):
        for j in range(num_columns):
            print("*", end="")
        print()

#(3)
rows = int(input("Enter number of rows: "))

for i in range(rows):
    # تحديد عدد النجوم في السطر الحالي
    num_stars = 2 * i + 1

    # طباعة النجوم في السطر الحالي
    for j in range(num_stars):
        print("*", end="")

    # إضافة سطر فارغ بعد كل سطر ما عدا السطر الأخير
    if i != rows - 1:
        print()

#(4)
num_rows = int(input("أدخل عدد الأسطر: "))

# التكرار على عدد الأسطر المدخل
for i in range(num_rows, 0, -1):
    # النجوم المطلوبة في كل سطر
    num_stars = 2 * i - 1
    # طباعة النجوم في كل سطر
    for j in range(num_stars):
        print("*", end="")
    print()

#(5)
rows = int(input('Enter the number of rows: '))
if rows >=0:
    for i in range(0, rows):
     for j in range(0, i + 1):
         print("*", end=' ')
         print(" ")
         for i in range(rows + 1, 0, -1):
             for j in range(0, i - 1):
                 print("*", end=' ')
     print(" ")

#(6)
num = int(input("Enter number of rows: "))
space = 3
for i in range(num):
    for j in range(num-i):
        print(" ", end="")
    for j in range(2*i+1):
        if j%2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    for j in range(space):
        print(" ", end="")
    for j in range(2*(num-i-1)+1):
        if j%2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#(7)

#(8)
rows = int(input("Enter an odd number of rows: "))
if rows % 2 == 0:
    rows += 1

for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1 or i == j or i + j == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


