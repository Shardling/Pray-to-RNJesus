import random
import time
import sys
from simple_chalk import chalk
colour_text_1 = "first"
colour_text_2 = "second"
colour_text_3 = "operation"
colour_text_4 = "congrats"
colour_text_5 = "high"
colour_text_6 = "low"
colour_text_7 = "number"

def slow_text_time(str, ms):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(ms)
def slow_text005(str):
  slow_text_time(str, 0.05)
def slow_text003(str):
  slow_text_time(str, 0.03)
def slow_text002(str):
  slow_text_time(str, 0.02)
def explain_1():
  slow_text003("Input a number between 1 and 50.\nA random number is generated between these numbers.\nyour guess if incorrect will tell you if it is too high or too low.\nIf you input a number outside the range you will be prompted to input a number inside the range.\n")
def explain_2():
  slow_text003("Input 2 numbers and then an operation(+, -, *, /).\nIt will use the operation and make a total number.\nA random number will be pulled in a range of 0 to 100.\nA prompt will tell you  if your guess is too high or too low.\nIn which case you will be able to input all fields again.\n")
def explain_3():
  slow_text002("Input a number, range is not given for this one. You must complete this within 31 guesses or you will need to start from the beginning, including a new random number\n")
def menu():
  slow_text005("Choose quiz 1, 2, or 3.\nThe larger the number, the higher the dificulty.\n")
  quiz_choice = input("")
  if quiz_choice == "1":
    explain_1()
    Quiz_1()
  elif quiz_choice == "2":
    explain_2()
    Quiz_2()
  elif quiz_choice == "3":
    explain_3()
    Quiz_3()
  else:
    menu()
def Quiz_1():
  Random = random.randint(0, 50)
  while True:
    Question_1 = input("")
    Split_1 = Question_1.rsplit(".")
    Question_1 = Split_1[0]
    if Question_1.isdigit() == True:
      Question_1 = int(Question_1)
      if Question_1 == Random:
        slow_text005({chalk.greenBright("Correct\n")})
        menu()
      elif Question_1 >= 51:
        slow_text003("please input a number between 0 and 50\n")
      elif Question_1 >= Random:
       slow_text005(f"too {chalk.red(colour_text_5)}\n")
      else:
        slow_text005(f"too {chalk.red(colour_text_6)}\n")
    else:
      slow_text003("please input a number between 0 and 50\n")
def Quiz_2():
  Random_2 = random.randint(0, 100)
  while True:
    slow_text005(f"input {chalk.blue(colour_text_1)} number\n")
    num_1 = input("")
    slow_text005(f"input {chalk.blue(colour_text_2)} number\n")
    num_2 = input("")
    try:
      num_1 = float(num_1)
      num_2 = float(num_2)
      slow_text005(f"input {chalk.magenta(colour_text_3)} (+, -, *, /)\n")
      operation = input("")
      if operation == "+" or operation == "-" or operation == "*" or operation == "/":
        formula_1 = num_1 + num_2
        formula_2 = num_1 - num_2
        formula_3 = num_1 * num_2
        if num_2 > 0:
          formula_4 = num_1 / num_2
      if operation == "+":
        print(formula_1)
        if formula_1 == Random_2:
          slow_text005(f"{chalk.greenBright(colour_text_4)}\n")
          menu()
        elif formula_1 >= Random_2:
          slow_text005(f"too {chalk.red(colour_text_5)}\n")
        else:
          slow_text005(f"too {chalk.red(colour_text_6)}\n")
      elif operation == "-":
        print(formula_2)
        if formula_2 == Random_2:
          slow_text005(f"{chalk.greenBright(colour_text_4)}\n")
          menu()
        elif formula_2 >= Random_2:
          slow_text005(f"too {chalk.red(colour_text_5)}\n")
        else:
          slow_text005(f"too {chalk.red(colour_text_6)}\n")
      elif operation == "*":
        print(formula_3)
        if formula_3 == Random_2:
          slow_text005(f"{chalk.greenBright(colour_text_4)}\n")
          menu()
        elif formula_3 >= Random_2:
          slow_text005(f"too {chalk.red(colour_text_5)}\n")
        else:
          slow_text005(f"too {chalk.red(colour_text_6)}\n")
      elif operation == "/" and num_2 >= 1:
        print(formula_4)
        if formula_4 == Random_2:
          slow_text005(f"{chalk.greenBright(colour_text_4)}\n")
          menu()
        elif formula_4 >= Random_2:
          slow_text005(f"too {chalk.red(colour_text_5)}\n")
        else:
          slow_text005(f"too {chalk.red(colour_text_6)}\n")
    except ValueError:
      Quiz_2()
def Quiz_3():
  while True:
    Exit = input("Would you like to exit to the menu?\n")
    if Exit.lower() == "yes":
      menu()
    else:
      Random_3 = random.randint(-1000000000, 1000000000)
      for i in range(31):
        slow_text003(f"Input {chalk.magenta(colour_text_7)}\n")
        Question_2 = input("")
        try:
          Question_2 = float(Question_2)
          if Question_2 == Random_3:
            slow_text003({chalk.green(colour_text_4)})
            menu()
          elif Question_2>= Random_3:
            slow_text005(f"too {chalk.red(colour_text_5)}\n")
            print("You have used" ,chalk.blue(i + 1) , "guesses")
          else:
            slow_text005(f"too {chalk.red(colour_text_6)}\n")
            print("You have used" ,chalk.blue(i + 1) , "guesses")
        except ValueError:
          print("You have used" ,chalk.blue(i + 1) , "guesses")
          slow_text003("")
      Quiz_3()
menu()
