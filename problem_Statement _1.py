Write a code that prints out the first occurrence of a duplicate in a given array of integers
Sample Input: [1,2,3,2,1]
Output: 2

def countOccurrences(arr, n, x):
	res = 0
	for i in range(n):
		if x == arr[i]:
			res += 1
	return res

arr = [1, 2, 3,2,1]
n = len(arr)
x = 1
print (countOccurrences(arr, n, x))




