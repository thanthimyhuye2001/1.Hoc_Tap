# Thân Thị Mỹ Huyền - 20206288
# Cài đặt giải thuật Sắp Xếp MergeSort

def mergeSort(arr):
	if len(arr) > 1:

		# phần tử giữa dãy
		mid = len(arr)//2

		# Chia đôi dãy đã cho: bên trái (Left) và bên phải (Right)
		L = arr[:mid]
		R = arr[mid:]

		# Sắp xếp bên trái
		mergeSort(L)
		# sắp xếp bên phải
		mergeSort(R)

		i = j = k = 0

		# So sánh các phần tử 2 dãy L[] với R[], nếu nhỏ hơn thì xếp vào dãy ban đầu
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Kiểm tra những phần tử còn lại
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

# Hàm in ra dãy, bỏ được dấu [] và dấu phẩy
def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()

# Input dãy và Output dãy đã xếp
arr = [12, 11, 13, 5, 6, 7]
print('Dãy cần xếp ', end="\n")
printList(arr)
mergeSort(arr)
print('Dãy sau khi sắp xếp ', end="\n")
printList(arr)