#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def sub(n1, n2):
    return n1- n2
    
#Multiply
def mul(n1, n2):
    return n1 * n2

#Divide
def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    num1 = float(input("what's the first number? "))
    for symbol in operations:
        print(symbol)
    ask_user = True
    while ask_user:
        op_sym1 = input("Pick an operation from above: ")
        num2 = float(input("what's the next number? "))

        calc = operations[op_sym1]
        answer = calc(num1 , num2)
        print(f"{num1} {op_sym1} {num2} = {answer}")

        ask_user = input("Do u want to continue? type 'y' for yes or 'n' for new calculation : ")
        if ask_user == "y":
            num1 = answer
        else:
            ask_user = False
            calculator() #recursion
calculator()
