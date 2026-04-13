class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def findPairsWithGivenSum(target,head):
    
    return head


head = Node(1)
two = Node(2)
three = Node(4)
four = Node(5)
five = Node(6)
six = Node(8)
seven = Node(9)
head.next = two
two.prev = head
two.next = three
three.prev = two
three.next = four
four.prev = three
four.next = five
five.prev = four
five.next = six
six.prev = five
six.next = seven
seven.prev = six
print(findPairsWithGivenSum(7,head))

