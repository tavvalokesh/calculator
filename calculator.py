def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b  

def new():
    x = int(input("Enter a number: "))
    exit = False

    while not exit:
        q = {"+": add, "-": subtract, "*": multiplication, "/": division}
        
        print("Available operations:")
        for i in q:
            print(i)
            
        p = input("Pick an operation: ")
        y = int(input("Enter another number: "))
        
        l = q[p]
        t = l(x, y)
        print("Result:", t)
        
        user = input("Enter 'y' to continue, 'n' to stop, or 'u' to start new: ")
        if user.lower() == "n":
            exit = True
        elif user.lower() == "u":
            print("new \n")
            return new()   
        elif user.lower() == "y":
            x = t          


new()
