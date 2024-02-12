from linkedList import LinkedList


def remove_duplicates(linked_list):
    current_node = linked_list.head
    while current_node is not None:
        next_node = current_node.next
        while next_node is not None:
            if current_node.value == next_node.value:
                current_node.next = next_node.next
                linked_list.length -= 1
            next_node = next_node.next
        current_node = current_node.next


linked_list = LinkedList()
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for value in values:
    linked_list.append(value)
print(linked_list)

remove_duplicates(linked_list)
print(linked_list)
