# Thân Thị Mỹ Huyền - 20206288
# Thuật toán trên cấu trúc dữ liệu danh sách
# Thêm một phần tử trong danh sách


# Node class
class Node:

	# Hàm khởi tạo đối tượng nút
	def __init__(self, data):
		self.data = data # Gán dữ liệu
		self.next = None # Khởi tạo tiếp theo là NULL


# Lớp Danh sách Liên kết chứa một đối tượng nút
class LinkedList:

	# Hàm khởi tạo head
	def __init__(self):
		self.head = None


	# Hàm thêm một nút mới vào đầu danh sách
	def AddHead(self, new_data):

		# Phân bổ nút
		# Thêm dữ liệu vào
		new_node = Node(new_data)

		# Thực hiện tiếp theo của nút mới là head
		new_node.next = self.head
  
		# Di chuyển head để trỏ đến nút mới
		self.head = new_node 


	# Hàm này nằm trong lớp Linked List
	# Chèn 1 nút mới sau nút đã chọn
	def insertAfter(self, prev_node, new_data):

		# Kiểm tra "nút đã chọn" có tồn tại hay không
		if prev_node is None:
			print("Nút đã chọn phải nằm trong Linked List !!!")
			return

		# Tạo nút mới
		# Thêm dữ liệu vào
		new_node = Node(new_data)

		# 4. Tạo phần tiếp theo của Nút mới như phần tiếp theo của "Nút đã chọn"
		new_node.next = prev_node.next

		# Trỏ next của "Nút đã chọn" trỏ tới Nút mới
		prev_node.next = new_node


	# Hàm này nằm trong lớp Linked List
	# Thêm một nút mới vào cuối
	def AddTail(self, new_data):

		# Tạo 1 nút mới
		# Thêm vào dữ liệu
		# Node cuối là node có next = NULL
		new_node = Node(new_data)

		# Nếu Linked List rỗng, thì Nút mới là head
		if self.head is None:
			self.head = new_node
			return

		# Duyệt danh sách liên kết đến Nút cuối cùng 
		last = self.head
		while (last.next):
			last = last.next

		# 6. Trỏ next của Nút cuối tới Nút mới
		last.next = new_node


	# Hàm để in linked list
	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data,end=" ")
			temp = temp.next


# ---------------------------------------------------------------------
# Chương trình chính
if __name__=='__main__':

	# Bắt đầu với danh sách rỗng
	llist = LinkedList()
 
	# Chèn (6) => Linked List trở thành 6 -> NULL
	llist.AddTail(6)

	# Thêm (7) vào đầu danh sách => Linked List trở thành 7->6->NULL
	llist.AddHead(7)

	# Thêm (1) vào đầu danh sách => Linked List trở thành 1->7->6->NULL
	llist.AddHead(1)

	# Thêm (4) vào cuối danh sách => Linked List trở thành 1->7->6->4->None
	llist.AddTail(4)

	# Thêm (8) đằng sau vị trí (7) => Linked List trở thành 1->7->8->6->4->None
	llist.insertAfter(llist.head.next, 8)
      
    # Thêm (5) đằng sau vị trí (6) => Linked List trở thành 1->7->8->6->5->4->None
	llist.insertAfter(llist.head.next.next.next, 5)
    
    
	print('Danh sách Linked List : ')
	llist.printList()
