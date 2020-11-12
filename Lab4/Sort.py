def insertion_sort(array):
    for i in range(1, len(array)):
        currentValue = array[i]
        currentPosition = i
        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition - 1]
            currentPosition = currentPosition - 1   # -= 1
        array[currentPosition] = currentValue


def selection_sort(array):
    n = len(array)
    for i in range(n):
        minimum = i # sugeruję min_index, albo argmin, dla odróżnienia, że to nie jest najmniejsza wartość, tylko indeks pod którym się znajduje
        for j in range(i + 1, n):
            if (array[j] < array[minimum]):
                minimum = j
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp   # a, b = b, a
    return array


L = [4, 3, 2, 1]
L2 = [4, 3, 2, 1]

insertion_sort(L)
selection_sort(L2)
print("Sorted array: " + str(L))
print("Sorted array: " + str(L2))

#Insertion Sort jest sortowaniem stabilnym

'''Selection Sort nie jest stabilne, jednak przy dodaniu dodatkowej tablicy do pamiętania indeksów
 oryginalnej tablicy stałoby się sortowaniem stabilnym'''  
