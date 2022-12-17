import sys # for sys.argv, the command-line arguments

from Stack import Stack


def delimiter_check(filename):
  delimiters = {"[": "]", "(": ")", "{": "}", None: None}
  #None is for when there is a closing delimiter and the Stack is empty
  #The stack returns None when popped empty, so I need to have None in the dictionary
  #To avoid an error
  close_delimiters = {"]", ")", "}"}
  #Set and dictionary used for O(1) access/membership checking
  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.
  with open(filename) as f: #Syntax obtained from here:
    # https://realpython.com/read-write-files-python/#reading-and-writing-opened-files
    str_representation = f.read()
  my_stack = Stack()
  #print(str_representation)
  for character in str_representation:
    if character in delimiters:
      my_stack.push(character)
    elif character in close_delimiters:
      if delimiters[my_stack.pop()] != character:
        return False
  return len(my_stack) == 0

  #print(str_representation) #Just to check that I'm doing this right

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


