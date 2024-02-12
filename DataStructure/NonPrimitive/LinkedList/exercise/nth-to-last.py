from linkedList import LinkedList


def nth_to_last(linked_list, n):
    if not (0 <= n < linked_list.length):
        raise IndexError("Index out of range")

    prev_node = linked_list.head
    current_node = linked_list.head
    for _ in range(n - 1):
        current_node = current_node.next
    while current_node.next is not None:
        prev_node = prev_node.next
        current_node = current_node.next

    return prev_node


ll = LinkedList()
values = range(1, 11)
for value in values:
    ll.append(value)
print(ll)
print(nth_to_last(ll, 3))
