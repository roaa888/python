# 1
# n = int(input("Enter the number of elements in the array: "))
# while n <= 0:
#     n = int(input("The number of elements must be greater than zero. Please enter again: "))
#
# arr = []
# for i in range(n):
#     x = int(input(f"Enter number {i+1}: "))
#     arr.append(x)
#
# print(f"The number of numbers is: {n}")
# print("Elements in the array:", end=" ")
# for i in range(n):
#     print(arr[i], end="")
#     if i != n-1:
#         print(",", end=" ")

#2
# def PrintSecondLowest(arr):
#     if len(arr) < 2:
#         print("An array must contain at least two elements")
#         return
#     small = min(arr)
#     second_number = int('inf')
#     for num in arr:
#         if num < second_number and num != small:
#             second_number = num
#         print("The second smallest element in the array is:", second_number)


#3
# for i in range(1, 13):
#     if i != 1:
#         print()
#     for j in range(1, 13):
#         print(i, 'x', j, '=', i*j)

#4
# a=0
# b=1
# while a <=6765:
#     print(a, end=" ") #we use "end to make sure that all the numbers written on the same line.
#     a,b = b, a + b


    # num = 12
    # for j in range(1, 13):
    #  for i in range(1, 11):
    #     print(num, 'x', i, '=', num * i)



# rows = int(input('Enter the number of rows: '))
# if rows>=1:
#  for i in range(rows):
#     for j in range(i):
#         print("*", end=' ')
#     print('')
# else:
#     print("Please enter a number greater than 0 ")

#1
# rows = int(input('Enter the number of rows: '))
# i = rows
# while i >= 1:
#     j = rows
#     while j > i:
#         # display space
#         print(' ', end=' ')
#         j -= 1
#     k = 1
#     while k <= i:
#         print('*', end=' ')
#         k += 1
#     print()
#     i -= 1


#2
# rows = int(input("Enter rows:"))
# cols = int(input("Enter Cols:"))
#
# for i in range(0, rows):
#     for j in range(1, i+1):
#         print(" ", end="")
#     for j in range(0, cols):
#         print("*", end="")
#     print()

#3
# num_rows = int(input("Enter the number of rows"));
# for i in range(0, num_rows):
# 	for j in range(0, num_rows-i-1):
# 		print(end=" ")
# 	for j in range(0, i+1):
# 		print("*", end=" ")
# 	print()



#4
# rows = int(input('Enter the number of rows: '))
# if rows >=0:
#   k = 2 * rows - 2
#   for i in range(rows, -1, -1):
#     for j in range(k, 0, -1):
#      print(end=" ")
#     k = k + 1
#     for j in range(0, i + 1):
#         print("*", end=" ")
#     print("")
# else:
#  print("Please enter a number greater than 0 ")


#q5
# rows = int(input('Enter the number of rows: '))
# if rows >=0:
#  for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print(" ")
# for i in range(rows + 1, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")


#8
# size = int(input("Enter the size of the butterfly pattern: "))
# for i in range(size):
#     for j in range(2*size):
#         if j == 2*size-1 or j == i or j == 2*size-2-i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# for i in range(size):
#     for j in range(2*size):
#         if j == 2*size-1 or j == size-1-i or j == size+i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


