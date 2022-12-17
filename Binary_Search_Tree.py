class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      #print("Constructor Called: " + str(value))
      self.value = value
      self.left = None
      self.right = None
      self.height = 1
      # TODO complete Node initialization
    def update_height(self):
      if self.left is None and self.right is None:
        self.height = 1
      elif self.left is None:
        self.height = self.right.height + 1
      elif self.right is None:
        self.height = self.left.height + 1
      else:
        self.height = 1 + max(self.right.height, self.left.height)
    # def is_leaf(self):
    #   return self.left is None and self.right is None
    def __str__(self):
      return str(self.value)

  def __init__(self):
    self.__root = None
    # TODO complete initialization

  def insert_element(self, value):
    self.__root = self.__recursively_insert_element(self.__root, value)
    #print(str(self.__root))
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.

    #pass # TODO replace pass with your implementation
  #Node t is the node being inserted
  #Need to figure out how to deal with the height
  def __recursively_insert_element(self, t, value):
    if t is None:
      #print("line 50: " + str(value))
      temp = Binary_Search_Tree.__BST_Node(value)
      return temp
    else:
      if value == t.value:
        raise ValueError
      if value < t.value:
        #print("line 56: " + str(value))
        t.left = self.__recursively_insert_element(t.left, value)
      else:
        #print("line 59: " + str(value))
        t.right = self.__recursively_insert_element(t.right, value)
      t.update_height()
      return t

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    #pass # TODO replace pass with your implementation
    self.__root = self.__recursively_remove_element(value, self.__root)

  def __recursively_remove_element(self, value, t):
    if t is None:
      raise ValueError
    elif value < t.value:
      t.left = self.__recursively_remove_element(value, t.left)
    elif value > t.value: 
      t.right = self.__recursively_remove_element(value, t.right)
    else: #If I've found what needs removing
      #Several cases
      if t.left is not None and t.right is not None:
        t.value = self.__get_min_value(t.right, t.value) 
        t.right = self.__recursively_remove_element(value, t.right)
      elif t.left is None:
        t = t.right
      else:
        t = t.left
    if t is not None:
      t.update_height()
    return t
  
  #Returns the minimum value in the subtree rooted at t and changes the value where the minimum used to be to be the value
  #of the node the function was initially called on
  #used by recursively_remove_element
  def __get_min_value(self, t, initial_value):
    if t is None:
      return ValueError
    while t.left is not None:
      t = t.left
    minimum_value = t.value
    t.value = initial_value
    return minimum_value


  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # elif self.__root.height == 1:
    #   return "[ " + str(self.__root.value) + "]"
    # else:
    #   unprocessed_str = self.__recursive_in_order(self.__root, "[ ")
    #   return unprocessed_str[:len(unprocessed_str) - 2] + "]"
    if self.__root is None:
      return "[ ]"
    python_list_representation = self.__recursive_in_order(self.__root)
    unprocessed_str = ", ".join(python_list_representation)
    return "[ " + unprocessed_str + " ]"
    #pass # TODO replace pass with your implementation
  #Recursive helper method
  def __recursive_in_order(self, t):
    if t is None: #Base Case
      return []
    return self.__recursive_in_order(t.left) + [str(t.value)] + self.__recursive_in_order(t.right)


  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root is None: #Hardcoded because of spacing
      return "[ ]"
    python_list_representation = self.__recursive_pre_order(self.__root)
    #a list representation of the tree's contents
    unprocessed_str = ", ".join(python_list_representation)
    return "[ " + unprocessed_str + " ]"
  def __recursive_pre_order(self, t):
    if t is None:
      return []
    return [str(t.value)] + self.__recursive_pre_order(t.left) + self.__recursive_pre_order(t.right)


  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root is None:
      return "[ ]"
    python_list_representation = self.__recursive_post_order(self.__root)
    unprocessed_str = ", ".join(python_list_representation)
    return "[ " + unprocessed_str + " ]"
  def __recursive_post_order(self, t):
    if t is None:
      return []
    return  self.__recursive_post_order(t.left) + self.__recursive_post_order(t.right)+ [str(t.value)]

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    if self.__root is None:
      return 0
    else:
      return self.__root.height
    #pass # TODO replace pass with your implementation

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.


# print(str(tree.get_height()))
# print(str(tree))
# tree.insert_element(1)
# print(str(tree.get_height()))
# print(str(tree))
# tree = Binary_Search_Tree()
# tree.insert_element(50)
# tree.insert_element(20)
# tree.insert_element(75)
# tree.insert_element(80)
# tree.insert_element(90)
# print(tree.get_height())
# print(str(tree))
# tree.remove_element(75)
# print(tree.get_height())
# print(str(tree))
# tree.insert_element(75)
# print(tree.get_height())
# print(str(tree))
# tree.remove_element(20)
# print(tree.get_height())
# print(str(tree))
# tree.remove_element(50)
# print(tree.get_height())
# print(str(tree))
# tree.insert_element(83)
# tree.insert_element(81)
# tree.insert_element(85)
# tree.insert_element(82)
# print(tree.get_height())
# print(str(tree))
# tree.remove_element(80)
# print(tree.get_height())
# print(str(tree))
# tree.remove_element(81)
# print(tree.get_height())
# print(str(tree))
