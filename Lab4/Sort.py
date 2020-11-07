def insertion_sort(arr):
    for i in range(1, len(arr)):
        currentValue = arr[i]
        currentPosition = i
        while currentPosition > 0 and arr[currentPosition - 1] > currentValue:
            arr[currentPosition] = arr[currentPosition - 1]
            currentPosition = currentPosition - 1
        arr[currentPosition] = currentValue


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        minimum = i
        for j in range(i + 1, n):
            if (arr[j] < arr[minimum]):
                minimum = j
        temp = arr[i]
        arr[i] = arr[minimum]
        arr[minimum] = temp
    return arr


L = [4, 3, 2, 1]
L2 = [4, 3, 2, 1]

insertion_sort(L)
selection_sort(L2)
print("Sorted array: " + str(L))
print("Sorted array: " + str(L2))

#Insertion Sort jest sortowaniem stabilnym

'''Selection Sort nie jest stabilne, jednak przy dodaniu dodatkowej tablicy do pamiętania indeksów
 oryginalnej tablicy stałoby się sortowaniem stabilnym'''  