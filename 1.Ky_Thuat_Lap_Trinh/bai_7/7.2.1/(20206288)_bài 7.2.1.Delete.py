# Thân Thị Mỹ Huyền - 20206288
# Thuật toán trên cấu trúc dữ liệu danh sách
# Xóa một phần tử trong danh sách

# Node class
class Node:

	# Hàm khởi tạo đối tượng nút
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	# Hàm khởi tạo head
	def __init__(self):
		self.head = None

	# Hàm thêm một nút mới vào đầu danh sách
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node


	# Hàm xóa 1 phần tử "key" trong Linked List
	def deleteNode(self, key):
		
		# Store head node
		temp = self.head

		# Xóa đầu
		if (temp is not None):
			if (temp.data == key):
				self.head = temp.next
				temp = None
				return
        
        # Xóa ở vị trí bất kỳ
		while(temp is not None):
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

		# Nếu giá trị "key" không tồn tại trong Linked List
		if(temp == None):
			return

		# Bỏ liên kết nút khỏi danh sách được liên kết
		prev.next = temp.next

		temp = None


	# Hàm để in linked list
	def printList(self):
		temp = self.head
		while(temp):
			print (" %d" %(temp.data))
			temp = temp.next
        


# ------------------------------------------------------------------------------------
# Chương trình chính
# Khởi tạo danh sách liên kết
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

print ("Danh sách đã tạo: ")
llist.printList()

n = float(input('Nhập phần tử cần xóa trong danh sách: '))

llist.deleteNode(n)
print (f"\nDanh sách sau khi xóa phần tử {n}:")
llist.printList()
