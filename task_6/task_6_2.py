"""
Create CustomList – the linked list of values of random type, which size changes dynamically and has an ability to index
elements.

The task requires implementation of the following functionality:
• Create the empty user list and the one based on enumeration of values separated by commas. The elements are stored
in form of unidirectional linked list. Nodes of this list must be implemented in class Item.
    Method name: __init__(self, *data) -> None;
• Add and remove elements.
    Method names: append(self, value) -> None - to add to the end,
                add_start(self, value) -> None - to add to the start,
                remove(self, value) -> None - to remove the first occurrence of given value;
• Operations with elements by index. Negative indexing is not necessary.
    Method names: __getitem__(self, index) -> Any,
                __setitem__(self, index, data) -> None,
                __delitem__(self, index) -> None;
• Receive index of predetermined value.
    Method name: find(self, value) -> Any;
• Clear the list.
    Method name: clear(self) -> None;
• Receive lists length.
    Method name: __len__(self) -> int;
• Make CustomList iterable to use in for-loops;
    Method name: __iter__(self);
• Raise exceptions when:
    find() or remove() don't find specific value
    index out of bound at methods getitem, setitem, delitem.


Notes:
    The class CustomList must not inherit from anything (except from the object, of course).
    Function names should be as described above. Additional functionality has no naming requirements.
    Indexation starts with 0.
    List length changes while adding and removing elements.
    Inside the list the elements are connected as in a linked list, starting with link to head.
"""


# raise IndexError
# raise ValueError


class Item:
    """
    A node in a unidirectional linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class CustomList:
    """
    An unidirectional linked list.
    """
    def __init__(self, *data) -> None:
        """
        Constructor for the CustomList class.
        """
        self.head = None
        self.length = 0
        if data:
            for node in data:
                self.append(node)

    def __iter__(self):
        """
        Iterator function for a CustomList class.
        """
        current = self.head
        while current:
            yield current.data
            current = current.next
        # raise StopIteration

    def __len__(self):
        """
        Return size of a CustomList class custom list.
        :return: The length of a custom list.
        :rtype: int
        """
        return self.length

    def __getitem__(self, index):
        """
        Function to return a value of an item at certain index.
        :param index: Index of the element to look for.
        :type index: int
        :return: Element at the certain index.
        :rtype: Any
        """
        if index >= self.length:
            raise IndexError("Index out of range.")
        else:
            current_index, current = 0, self.head
            while current_index < index:
                current_index += 1
                current = current.next
            return current.data

    def __setitem__(self, index, data) -> None:
        """
        Function to change item at a certain position in a custom list.
        :param index: Index of the element to change.
        :type index: int
        :param data: The data to write to an index.
        :type data: Any
        """
        if index >= self.length:
            raise IndexError("Index out of range.")
        else:
            current_index, current = 0, self.head
            while current_index < index:
                current_index += 1
                current = current.next
            current.data = data

    def __delitem__(self, index) -> None:
        """
        Function to delete an item at a certain position in a custom list.
        :param index: Index of an item that need to be deleted from a custom list.
        :type index: int
        """
        if index >= self.length:
            raise IndexError("Index out of range.")
        elif index == 0:
            current = self.head
            self.head = current.next
            current = None
            self.length -= 1
        else:
            current, previous, current_index = self.head, None, 0
            while current_index < index:
                current_index += 1
                previous = current
                current = current.next
            self.length -= 1
            previous.next = current.next
            current = None

    def find(self, value):
        """
        Function to find index of an element in a custom list.
        :param value: The item to look for inside custom list.
        :type value: Any
        :return: Index of an element.
        :rtype: int
        """
        current, current_position = self.head, 0
        while current and current.data != value:
            current = current.next
            current_position += 1
        if current is None:
            raise ValueError('Element not in the list.')
        else:
            return current_position

    def remove(self, value) -> None:
        """
        Function to remove first occurrence of the item inside custom list.
        :param value: Item which first occurrence in the custom list will be deleted.
        :type value: Any
        """
        current = self.head
        if current and current.data == value:
            self.head = current.next
            current = None
            self.length -= 1
        else:
            previous = None
            while current and current.data != value:
                previous = current
                current = current.next
            if current is None:
                raise ValueError('Element not in the list.')
            else:
                self.length -= 1
                previous.next = current.next
                current = None

    def append(self, value) -> None:
        """
        Add an item to the end of the custom list.
        :param value: Item to add to the end of the custom list.
        :type value: Any
        """
        self.length += 1
        new_node = Item(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def add_start(self, value) -> None:
        """
        Add an item to the beginning of the custom list.
        :param value: Item to add to the beginning of the custom list.
        :type value: Any

        """
        self.length += 1
        new_node = Item(value)
        new_node.next = self.head
        self.head = new_node

    def clear(self):
        """
        Clear custom list.
        """
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


# udlist = CustomList('one', 'two')
# udlist.add_start('zero')
# udlist.append('three')
# udlist.append('four')
# udlist.add_start('minus one')
# udlist.add_start('minus two')
# udlist.remove('three')
#
#
# udlist.print_list()
#
#
# udlist.__setitem__(4, 'test')
# udlist.__delitem__(0)
# for i, item in enumerate(udlist):
#     print(f"{i} is the {item}")
#
# print(f"Length if unidirectional list = {udlist.__len__()}")
# print(f"{udlist.__getitem__(4)}")
# print(udlist.find('test'))
