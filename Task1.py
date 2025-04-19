def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break


firstNo = inputNumber("Enter the first number :")
print(firstNo)

secondNo = inputNumber("Enter the second number :")
print(secondNo)

addition = firstNo + secondNo
subtraction = firstNo - secondNo
multiplication = firstNo * secondNo
division = firstNo / secondNo

print("Addition: ", addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Division: ", division)