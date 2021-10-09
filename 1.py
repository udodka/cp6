A = True
while A:
    try:
        print("Введите числа через пробел и нажмите ентер:")
        array = [float(x) for x in input().split()]
    except ValueError:
        print("еррор")
    else:
        A = False
B = True
while B:
    try:
        print("Введите значение delta:")
        delta = float(input())
    except ValueError:
        print("еррор")
    else:
        B = False

min_number = array[0]

for i in range(len(array)):
    if min_number > array[i]:
        min_number = array[i]

count = 0
for i in range(len(array)):
    if array[i] == min_number + delta:
        count = count + 1

print("Вывод:", count)
