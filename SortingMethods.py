def bubbleSort(numbers):
    x = len(numbers)-1
    for i in range(x):
        for j in range(0, x-i):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp

def selectionSort(numbers):
    x= len(numbers)
    for i in range(x):
        min = i
        for j in range(i+1, x):
            if numbers[j]<numbers[min]:
                min = j
        temp = numbers[i]
        numbers[i] = numbers[min]
        numbers[min] = temp


numbers = [1, -5,4,8.5]
print(numbers)
bubbleSort(numbers)
print(numbers)

numbers = [1, -5, 4 ,8.5]
print(numbers)
selectionSort(numbers)
print(numbers)