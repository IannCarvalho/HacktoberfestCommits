array = [9, 14, 3, 2, 43, 11, 58, 22]
print("Before Sort")
listString = ""
for num in array:
    listString += str(num) + " "
print listString

leftIndex = 0
rightIndex = len(array)-1

if (len(array) > 0 and leftIndex >= 0 and rightIndex < len(array) and leftIndex < rightIndex):

    biggest = array[leftIndex]

    for i in range(leftIndex, rightIndex+1):
        if (array[i] > biggest):
            biggest = array[i]

    count = [0] * (biggest + 1)

    for i in range(leftIndex, rightIndex+1):
        count[array[i]] = count[array[i]] + 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    answer = [0] * len(array)

    for i in range(leftIndex, rightIndex+1):
        answer[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1

    for i in range(leftIndex, rightIndex+1):
        array[i] = answer[i]

print("After Sort")
listString = ""
for num in array:
    listString += str(num) + " "
print listString
