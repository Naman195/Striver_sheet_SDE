class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def reversed_Linked_list(head):
    prev = None
    curr = head
    
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    
    head = prev
    return head

def print_Linked_list(head):
    temp = head
    while temp:
        print(temp.data, end = " --> ")
        temp = temp.next
    print()
    

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

x = reversed_Linked_list(head)
print_Linked_list(x)
