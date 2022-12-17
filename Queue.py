from Deque_Generator import get_deque

class Queue:
  __slots__ = "__dq"
  def __init__(self):
    # TODO replace pass with your implementation.
    self.__dq = get_deque()
    pass

  def __str__(self):
    # TODO replace pass with your implementation.
    return str(self.__dq)

  def __len__(self):
    # TODO replace pass with your implementation.
    return len(self.__dq)

  def enqueue(self, val):
    # TODO replace pass with your implementation.
    self.__dq.push_front(val)

  def dequeue(self):
    # TODO replace pass with your implementation.
    return self.__dq.pop_back()

  def peek(self):
    # TODO replace pass with your implementation.
    return self.__dq.peek_back()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
  
