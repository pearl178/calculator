#Add
def add(n1,n2):
  return n1+n2
#Subtract
def subtract(n1,n2):
  return n1-n2
#Multiply
def multiply(n1,n2):
  return n1*n2
#Divide
def divide(n1,n2):
  return n1/n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculator():
  import art
  print(art.logo)
  end_calculation = False
  num1 = float(input("What's the first number? "))
  while not end_calculation:
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation from the symbols above: ")
    num2 = float(input("What's the second number? "))
    function = operations[operation_symbol]
    answer = function(num1,num2)
    print(f"{num1}{operation_symbol}{num2}={answer}")
    ask_user = input("Type 'yes' to continue with the answer or 'no' to start a new calculation:\n")
    if ask_user=='no':
      end_calculation = True
      calculator()
    else:
      num1 = answer

calculator()
