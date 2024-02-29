class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def push(self, data):
        self.append(data)   

# Test Linked List
if __name__ == "__main__":
    # yaratish Linked List
    linked_list = LinkedList()

    # Inserting elements
    for i in range(1, 6):
        linked_list.insert(i)

    print("After inserting elements at the beginning:")
    linked_list.print_list()

    # Appending elements
    for i in range(6, 11):
        linked_list.append(i)

    print("\nAfter appending elements at the end:")
    linked_list.print_list()

    # elementlarni push qilish
    for i in range(11, 16):
        linked_list.push(i)

    print("\nAfter pushing elements at the end:")
    linked_list.print_list()
