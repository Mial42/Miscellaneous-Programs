import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

  def test_print_empty(self):
    self.assertEqual(len(self.__deque), 0)
    #Testing that a pristine DQ has the right length and prints correctly
    self.assertEqual("[ ]", str(self.__deque))
  def test_print_one(self):
    self.__deque.push_front('1')
    self.assertEqual("[ 1 ]", str(self.__deque))
  def test_print_two(self):
    self.__deque.push_front('1')
    self.__deque.push_front('2')
    self.assertEqual("[ 2, 1 ]", str(self.__deque))

  def test_push_front_empty(self):
    self.__deque.push_front('1')
    self.assertEqual("[ 1 ]", str(self.__deque))
    self.assertEqual(len(self.__deque), 1)

  def test_push_back_empty(self):
    self.__deque.push_back('1')
    self.assertEqual("[ 1 ]", str(self.__deque))
    self.assertEqual(len(self.__deque), 1)

  def test_push_front_one(self):
    self.__deque.push_front('1')
    self.__deque.push_front('2')
    self.assertEqual("[ 2, 1 ]", str(self.__deque))
    self.assertEqual(len(self.__deque), 2)


  def test_push_back_one(self):
    self.__deque.push_back('1')
    self.__deque.push_back('2')
    self.assertEqual("[ 1, 2 ]", str(self.__deque))
    self.assertEqual(len(self.__deque), 2)

  def test_push_front_two(self):
    self.__deque.push_front('1')
    self.__deque.push_front('2')
    self.__deque.push_front('3')
    self.assertEqual("[ 3, 2, 1 ]", str(self.__deque))
    self.assertEqual(len(self.__deque), 3)

  def test_push_back_two(self):
    self.__deque.push_back('1')
    self.__deque.push_back('2')
    self.__deque.push_back('3')
    self.assertEqual("[ 1, 2, 3 ]", str(self.__deque))
    self.assertEqual(len(self.__deque), 3)

  def test_push_front_five(self):
    for i in range(1, 6):
      self.__deque.push_front(str(i))
    self.assertEqual("[ 5, 4, 3, 2, 1 ]", str(self.__deque))
    self.assertEqual(len(self.__deque), 5)

  def test_push_back_five(self):
    for i in range(1, 6):
      self.__deque.push_back(str(i))
    self.assertEqual("[ 1, 2, 3, 4, 5 ]", str(self.__deque))
    self.assertEqual(len(self.__deque), 5)

  def test_alternate_push_front_and_back(self):
    self.__deque.push_front("f1")
    self.__deque.push_back("b1")
    self.__deque.push_front("f2")
    self.__deque.push_back("b2")
    self.assertEqual("[ f2, f1, b1, b2 ]", str(self.__deque))
    self.assertEqual(len(self.__deque), 4)

  def test_peek_front_empty(self):
    temp = self.__deque.peek_front()
    self.assertEqual(temp, None)

  def test_peek_back_empty(self):
    temp = self.__deque.peek_back()
    self.assertEqual(temp, None)

  def test_peek_front_one(self):
    self.__deque.push_front('1')
    temp = self.__deque.peek_front()
    self.assertEqual(temp, "1")

  def test_peek_back_one(self):
    self.__deque.push_front('1')
    temp = self.__deque.peek_back()
    self.assertEqual(temp, "1")

  def test_peek_front_two(self):
    self.__deque.push_back('1')
    self.__deque.push_front('2')
    temp = self.__deque.peek_front()
    self.assertEqual(temp, "2")

  def test_peek_back_two(self):
    self.__deque.push_front('1')
    self.__deque.push_back('2')
    temp = self.__deque.peek_back()
    self.assertEqual(temp, "2")

  def test_pop_front_empty(self):
    temp = self.__deque.pop_front()
    self.assertEqual(temp, None)
    #Making sure I don't accidentally make my DQ length negative
    self.assertEqual(len(self.__deque), 0)

  def test_pop_back_empty(self):
    temp = self.__deque.pop_back()
    self.assertEqual(temp, None)
    self.assertEqual(len(self.__deque), 0)

  def test_pop_front_one(self):
    self.__deque.push_front("1")
    temp = self.__deque.pop_front()
    self.assertEqual(temp, "1")
    self.assertEqual(len(self.__deque), 0)
    self.assertEqual("[ ]", str(self.__deque))

  def test_pop_back_one(self):
    self.__deque.push_front("1")
    temp = self.__deque.pop_back()
    self.assertEqual(temp, "1")
    self.assertEqual(len(self.__deque), 0)
    self.assertEqual("[ ]", str(self.__deque))

  def test_pop_front_two(self):
    self.__deque.push_front("2")
    self.__deque.push_front("1")
    temp = self.__deque.pop_front()
    self.assertEqual(temp, "1")
    self.assertEqual(len(self.__deque), 1)
    self.assertEqual("[ 2 ]", str(self.__deque))

  def test_pop_back_two(self):
    self.__deque.push_front("2")
    self.__deque.push_back("1")
    temp = self.__deque.pop_back()
    self.assertEqual(temp, "1")
    self.assertEqual(len(self.__deque), 1)
    self.assertEqual("[ 2 ]", str(self.__deque))

  def test_pop_front_five(self):
    for i in range(5):
      self.__deque.push_front(str(i))
    for i in range(4, -1, -1):
      temp = self.__deque.pop_front()
      self.assertEqual(temp, str(i))

  def test_pop_back_five(self):
    for i in range(5):
      self.__deque.push_back(str(i))
    for i in range(4, -1, -1):
      temp = self.__deque.pop_back()
      self.assertEqual(temp, str(i))

  def test_alternate_pop_front_and_back(self):
    self.__deque.push_front("f1")
    self.__deque.push_back("b1")
    self.__deque.push_front("f2")
    self.__deque.push_back("b2")
    b2 = self.__deque.pop_back()
    f2 = self.__deque.pop_front()
    self.assertEqual(b2, "b2")
    self.assertEqual(f2, "f2")
    self.assertEqual("[ f1, b1 ]", str(self.__deque))

  def test_enqueue_empty(self):
    self.__queue.enqueue("1")
    self.assertEqual(len(self.__queue), 1)
    self.assertEqual("[ 1 ]", str(self.__queue))

  def test_dequeue_empty(self):
    temp = self.__queue.dequeue()
    self.assertEqual(None, temp)
    self.assertEqual(0, len(self.__queue))
    self.assertEqual("[ ]", str(self.__queue))

  def test_enqueue_one(self):
    self.__queue.enqueue("1")
    self.__queue.enqueue("2")
    self.assertEqual(len(self.__queue), 2)
    self.assertEqual("[ 2, 1 ]", str(self.__queue))

  def test_dequeue_one(self):
    self.__queue.enqueue("1")
    temp = self.__queue.dequeue()
    self.assertEqual("1", temp)
    self.assertEqual(0, len(self.__queue))
    self.assertEqual("[ ]", str(self.__queue))

  def test_dequeue_two(self):
    self.__queue.enqueue("1")
    self.__queue.enqueue("2")
    temp = self.__queue.dequeue()
    self.assertEqual("1", temp)
    self.assertEqual(1, len(self.__queue))
    self.assertEqual("[ 2 ]", str(self.__queue))


  def test_q_peek_empty(self):
    temp = self.__queue.peek()
    self.assertEqual(None, temp)
    self.assertEqual(0, len(self.__queue))
    self.assertEqual("[ ]", str(self.__queue))

  def test_q_peek_one(self):
    self.__queue.enqueue("1")
    temp = self.__queue.peek()
    self.assertEqual(temp, "1")
    self.assertEqual(1, len(self.__queue))
    self.assertEqual("[ 1 ]", str(self.__queue))

  def test_q_peek_two(self):
    self.__queue.enqueue("1")
    self.__queue.enqueue("2")
    temp = self.__queue.peek()
    self.assertEqual(temp, "1")
    self.assertEqual(2, len(self.__queue))
    self.assertEqual("[ 2, 1 ]", str(self.__queue))

  def test_push_empty(self):
    self.__stack.push("1")
    self.assertEqual(len(self.__stack), 1)
    self.assertEqual("[ 1 ]", str(self.__stack))

  def test_pop_empty(self):
    temp = self.__stack.pop()
    self.assertEqual(temp, None)
    self.assertEqual(0, len(self.__stack))
    self.assertEqual("[ ]", str(self.__stack))

  def test_push_one(self):
    self.__stack.push("1")
    self.__stack.push("2")
    self.assertEqual(len(self.__stack), 2)
    self.assertEqual("[ 2, 1 ]", str(self.__stack))

  def test_pop_one(self):
    self.__stack.push("1")
    temp = self.__stack.pop()
    self.assertEqual(temp, "1")
    self.assertEqual(0, len(self.__stack))
    self.assertEqual("[ ]", str(self.__stack))

  def test_pop_two(self):
    self.__stack.push("1")
    self.__stack.push("2")
    temp = self.__stack.pop()
    self.assertEqual(temp, "2")
    self.assertEqual(1, len(self.__stack))
    self.assertEqual("[ 1 ]", str(self.__stack))

  def test_s_peek_empty(self):
    temp = self.__stack.peek()
    self.assertEqual(None, temp)
    self.assertEqual(0, len(self.__stack))
    self.assertEqual("[ ]", str(self.__stack))

  def test_s_peek_one(self):
    self.__stack.push("1")
    temp = self.__stack.peek()
    self.assertEqual("1", temp)
    self.assertEqual(1, len(self.__stack))
    self.assertEqual("[ 1 ]", str(self.__stack))

  def test_s_peek_two(self):
    self.__stack.push("1")
    self.__stack.push("2")
    temp = self.__stack.peek()
    self.assertEqual("2", temp)
    self.assertEqual(2, len(self.__stack))
    self.assertEqual("[ 2, 1 ]", str(self.__stack))
  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_

if __name__ == '__main__':
  unittest.main()

