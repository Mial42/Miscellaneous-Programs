from Deque import Deque


class Array_Deque(Deque):
    __slots__ = "__capacity", "__contents", "__front", "__back", "__length"

    def __init__(self):
        # capacity starts at 1; we will grow on demand.
        self.__capacity = 1
        self.__contents = [None] * self.__capacity
        self.__front = None
        self.__back = None
        self.__length = 0
        # TODO replace pass with any additional initializations you need.

    def __str__(self):
        # TODO replace pass with an implementation that returns a string of
        # exactly the same format as the __str__ method in the Linked_List_Deque.
        #print(self.__contents)
        #TODO FIX this so single quotes don't appear around string entries when printed
        if self.__length == 0:
            return "[ ]"
        elif self.__length == 1:
            return "[ " + str(self.__contents[self.__front]) + " ]"
        else:
            #temp_arr = [None] * self.__length
            i = self.__front
            j = 0
            result = '[ ' + str(self.__contents[i]) + ", "
            #temp_arr[j] = self.__contents[i]
            # print("BACK: " + str(self.__back))
            # print("FRONT: " + str(self.__front))
            while i != self.__back:
                i = ((i + 1) + len(self.__contents)) % len(self.__contents)
                #j = j + 1
                #temp_arr[j] = self.__contents[i]
                result = result + str(self.__contents[i]) + ", "
            result = result[:len(result) - 2] + " ]"
            return result
            #return "[ " + str(temp_arr)[1:len(str(temp_arr)) - 1] + " ]"

    # def get_raw_contents(self):  # PURELY for testing purposes
    #     return self.__contents

    def __len__(self):
        # TODO replace pass with an implementation that returns the number of
        # items in the deque. This method must run in constant time.
        return self.__length

    def __grow(self):
        # TODO replace pass with an implementation that doubles the capacity
        # and positions existing items in the deque starting in cell 0 (why is
        # necessary?)
        new_contents = [None] * self.__capacity * 2
        self.__capacity = self.__capacity * 2
        i = self.__front
        j = 0
        new_contents[j] = self.__contents[i]
        # print("Front = " + str(self.__front))
        # print("Back = " + str(self.__back))
        while i != self.__back:
            # print("i: " + str(i))
            # print("j: " + str(j))
            i = ((i + 1) + len(self.__contents)) % len(self.__contents)
            j = j + 1
            new_contents[j] = self.__contents[i]
        #print(new_contents)
        self.__front = 0
        self.__back = j
        self.__contents = new_contents

    def push_front(self, val):
        # TODO replace pass with your implementation, growing the array before
        # pushing if necessary.
        # print("Length: " + str(self.__length))
        # print("Capacity: " + str(self.__capacity))
        if self.__length == 0:
            self.__front = 0
            self.__back = 0
            self.__contents[0] = val
        elif self.__length == self.__capacity:
            self.__grow()
        if self.__length != 0:
            self.__front = ((self.__front - 1) + len(self.__contents)) % len(self.__contents)
            self.__contents[self.__front] = val
        self.__length = self.__length + 1
        # print("Length: " + str(self.__length))
        # print("Capacity: " + str(self.__capacity))
        # print("DEBUG: THIS IS THE FRONT: " + str(self.__front))

    def pop_front(self):
        # TODO replace pass with your implementation. Do not reduce the capacity.
        if self.__length == 0:
            return None
        temp = self.__contents[self.__front]
        if self.__length == 1:
            self.__contents[self.__front] = None
            self.__back = None
            self.__front = None
        else:
            self.__front = ((self.__front + 1) + len(self.__contents)) % len(self.__contents)
        self.__length = self.__length - 1
        return temp

    def peek_front(self):
        if self.__front is None:
            return None
        else:
            return self.__contents[self.__front]

    def push_back(self, val):
        # TODO replace pass with your implementation, growing the array before
        # pushing if necessary.
        if self.__length == 0:
            self.__front = 0
            self.__back = 0
            self.__contents[0] = val
        elif self.__length == self.__capacity:
            self.__grow()
        if self.__length != 0:
            self.__back = ((self.__back + 1) + len(self.__contents)) % len(self.__contents)
            self.__contents[self.__back] = val
        self.__length = self.__length + 1

    def pop_back(self):
        # TODO replace pass with your implementation. Do not reduce the capacity.
        if self.__length == 0:
            return None
        temp = self.__contents[self.__back]
        if self.__length == 1:
            self.__contents[self.__back] = None
            self.__back = None
            self.__front = None
        else:
            self.__back = ((self.__back - 1) + len(self.__contents)) % len(self.__contents)
        self.__length = self.__length - 1
        return temp

    def peek_back(self):
        # TODO replace pass with your implementation.
        if self.__back is None:
            return None
        else:
            return self.__contents[self.__back]


# No main section is necessary. Unit tests take its place.
# if __name__ == '__main__':
#  pass
# Just some testing
# test_arr = Array_Deque()
# print(test_arr)
# test_arr.push_front(str(1))
# print(test_arr)
# for r in range(2, 10):
#   test_arr.push_front(str(r))
#   print(test_arr)
# #print(test_arr)
# print(test_arr.peek_front())
# print(test_arr.pop_front())
# print(test_arr)
# while test_arr.peek_front() is not None:
#   print(test_arr.pop_front())
#   print(test_arr)
# #print(test_arr)
# test_arr.push_back(1)
# print(test_arr)
# for r in range(2, 10):
#   test_arr.push_back(r)
#   print(test_arr)
# print(test_arr.peek_back())
# print(test_arr.pop_back())
# print(test_arr.pop_front())
# print(test_arr.pop_front())
# print(test_arr.pop_back())
# print(test_arr)
# test_arr.push_front("FRONTAL!")
# print(test_arr)
# test_arr.push_back(("REAR!"))
# print(test_arr)
# for i in range(11, 200):
#   test_arr.push_front(i)
#   test_arr.push_back((-1 * i))
# print(test_arr)
#print(test_arr)