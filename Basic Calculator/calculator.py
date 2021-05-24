def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operators={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
from art import logo
def calculator():
    to_continue=True
    print(logo)
    num1=int(input("What is the first number ?"))
    while to_continue:
        for operator in operators:
            print(operator)

        operation_symbol=input("Pick an operation from the above given list. : ")
        num2=int(input("What is the next number ?"))
        answer=operators[operation_symbol](num1,num2)

        print("{} {} {} = {}".format(num1,operation_symbol,num2,answer))

        to_continueL=input(f"Do you want to continue calculations on {answer}? Type 'y' if yes, or 'n' to start a new calculation: ").lower()
        if to_continueL=="n":
            to_continue=False
            calculator()
        elif to_continueL=="y":
            to_continue=True    
            num1=answer  
        else:
            return

calculator()