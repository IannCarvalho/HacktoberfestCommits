array = [9, 14, 3, 2, 43, 11, 58, 22]
print("Before Sort")
listString = ""
for num in array:
    listString += str(num) + " "
print listString

leftIndex = 0
rightIndex = len(array)-1

if array != None and leftIndex < rightIndex and leftIndex >= 0 and rightIndex >= 0 and len(array) > 0 and len(array) >= rightIndex:
    for i in range(leftIndex, rightIndex):
		indiceDoMenor = i
		for j in range(i+1, rightIndex+1):
			if array[j] < array[indiceDoMenor]:
				indiceDoMenor = j
		array[i], array[indiceDoMenor] = array[indiceDoMenor], array[i]

print("After Sort")
listString = ""
for num in array:
    listString += str(num) + " "
print listString
