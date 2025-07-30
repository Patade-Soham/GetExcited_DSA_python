def push(stack,item):
    stack.append(item)
    return stack
def Pop(stack):
    if isEmpty(stack):
        print('Stack Underflow.')
        return 
    else:    
        stack.pop()
        
def peek(stack):
    if isEmpty(stack):
        print('Stack Emptyy.')
        return 
    else:    
        return stack[len(stack)-1]
def display(stack):
    if isEmpty(stack):
        print('Stack is Empty.')
        return 
    else:    
        print(stack)
        return
def isEmpty(stack):
    if len(stack)-1 == 0:
        return True
    return False
stack=[]
push(stack,8)
push(stack,9)
push(stack,6)
push(stack,4)
display(stack)
Pop(stack)
display(stack)
Pop(stack)
display(stack)
Pop(stack)
display(stack)
Pop(stack)
display(stack)
Pop(stack)
