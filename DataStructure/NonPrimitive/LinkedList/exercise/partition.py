from linkedList import LinkedList


def partition(ll, x):
    """Partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x."""
    current = ll.head
    ll.tail = ll.head
    while current is not None:
        next_node = current.next
        if current.value < x:  # prepend
            current.next = ll.head
            ll.head = current
        else:  # append
            ll.tail.next = current
            ll.tail = current
        current = next_node

    if ll.tail.next is not None:
        ll.tail.next = None


PARTITION_X = 5

ll = LinkedList()
values = [3, 5, 8, 5, 10, 1, 2]
for value in values:
    ll.append(value)

print(f"before: {ll}")
partition(ll, PARTITION_X)
print(f"after: {ll}")
