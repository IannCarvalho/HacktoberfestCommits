def sort(array, leftIndex, rightIndex):
    if (leftIndex < rightIndex):
        mid = (leftIndex + rightIndex) / 2
        sort(array, leftIndex, mid)
        sort(array, mid + 1, rightIndex)
        merge(array, leftIndex, mid, rightIndex)


def merge(array, leftIndex, mid, rightIndex):
    i = leftIndex
    j = mid + 1
    k = leftIndex

    aux = list(array)

    while (i <= mid and j <= rightIndex):
        if (aux[i] < (aux[j])):
            array[k] = aux[i]
            i += 1
        else:
            array[k] = aux[j]
            j += 1
        k += 1

    while (i <= mid):
        array[k] = aux[i]
        i += 1
        k += 1

    while (j <= rightIndex):
        array[k] = aux[j]
        k += 1
        j += 1

array = [9, 14, 3, 2, 43, 11, 58, 22]
print("Before Sort")
listString = ""
for num in array:
    listString += str(num) + " "
print listString

sort(array, 0, len(array)-1)

print("After Sort")
listString = ""
for num in array:
    listString += str(num) + " "
print listString
