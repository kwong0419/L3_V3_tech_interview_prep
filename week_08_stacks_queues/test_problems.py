from problems import valid_parentheses, min_stack, implement_queue_using_stacks

def test_valid_parentheses():
    assert valid_parentheses("()") == True
    assert valid_parentheses("()[]{}") == True
    assert valid_parentheses("(]") == False
    assert valid_parentheses("([)]") == False
    assert valid_parentheses("{[]}") == True
    
    assert valid_parentheses("]") == False

def test_min_stack():
    stack = min_stack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.getMin() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.getMin() == -2

    stack2 = min_stack()
    stack2.push(-1)
    assert stack2.top() == -1
    assert stack2.getMin() == -1
    stack2.pop()

def test_implement_queue_using_stacks():
    queue = implement_queue_using_stacks()
    queue.push(1)              # queue is: [1]
    queue.push(2)              # queue is: [1, 2]
    assert queue.peek() == 1   # return 1
    assert queue.pop() == 1    # return 1, queue is [2]
    assert queue.empty() == False

    queue2 = implement_queue_using_stacks()
    assert queue2.empty() == True 
    queue2.push(1)              # queue is: [1]
    queue2.push(2)              # queue is: [1, 2]
    queue2.push(3)              # queue is: [1, 2, 3]
    assert queue2.pop() == 1    # return 1, queue is [2, 3]
    assert queue2.pop() == 2    # return 2, queue is [3]
    assert queue2.peek() == 3   # return 3

if __name__ == "__main__":
    test_valid_parentheses()
    test_min_stack()
    test_implement_queue_using_stacks()
