import unittest
from Binary_Search_Tree import Binary_Search_Tree


class BSTTester(unittest.TestCase):
    def setUp(self):
        self.__tree = Binary_Search_Tree()
    
    def test_empty_attributes(self):
        self.assertEqual(0, self.__tree.get_height()) #Empty BST should have a height of 0
        self.assertEqual("[ ]", self.__tree.in_order()) #Empty string representation of a BST
        self.assertEqual("[ ]", self.__tree.post_order())
        self.assertEqual("[ ]", self.__tree.pre_order())

    def test_one_element_tree(self): #Making sure a 1 element tree is correct; 
        #this shouldn't be a special case, but may as well test it
        #Checks if inserting on an empty tree works
        self.__tree.insert_element(1)
        self.assertEqual(1, self.__tree.get_height())
        self.assertEqual("[ 1 ]", self.__tree.in_order()) #One string representation of a BST
        self.assertEqual("[ 1 ]", self.__tree.post_order())
        self.assertEqual("[ 1 ]", self.__tree.pre_order())

    def test_in_order_traversal(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(3) #Should make a tree that looks like: 2
        self.assertEqual("[ 1, 2, 3 ]", self.__tree.in_order())          #1 3

    def test_pre_order_traversal(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(3) 
        self.assertEqual("[ 2, 1, 3 ]", self.__tree.pre_order())

    def test_post_order_traversal(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(3) 
        self.assertEqual("[ 1, 3, 2 ]", self.__tree.post_order())

    def test_insert_one_two(self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(75)
        self.assertEqual("[ 50, 75 ]", self.__tree.in_order())
        self.assertEqual("[ 50, 75 ]", self.__tree.pre_order())
        self.assertEqual("[ 75, 50 ]", self.__tree.post_order())
        self.assertEqual(2, self.__tree.get_height())

    def test_insert_one_two_three_balanced(self):
         #Testing if insertion puts in a third val correctly on a balanced tree
        self.__tree.insert_element(50)
        self.__tree.insert_element(75)
        self.__tree.insert_element(20)
        self.assertEqual("[ 20, 50, 75 ]", self.__tree.in_order())
        self.assertEqual("[ 50, 20, 75 ]", self.__tree.pre_order())
        self.assertEqual("[ 20, 75, 50 ]", self.__tree.post_order())
        self.assertEqual(2, self.__tree.get_height()) #No height change

    def test_insert_duplicate(self):
        self.__tree.insert_element(1)
        try:
            self.__tree.insert_element(1)
        except ValueError:
            self.assertEqual(1, self.__tree.get_height())
            self.assertEqual("[ 1 ]", self.__tree.in_order()) #remove shouldn't change the tree
            self.assertEqual("[ 1 ]", self.__tree.post_order())
            self.assertEqual("[ 1 ]", self.__tree.pre_order())
        

    def test_insert_one_two_three_unbalanced(self): 
    #Testing if insertion puts in a third val correctly on an unbalanced tree
    #Using the same values as the previous test case
        self.__tree.insert_element(20)
        self.__tree.insert_element(50)
        self.__tree.insert_element(75)
        self.assertEqual("[ 20, 50, 75 ]", self.__tree.in_order())
        self.assertEqual("[ 20, 50, 75 ]", self.__tree.pre_order())
        self.assertEqual("[ 75, 50, 20 ]", self.__tree.post_order())
        self.assertEqual(3, self.__tree.get_height()) #Height change

    def test_remove_on_empty(self):
        try:
            self.__tree.remove_element(1)
        except ValueError:
            self.assertEqual(0, self.__tree.get_height())
            self.assertEqual("[ ]", self.__tree.in_order()) #Empty string representation of a BST
            self.assertEqual("[ ]", self.__tree.post_order())
            self.assertEqual("[ ]", self.__tree.pre_order())
    
    def test_remove_on_one(self):
        self.__tree.insert_element(1)
        self.__tree.remove_element(1)
        self.assertEqual(0, self.__tree.get_height())
        self.assertEqual("[ ]", self.__tree.in_order()) #Empty string representation of a BST
        self.assertEqual("[ ]", self.__tree.post_order())
        self.assertEqual("[ ]", self.__tree.pre_order())

    def test_remove_non_existent_value(self):
        self.__tree.insert_element(1)
        try:
            self.__tree.remove_element(2)
        except ValueError:
            self.assertEqual(1, self.__tree.get_height()) #Remove shouldn't shrink tree's height in this case
            self.assertEqual("[ 1 ]", self.__tree.in_order()) #remove shouldn't change the tree
            self.assertEqual("[ 1 ]", self.__tree.post_order())
            self.assertEqual("[ 1 ]", self.__tree.pre_order())

    def test_remove_no_children(self): #Remove a node with no children
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(3)
        self.__tree.remove_element(1)
        self.assertEqual(2, self.__tree.get_height())
        self.assertEqual("[ 2, 3 ]", self.__tree.in_order())
        self.assertEqual("[ 2, 3 ]", self.__tree.pre_order())
        self.assertEqual("[ 3, 2 ]", self.__tree.post_order())
    
    def test_remove_left_child(self): #Remove a node with a left child
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(3)
        self.__tree.insert_element(0)
        self.__tree.remove_element(1)
        self.assertEqual(2, self.__tree.get_height()) #Note that height changes from 3 to 2
        self.assertEqual("[ 0, 2, 3 ]", self.__tree.in_order())
        self.assertEqual("[ 2, 0, 3 ]", self.__tree.pre_order())
        self.assertEqual("[ 0, 3, 2 ]", self.__tree.post_order())
          
    def test_remove_right_child(self): #Remove a node with a right child
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(3)
        self.__tree.insert_element(1.5)
        self.__tree.remove_element(1)
        self.assertEqual(2, self.__tree.get_height()) #Note that height changes from 3 to 2
        self.assertEqual("[ 1.5, 2, 3 ]", self.__tree.in_order())
        self.assertEqual("[ 2, 1.5, 3 ]", self.__tree.pre_order())
        self.assertEqual("[ 1.5, 3, 2 ]", self.__tree.post_order())

    def test_remove_two_children(self): #Remove a node with two children
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(3)
        self.__tree.insert_element(1.5)
        self.__tree.insert_element(0)
        self.__tree.remove_element(1)
        self.assertEqual(3, self.__tree.get_height()) 
        self.assertEqual("[ 0, 1.5, 2, 3 ]", self.__tree.in_order())
        self.assertEqual("[ 2, 1.5, 0, 3 ]", self.__tree.pre_order())
        self.assertEqual("[ 0, 1.5, 3, 2 ]", self.__tree.post_order())

    def test_remove_at_root(self): #Remove at root
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(3)
        self.__tree.remove_element(2)
        self.assertEqual(2, self.__tree.get_height())
        self.assertEqual("[ 1, 3 ]", self.__tree.in_order())
        self.assertEqual("[ 3, 1 ]", self.__tree.pre_order())
        self.assertEqual("[ 1, 3 ]", self.__tree.post_order())

    def test_remove_left_child_subtree(self): 
    #To make sure that swapping the lowest value on the right subtree with the removed node's value works
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(1)
        self.__tree.remove_element(3)
        self.assertEqual(4, self.__tree.get_height())
        self.assertEqual("[ 1, 2, 4, 5 ]", self.__tree.in_order())
        self.assertEqual("[ 5, 4, 2, 1 ]", self.__tree.pre_order())
        self.assertEqual("[ 1, 2, 4, 5 ]", self.__tree.post_order())


    def test_remove_two_children_subtree(self):
    #Remove a node with two children whose right child has children
    #To make sure that in the case of removing a child with two children
    #Whose right child also has children
    #That the lowest value of the right subtree of the removed element is swapped in
    #To make sure that swapping the lowest value on the right subtree with the removed node's value works
    #When there are other children of the lowest node's parent
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3.5)
        self.__tree.insert_element(4.5)
        self.__tree.remove_element(3)
        self.assertEqual(4, self.__tree.get_height())
        self.assertEqual("[ 2, 3.5, 4, 4.5, 5 ]", self.__tree.in_order())
        self.assertEqual("[ 5, 3.5, 2, 4, 4.5 ]", self.__tree.pre_order())
        self.assertEqual("[ 2, 4.5, 4, 3.5, 5 ]", self.__tree.post_order())


   
    


if __name__ == "__main__":
    unittest.main()