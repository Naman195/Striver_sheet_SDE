class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

def removeNthNode(head, n):
    dummy = Node(-1)
    dummy.next = head
    slow = dummy
    fast = dummy
    
    for i in range(1, n+1):
        fast = fast.next
    
    while fast.next:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next
    return dummy.next


def printLL(head):
    temp = head
    while temp:
        print(temp.data, end = " ")
        temp = temp.next
    print()


arr = [1, 2, 3, 4, 5]
N = 3
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])
head.next.next.next.next = Node(arr[4])

x = removeNthNode(head, N)
printLL(x)
        
    
    