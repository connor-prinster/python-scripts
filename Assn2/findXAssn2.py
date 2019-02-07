arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 10]

value = 11

while arr1 and arr2:
	if arr1[0] + arr2[-1] == value:
		print("found value", value, ". First value:", arr1[0], " Second value:", arr2[-1])
		quit()
	elif arr1[0] + arr2[-1] > value:
		del arr2[-1]
	elif arr1[0] + arr2[-1] < value:
		del arr1[-1] 
print("not there")
quit()
		