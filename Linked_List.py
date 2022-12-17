class Linked_List:
    class __Node:
        __slots__ = "val", "nxt", "prev" #Taken from the book to streamline memory

        def __init__(self, val):
            # declare and initialize the public attributes
            # for objects of the Node class.
            # TODO replace pass with your implementation
            self.val = val
            #print("This is my value " + str(val))
            self.nxt = None
            self.prev = None

    __slots__ = "__header", "__trailer", "__length", "__iternode"
    def __init__(self):
        # declare and initialize the private attributes
        # for objects of the sentineled Linked_List class
        # TODO replace pass with your implementation
        self.__length = 0
        self.__header = self.__Node(None)
        self.__trailer = self.__Node(None)
        self.__header.nxt = self.__trailer
        self.__trailer.prev = self.__header


    def __len__(self):
        # return the number of value-containing nodes in
        # this list.
        # TODO replace pass with your implementation
        return self.__length


    def append_element(self, val):
        # increase the size of the list by one, and add a
        # node containing val at the new tail position. this
        # is the only way to add items at the tail position.
        # TODO replace pass with your implementation
        newest = self.__Node(val) #Initialize the node to be added
        newest.nxt = self.__trailer #Set the next of newest to the trailer
        newest.prev = self.__trailer.prev #Set the prev of newest to the previous last node
        self.__trailer.prev.nxt = newest #set the next of the previous last node to the newest
        self.__trailer.prev = newest
        self.__length = self.__length + 1

    def insert_element_at(self, val, index):
        #TODO Efficiency gain: go from the tail if index > length / 2.
        # assuming the head position (not the header node)
        # is indexed 0, add a node containing val at the
        # specified index. If the index is not a valid
        # position within the list, raise an IndexError
        # exception. This method cannot be used to add an
        # item at the tail position.
        if index < 0 or index >= self.__length:
            raise IndexError("Sorry, your proposed index is out of bounds.")
        newest = self.__Node(val)
        if index < self.__length / 2:
            cur = self.__header
            counter = 0
            while counter < index:
                counter = counter + 1
                cur = cur.nxt
        #Cur is the node that needs to be before newest
        else:
            cur = self.__trailer.prev.prev
            counter = self.__length - 1
            while counter > index:
                counter = counter - 1
                cur = cur.prev
        newest.prev = cur
        newest.nxt = cur.nxt
        cur.nxt.prev = newest
        cur.nxt = newest
        self.__length = self.__length + 1

    def remove_element_at(self, index):
        # assuming the head position (not the header node)
        # is indexed 0, remove and return the value stored
        # in the node at the specified index. If the index
        # is invalid, raise an IndexError exception.
        if index < 0 or index >= self.__length:
            raise IndexError("Sorry, your proposed index is out of bounds.")
        if index < self.__length / 2:
            cur = self.__header
            counter = -1
            while counter < index:
                cur = cur.nxt
                counter = counter + 1
        else:
            cur = self.__trailer
            counter = self.__length
            while counter > index:
                cur = cur.prev
                counter = counter - 1
        result = cur.val #Storing the value to be returned
        cur.nxt.prev = cur.prev #Removing cur from the list
        cur.prev.nxt = cur.nxt
        self.__length = self.__length - 1
        return result

    def get_element_at(self, index):
        if index < 0 or index >= self.__length:
            raise IndexError("Sorry, your proposed index is out of bounds.")
        if index < self.__length / 2:
            cur = self.__header
            counter = -1
            while counter < index:
                cur = cur.nxt
                counter = counter + 1
        else:
            cur = self.__trailer
            counter = self.__length
            while counter > index:
                cur = cur.prev
                counter = counter - 1
        result = cur.val  # Storing the value to be returned
        return result

    def rotate_left(self):
        # rotate the list left one position. Conceptual indices
        # should all decrease by one, except for the head, which
        # should become the tail. For example, if the list is
        # [ 5, 7, 9, -4 ], this method should alter it to
        # [ 7, 9, -4, 5 ]. This method should modify the list in
        # place and must not return a value.
        # TODO replace pass with your implementation.
        cur = self.__header.nxt
        if self.__length > 1:
            self.__header.nxt = cur.nxt
            self.__header.nxt.prev = self.__header
            cur.prev = self.__trailer.prev
            cur.nxt = self.__trailer
            self.__trailer.prev.nxt = cur
            self.__trailer.prev = cur

    def __str__(self):
        # return a string representation of the list's
        # contents. An empty list should appear as [ ].
        # A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ].
        # You may assume that the values stored inside of the
        # node objects implement the __str__() method, so you
        # call str(val_object) on them to aquire their string
        # representations.
        # TODO replace pass with your implementation
        #Do this with a list instead of a string to make it linear?
        #TODO Unmake it linear because str(list) causes issues with the grader
        cur = self.__header.nxt
        if self.__length == 0:
            return "[ ]"
        elif self.__length == 1:
            return "[ " + str(cur.val) + " ]"
        else:
            result = "[ "
            while cur is not self.__trailer:
                elem = str(cur.val)
                result = result + elem + ", "
                cur = cur.nxt
            result = result[:len(result) - 2] + " ]"
            return result
            # temp_arr = [None] * self.__length
            # i = 0
            # while cur is not self.__trailer:
            #     elem = cur.val
            #     temp_arr[i] = elem
            #     cur = cur.nxt
            #     i = i + 1
            # return "[ " + str(temp_arr)[1:len(str(temp_arr)) - 1] + " ]"

    #__iternode = None
    #__iternode = None
    def __iter__(self):
        # initialize a new attribute for walking through your list
        # TODO insert your initialization code before the return
        # statement. do not modify the return statement.
        self.__iternode = self.__header.nxt
        return self

    def __next__(self):
        if self.__iternode is self.__trailer:
            raise StopIteration
        to_return = self.__iternode.val
        self.__iternode = self.__iternode.nxt
        return to_return

        # using the attribute that you initialized in __iter__(),
        # fetch the next value and return it. If there are no more
        # values to fetch, raise a StopIteration exception.
        # TODO replace pass with your implementation
        pass


if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases
    # when the list is empty, when it has one element, and when
    # it has several elements. Do the indexed methods raise exceptions
    # when given invalid indices? Do they position items
    # correctly when given valid indices? Does the string
    # representation of your list conform to the specified format?
    # Does removing an element function correctly regardless of that
    # element's location? Does a for loop iterate through your list
    # from head to tail? Your writeup should explain why you chose the
    # test cases. Leave all test cases in your code when submitting.

    l = Linked_List()
    #Testing the __str__() and len methods first because it helps test the other methods
    print(l.__str__())
    print(l.__len__())
    print(len(l))
    #Also showing append method works on an empty list
    l.append_element("1 Element List")
    print(l.__str__())
    print(l.__len__())
    #...And a list with one element
    l.append_element("2 element list")
    print(l.__str__())
    print(l.__len__())
    print(len(l))
    l.append_element("3 element list")
    print(l.__str__())
    print(l.__len__())
    #Testing the append method
    l = Linked_List()
    for i in range(11):
        l.append_element(i)
    print(l.__len__())
    print(l.__str__())
    #Insertion at position 0
    l.insert_element_at(55, 0)
    print(l.__str__())
    #Making sure insertion correctly modifies len
    print(l.__len__())
    print(len(l))
    #Insertion in the second half of the list
    l.insert_element_at(99, 11)
    print(l.__str__())
    print(l.__len__())
    #Insertion in the first half of the list
    l.insert_element_at(99, 3)
    print(l.__str__())
    print(l.__len__())
    l = Linked_List()
    try:
        l.insert_element_at(55, -1) #Gives error as it should
    except IndexError:
        print("insert_element_at correctly gives an index error when out of bounds")
    try:
        l.insert_element_at(55, 0) #Gives error as it should
    except IndexError:
        print("insert_element_at correctly gives an index error when appending an element with it")
    #Making sure you can add at the head as long as there is another node
    print(l.__len__())
    print(l.__str__())
    l.append_element(0)
    l.insert_element_at(55, 0)
    print(l.__str__())
    #Verifying remove_element_at works on the first half of a list with more then one node
    print(l.remove_element_at(0))
    print(l.__len__())
    print(l.__str__())
    #Verifying it works on a list of size 1
    print(l.remove_element_at(0))
    print(l.__str__())
    l.append_element(0)
    l.append_element(1)
    #Verifying it works on the second half of a list with more then one node
    print(l.__str__())
    print(l.__len__())
    print(l.remove_element_at(1))
    print(l.__str__())
    print(l.__len__())
    try:
        l.remove_element_at(3) #Gives error as it should
    except IndexError:
        print("remove_element_at correctly gives an index error when out of bounds")
    try:
        l.remove_element_at(1) #Gives error as it should
    except IndexError:
        print("remove_element_at correctly gives an index error when out of bounds")
    try:
        l.remove_element_at(-1) #Gives error as it should
    except IndexError:
        print("remove_element_at correctly gives an index error when out of bounds")
    print(l.__len__())
    l = Linked_List()
    for i in range(10):
        l.append_element(i)
    print(l.__str__())
    print(l.get_element_at(0))
    print(l.get_element_at(1))
    print(l.get_element_at(7))
    print(l.get_element_at(9))
    #Checking if remove_element_at works on the last node
    print(l.remove_element_at(9))
    l = Linked_List()
    try:
        print(l.get_element_at(0))
    except IndexError:
        print("Correctly gives an index error when getting from an empty list")
    l.append_element(0)
    print(l.get_element_at(0))
    try:
        print(l.get_element_at(-1))
    except IndexError:
        print("Correctly gives an index error when out of bounds")
    try:
        print(l.get_element_at(2))
    except IndexError:
        print("Correctly gives an index error when out of bounds")
    l = Linked_List()
    print(l.__str__())
    l.rotate_left()
    print(l.__str__())
    l.append_element((1))
    print(l.__str__())
    l.rotate_left()
    print(l.__str__())
    l.append_element((2))
    print(l.__str__())
    l.rotate_left()
    print(l.__str__())
    l.append_element((3))
    print(l.__str__())
    l.rotate_left()
    print(l.__str__())
    #Testing next and iter
    for value in l:
        print("Working: "+ str(value))
    #Making sure it doesn't iterate on an empty list
    l = Linked_List()
    for value in l:
        print(str(value))