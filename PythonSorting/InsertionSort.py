array = [9, 14, 3, 2, 43, 11, 58, 22]
print("Before Sort")
listString = ""
for num in array:
    listString += str(num) + " "
print listString

leftIndex = 0
rightIndex = len(array)-1

if (array != None and leftIndex < rightIndex and leftIndex >= 0 and rightIndex >= 0 and len(array) > 0 and len(array) >= rightIndex):
	for i in range(leftIndex + 1, rightIndex):
		k = i
		while (k > 0 and array[k - 1] > (array[k])):
			array[k - 1], array[k] = array[k], array[k - 1]
			k -= 1

print("After Sort")
listString = ""
for num in array:
    listString += str(num) + " "
print listString
