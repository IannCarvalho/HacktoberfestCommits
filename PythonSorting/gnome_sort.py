array = [9, 14, 3, 2, 43, 11, 58, 22]
print("Before Sort")
listString = ""
for num in array:
    listString += str(num) + " "
print listString

leftIndex = 0
rightIndex = len(array)-1

if (len(array) > 0 and leftIndex >= 0 and rightIndex < len(array) and leftIndex < rightIndex):
    pivot = leftIndex + 1
    while (pivot <= rightIndex):
        if (pivot == leftIndex or array[pivot] >= (array[pivot - 1])):
            pivot += 1
        else:
            array[pivot], array[pivot - 1] = array[pivot - 1], array[pivot]
            pivot -= 1

print("After Sort")
listString = ""
for num in array:
    listString += str(num) + " "
print listString
