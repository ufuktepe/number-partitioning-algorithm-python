class MaxHeap:
    def __init__(self, items):
        """
        Initialize the heap.
        :param items: elements of the heap
        """
        self.items = items
        self.n = len(items)

        # Build the heap
        self.build_max_heap()


    def build_max_heap(self):
        """
        Builds a max-heap. Takes O(nlog(n)) time since max_heapify takes O(log(n)) time.
        :return: None
        """

        # # Get the number of items
        # n = len(self.items)

        # Build the heap in bottom-up manner
        for i in range(self.n // 2, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        """
        Floats down the value at index i to its correct position so that the subtree rooted at index i obeys the
        max heap property. Takes O(log(n)) time.
        :param i: index of the item to be positioned
        :return: None
        """

        # Get the indices of the left and right children
        left = 2 * i + 1
        right = 2 * i + 2

        # heap_size = len(self.items)

        # Compare the left child to the current item and get the index of the minimum item
        if self.n > left and self.items[left] > self.items[i]:
            max_idx = left
        else:
            max_idx = i

        # Update the index for the maximum item if the right child is the maximum item
        if self.n > right and self.items[right] > self.items[max_idx]:
            max_idx = right

        # If the current item is not the maximum one, swap it with the maximum item and call max_heapify again
        if max_idx != i:
            self.items[i], self.items[max_idx] = self.items[max_idx], self.items[i]

            self.max_heapify(max_idx)


    def extract_max(self):
        """
        Removes and returns the maximum item.
        :return: largest value item
        """

        # Raise an IndexError if there are no items in the heap.
        if self.n < 1:
            raise IndexError()

        # Get the maximum item
        max_item = self.items[0]

        # Replace the maximum item with the last item
        self.items[0] = self.items[-1]

        # Remove the last item
        del self.items[-1]
        self.n -= 1

        if self.n > 0:
            # Max heapify for the first item
            self.max_heapify(0)

        return max_item

    def heap_increase_key(self, i, key):
        """
        Sets the value of the item at index i to key and calls restore_max_heap_property to find the correct position
        for it.
        :param i: index of the item whose value will be updated
        :param key: new value for item at index i
        :return: None
        """

        # Raise a ValueError if the new value is smaller than the current value
        if key < self.items[i]:
            raise ValueError

        # Update the value of the item at index i to its new value
        self.items[i] = key

        # Restore the max-heap property
        self.restore_max_heap_property(i)

    def restore_max_heap_property(self, i):
        """
        Finds the correct position for the item at index i by traversing the tree from i to the root.
        :param i: index of the child node
        :return: None
        """

        # Return if the item is the root
        if i == 0:
            return

        parent = (i - 1) // 2

        # Check if the parent is smaller than the child
        if self.items[parent] < self.items[i]:

            # Swap the parent with the child
            self.items[i], self.items[parent] = self.items[parent], self.items[i]

            # Recursively move up the tree
            self.restore_max_heap_property(parent)

    def insert(self, key):
        self.items.append(key)
        self.n += 1

        i = self.n - 1

        # Restore the max-heap property
        self.restore_max_heap_property(i)
