class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

def mergeTwoLists(list1, list2):
    head1 = list1
    head2 = list2
    dummy_Node = Node(-1)
    temp = dummy_Node
    
    while head1 and head2:
        if head1.data <= head2.data:
            temp.next = head1
            head1 = head1.next
            
        else:
            temp.next = head2
            head2 = head2.next
            
        temp = temp.next
    if head1:
        temp.next = head1
        temp = temp.next
        
    
    if head2:
        temp.next = head2
        temp = temp.next
    
    return dummy_Node.next

def printLL(head):
    temp = head
    while temp:
        print(temp.data, end = " ")
        temp = temp.next
        
    print()


list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)

printLL(list1)
printLL(list2)

x = mergeTwoLists(list1, list2)
# print(x)
printLL(x)
        
        
            
    
    
    