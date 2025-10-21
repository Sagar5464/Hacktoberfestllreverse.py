class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
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
        # ❌ Bug: forgot to move 'curr' to 'next' before updating link
        while curr:
            curr.next = prev
            prev = curr
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
ll.print_list()  # Expected: 5 4 3 2 1
