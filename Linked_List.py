class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
 
head = node1
# Memory allocation (linking nodes)
node1.next = node2
node2.next = node3
node3.next = node4

def deleting_at_end(head):

    if head is None:
        return None
    if head.next is None:
        return None
    current=head
    while current.next.next is not None:
        current = current.next

    current.next = None
    return head

def delete_at_begining(head):

    if head is not None:
        head = head.next
    return head   

def insert_at_begining(head,cls,data):

    new_node = cls(data)
    new_node.next=head
    head = new_node  #this is for moving head to the beginning position
    return head

def insert_at_end(head,cls,data):

    new_node=cls(data)

    if head is None:
        head = new_node
    
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return head
    
def deletion_at_specific_position(head,data):

    if head is None:
        return None
    if head.data == data:
        return head.next

    current = head
    while current.next.data != data:
        current = current.next
    
    current.next = current.next.next
    return head

def insertion_specific_position(head,cls,data,prev_data):
    new_node = cls(data)
    current = head

    if current is None:
        return None 
    if current.data == prev_data:
        new_node.next = head
        head = new_node

    while current is not None and current.next.data != prev_data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head

# Insert a new node with data 15 before the node with data 20

head = insertion_specific_position(head, Node, 15, 20)
current=head
head = deleting_at_end(head)
current=head
while current is not None:
    print(current.data,end='->')
    current=current.next
print('None')

    

 





