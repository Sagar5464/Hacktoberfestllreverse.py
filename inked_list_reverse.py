class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def reverse(self):
        prev = None
        curr = self.head
        # ✅ Correct: store next before breaking link
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

ll = LinkedList()
for i in [1, 2, 3, 4, 5]:
    ll.append(i)

ll.reverse()
ll.print_list()  # ✅ Output: 5 4 3 2 1
