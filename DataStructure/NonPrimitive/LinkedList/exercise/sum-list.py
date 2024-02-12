from linkedList import LinkedList


def sum_list(ll1, ll2):
    current_node1 = ll1.head
    current_node2 = ll2.head
    carry = 0

    ll = LinkedList()
    while current_node1 is not None or current_node2 is not None:
        if current_node1 is not None:
            value1 = current_node1.value
            current_node1 = current_node1.next
        else:
            value1 = 0
        if current_node2 is not None:
            value2 = current_node2.value
            current_node2 = current_node2.next
        else:
            value2 = 0
        sum = value1 + value2 + carry
        carry = sum // 10
        ll.append(sum % 10)
    return ll


ll1 = LinkedList()
ll2 = LinkedList()
values1 = [7, 1, 6]
values2 = [5, 9, 2]
for v1, v2 in zip(values1, values2):
    ll1.append(v1)
    ll2.append(v2)

print(ll1)
print(ll2)
new_ll = sum_list(ll1, ll2)
print(new_ll)
