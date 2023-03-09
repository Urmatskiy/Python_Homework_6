# # Определить индексы элементов массива (списка),
# # значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = list(map(int, input().split()))
low = int(input())
high = int(input())

for i in range(len(list_1)):
    if low <= list_1[i] <= high:
        print(i, end=" ")


