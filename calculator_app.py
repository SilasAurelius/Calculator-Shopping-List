def add(num1, num2):   
    return num1 + num2

def sub(num1, num2):
    return num1 - num2 
  
def mult(num1, num2):
    return num1 * num2

def dvid(num1, num2):
    return num1 // num2
    
while True:
    try:
        #Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError as ERROR:
            print("INVALID INPUT!\nTry again. ")
            continue
    
    opt = input("Select function below:\nSelect: + for addition\nSelect: - for subtraction\nSelect: / for divison\nSelect: * for multiplication\nInput function: ")
        
    if opt == '+':
       print(f"{num1} + {num2} = {add(num1, num2)}") 
    elif opt == '-':
        print(f"{num1} - {num2} = {sub(num1, num2)}")
    elif opt == '*':
        print(f"{num1} * {num2} = {mult(num1, num2)}")
    else:
        try:
            opt == '/'
            print(f"{num1} / {num2} = {dvid(num1, num2)}")
        except ZeroDivisionError:
            print("Cannot divide by zero, try again.")
            continue

#Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.