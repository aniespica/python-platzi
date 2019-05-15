import random
import timeit


def costly_func():
   return map(lambda x: x^2, range(10))
 

def binary_search(data, target, low, high):
	if low > high:
		return False
	
	mid = (low + high) // 2
	
	if target == data[mid]:
		return True
	elif target < data[mid]:
		return binary_search(data,target, low, mid - 1)
	else:
		return binary_search(data,target, mid + 1, high)


def binary_search_while(data, target, low, high):

	while low <= high:
		mid = (low + high) // 2
		
		if target == data[mid]:
			return True
		elif target < data[mid]:
			high = mid - 1
		else:
			low = mid + 1
	
	return False	


if __name__ == '__main__':
	data = [random.randint(0,100) for i in range(10)]
	
	data.sort()
	
	print(data)
	
	target = int(input('What number would you like to find? '))
	
	found = binary_search(data, target, 0, len(data) - 1)
	found2 = binary_search_while(data,target, 0, len(data) - 1)
	timeit.timeit(costly_func)
	print(found)
	print(found2)
