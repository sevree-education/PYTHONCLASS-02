myqueue = []

def add_queue(x):
    myqueue.append(x)

def delete_queue():
    if myqueue:
        return myqueue.pop(0)
    print("QUEUE IS EMPTY")
    return None

add_queue({"name" : "OUSSAMA", "ticket": 1})

add_queue({"name" : "SALIM", "ticket": 2})

add_queue({"name" : "MOHA", "ticket": 3})

add_queue({"name" : "JACK", "ticket": 4})
print("BEFORE\n")
print(myqueue)
print("AFTER\n")
x = delete_queue()
print(myqueue)