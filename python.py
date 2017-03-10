import sys

def kth_node(head, k):
    arr = []

    while head is not None:
        if len(arr) == 0 or arr[-1] < head.data:
            arr.append(head.data)

        elif arr[-1] > head.data:
            arr = quickSort(arr, head.data)

        head = head.next

    if k >= len(arr):
        'index out of bounds error'
        return 0

    return arr[-k]

def quickSort(arr, data):
    for i in range(len(arr)):
        if data <= arr[i]:
            pivot = i
            arr1 = arr[:pivot]
            arr2 = arr[pivot:]
            arr1.append(data)
            arr = arr1 + arr2
            break

    return arr

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

linked_list = Node(5)
linked_list.next = Node(2)
linked_list.next.next = Node(8)
linked_list.next.next.next = Node(27)
linked_list.next.next.next.next = Node(62)
linked_list.next.next.next.next.next = Node(34)
linked_list.next.next.next.next.next.next = Node(12)
linked_list.next.next.next.next.next.next.next = Node(24)
linked_list.next.next.next.next.next.next.next.next = Node(2)

print kth_node(linked_list, 2)

