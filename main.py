try:
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    
    print("What operation do you want to perform?: Addition + \n Subtraction - \n Division / \n Multiplication * ")
    
    operation = input("Enter the operation:")
    
    match operation:
        case "+":
            print (f"The result is {a + b}")
        case "-":
            print (f"The result is {a - b}")
        case "*":
            print (f"The result is {a * b}")
        case "/":
            print (f"The result is {a / b}")
        case default:
            print("There was a error!")
     
            
    
except:
    print("Enter a Valid input!")