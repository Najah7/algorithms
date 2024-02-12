from linkedList import LinkedList, Node


def intersection(ll1, ll2):  # O(n + diff)
    if ll1.tail is not ll2.tail:
        return False

    len1 = len(ll1)
    len2 = len(ll2)

    shorter = ll1 if len1 < len2 else ll2
    longer = ll2 if len1 < len2 else ll1

    diff = len(longer) - len(shorter)

    longer_node = longer.head
    shorter_node = shorter.head

    for _ in range(diff):  # O(diff)
        longer_node = longer_node.next

    while shorter_node is not longer_node:  # O(n)
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


def add_some_nodes(ll1, ll2, value):
    new_node = Node(value)
    lls = [ll1, ll2]
    for ll in lls:
        ll.tail.next = new_node
        ll.tail = new_node
        ll.length += 1


llA = LinkedList()
llB = LinkedList()
valuesA = [3, 1, 5, 9, 7, 2, 1]
valuesB = [4, 6]
for value in valuesA:
    llA.append(value)
for value in valuesB:
    llB.append(value)

add_some_nodes(llA, llB, 7)
add_some_nodes(llA, llB, 2)

print(llA)
print(llB)

print(intersection(llA, llB))
