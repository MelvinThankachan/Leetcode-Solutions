class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list_from_array(arr):
    """Create a linked list from a given array."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def print_list(head):
    """Print all values in the linked list."""
    list_array = []
    current = head
    while current:
        list_array.append(current.val)
        current = current.next
    print(list_array)


def insert_node(head, val):
    """Insert a new node with value `val` at the end of the list."""
    if not head:
        return ListNode(val)
    current = head
    while current.next:
        current = current.next
    current.next = ListNode(val)
    return head


def delete_node(head, val):
    """Delete the first occurrence of a node with value `val`."""
    if not head:
        return None
    if head.val == val:
        return head.next
    current = head
    while current.next and current.next.val != val:
        current = current.next
    if current.next:
        current.next = current.next.next
    return head


def search_list(head, val):
    """Search for a value in the list and return True if found, otherwise False."""
    current = head
    while current:
        if current.val == val:
            return True
        current = current.next
    return False


def reverse_list(head):
    """Reverse the linked list."""
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def length_of_list(head):
    """Find the length of the linked list."""
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length


def is_list_equal(head, lst):
    """Check if the linked list matches the given list of values."""
    current = head
    for value in lst:
        if not current:
            return False  # List is shorter than the given list
        if current.val != value:
            return False  # Mismatch found
        current = current.next
    return current is None  # True if no extra nodes in the list
