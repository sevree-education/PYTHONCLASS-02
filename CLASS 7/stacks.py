mystack = []

def add_stack(x):
    mystack.append(x)

def delete_stack():
    if mystack:
        return mystack.pop()
    print("EMPTY STACK")
    return None

add_stack("BOX A")
add_stack("BOX B")
add_stack("BOX C")
print(mystack)

x = delete_stack()
print(mystack)