array = [9, 14, 3, 2, 43, 11, 58, 22]
print("Before Sort")
listString = ""
for num in array:
    listString += str(num) + " "
print listString

leftIndex = 0
rightIndex = len(array)-1

if array != None and leftIndex < rightIndex and leftIndex >= 0 and rightIndex >= 0 and len(array) > 0 and len(array) >= rightIndex:
    i = leftIndex
    while (i < rightIndex):
        swap = False
        for y in range(leftIndex, rightIndex - i):
            if (array[y] > (array[y + 1])):
                array[y], array[y + 1] = array[y + 1], array[y]
                swap = True
        if (not swap):
            break
        i += 1

print("After Sort")
listString = ""
for num in array:
    listString += str(num) + " "
print listString