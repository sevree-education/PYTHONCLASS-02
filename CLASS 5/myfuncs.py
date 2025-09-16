def add(x, y):
    return x + y

def SayHelloWorld():
    print("Hello World")

def greet(name, language="en"):
    if language == "en":
        print("Hello", name)
    elif(language == "fr"):
        print("Salut", name)
    elif(language == "ar"):
        print("Merhaban", name)
    else:
        print("Invalid Language")