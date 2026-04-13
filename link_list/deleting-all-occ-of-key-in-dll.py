class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def deleteAllOccurOfX(head, x):
    pivot = Node(-1)
    pivot.next = head
    l = head
    while l:
        # print(l.data)
        if l.data!=x:
            pivot = pivot.next
            pivot.data = l.data
            print(pivot.data)
        l = l.next
    pivot.next = None
    return head
head = Node(2)
two = Node(2)
three = Node(10)
four = Node(8)
five = Node(4)
six = Node(2)
seven = Node(5)
eight = Node(2)
head.next = two
two.prev = head
two.next = three
three.prev = two
three.next= four
four.prev = three
four.next = five
five.prev = four
five.next = six
six.prev = five
six.next = seven
seven.prev = six
seven.next = eight
eight.prev = seven
deleteAllOccurOfX(head,2)
while head:
    print(head.data)
    head = head.next
    
