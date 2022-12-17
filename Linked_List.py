class Linked_List:
    class __Node:
        __slots__ = "__val", "__nxt", "__prev" #Taken from the book to streamline memory

        def __init__(self, val):
            # declare and initialize the public attributes
            # for objects of the Node class.
            # TODO replace pass with your implementation
            self.__val = val
            #print("This is my value " + str(val))
            self.__nxt = None
            self.__prev = None

        def get_next(self):
            return self.__nxt

        def get_prev(self):
            return self.__prev

        def set_next(self, node):
            self.__nxt = node

        def set_prev(self, node):
            self.__prev = node

        def get_val(self):
            return self.__val

        def set_val(self, new_val):
            self.__val = new_val

    __slots__ = "__header", "__trailer", "__length"
    def __init__(self):
        # declare and initialize the private attributes
        # for objects of the sentineled Linked_List class
        # TODO replace pass with your implementation
        self.__length = 0
        self.__header = self.__Node(None)
        self.__trailer = self.__Node(None)
        self.__header.set_next(self.__trailer)
        self.__trailer.set_prev(self.__header)


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
        newest.set_next(self.__trailer) #Set the next of newest to the trailer
        newest.set_prev(self.__trailer.get_prev()) #Set the prev of newest to the previous last node
        self.__trailer.get_prev().set_next(newest) #set the next of the previous last node to the newest
        self.__trailer.set_prev(newest)
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
                cur = cur.get_next()
        #Cur is the node that needs to be before newest
        else:
            #Since you can't insert after the trailer or after the last node
            cur = self.__trailer.get_prev().get_prev()
            counter = self.__length - 1
            while counter > index:
                counter = counter - 1
                cur = cur.get_prev()
        newest.set_prev(cur)
        newest.set_next(cur.get_next())
        cur.get_next().set_prev(newest)
        cur.set_next(newest)
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
                cur = cur.get_next()
                counter = counter + 1
        else:
            cur = self.__trailer
            counter = self.__length
            while counter > index:
                cur = cur.get_prev()
                counter = counter - 1
        result = cur.get_val() #Storing the value to be returned
        cur.get_next().set_prev(cur.get_prev()) #Removing cur from the list
        cur.get_prev().set_next(cur.get_next())
        self.__length = self.__length - 1
        return result

    def get_element_at(self, index):
        if index < 0 or index >= self.__length:
            raise IndexError("Sorry, your proposed index is out of bounds.")
        if index < self.__length / 2:
            cur = self.__header
            counter = -1
            while counter < index:
                cur = cur.get_next()
                counter = counter + 1
        else:
            cur = self.__trailer
            counter = self.__length
            while counter > index:
                cur = cur.get_prev()
                counter = counter - 1
        result = cur.get_val()  # Storing the value to be returned
        return result

    def rotate_left(self):
        # rotate the list left one position. Conceptual indices
        # should all decrease by one, except for the head, which
        # should become the tail. For example, if the list is
        # [ 5, 7, 9, -4 ], this method should alter it to
        # [ 7, 9, -4, 5 ]. This method should modify the list in
        # place and must not return a value.
        # TODO replace pass with your implementation.
        cur = self.__header.get_next()
        head_value = cur.get_val()
        while cur is not self.__trailer:
            cur.set_val(cur.get_next().get_val())
            cur = cur.get_next()
        self.__trailer.get_prev().set_val(head_value)

    def __str__(self):
        # return a string representation of the list's
        # contents. An empty list should appear as [ ].
        # A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ].
        # You may assume that the values stored inside of the
        # node objects implement the __str__() method, so you
        # call str(val_object) on them to get their string
        # representations.
        # TODO replace pass with your implementation
        result = "[ "
        cur = self.__header.get_next()
        #print(cur.get_val())
        while cur is not self.__trailer:
            elem = str(cur.get_val())
            result = result + elem
            if cur.get_next() is not self.__trailer:
                result = result + ", "
            else:
                result = result + " "
            cur = cur.get_next()
        return result + "]"



    def __iter__(self):
        # initialize a new attribute for walking through your list
        # TODO insert your initialization code before the return
        # statement. do not modify the return statement.
        return self

    def __next__(self):
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
    for i in range(11):
        l.append_element(i)
    # print(l.__len__())
    print(l.__str__())
    # l.insert_element_at(55, 0)
    # print(l.__str__())
    # l.insert_element_at(99, 11)
    # print(l.__str__())
    # l = Linked_List()
    # #l.insert_element_at(55, 0) #Gives error as it should
    # l.append_element(0)
    # print(l.__str__())
    # l.insert_element_at(55, 0)
    # print(l.__str__())
    # print(l.remove_element_at(0))
    # print(l.__str__())
    # print(l.remove_element_at(10))
    # print(l.__str__())
    # print(l.remove_element_at(2))
    # print(l.__str__())
    # print(l.remove_element_at(6))
    # print(l.__str__())
    # print(l.__len__())
    l.rotate_left()
    print(l.__str__())
    l = Linked_List()
    print(l.__str__())
    l.rotate_left()
    print(l.__str__())
    l.append_element((1))
    print(l.__str__())
    l.rotate_left()
    print(l.__str__())