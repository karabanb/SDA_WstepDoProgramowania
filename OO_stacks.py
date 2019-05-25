
class Stack:

    def __init__(self):
        self._stack = []

    def pop(self):
        """Pop element form the stack"""
        if len(self._stack) > 0:
            return self._stack.pop()
        return None

    def push(self, element):
        """Push element to the stack"""
        self._stack.append(element)


if __name__ == '__main__':
    my_stack = Stack()
    print(dir(my_stack))

    my_stack.push(7)
    my_stack.push(42)

    print(my_stack._stack)

    element = my_stack.pop()
    print(element)
    print(my_stack._stack)

    element2 = my_stack.pop()
