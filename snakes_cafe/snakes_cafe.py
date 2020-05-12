from textwrap import dedent

def intro():
  print(dedent(f"""
  {"*"*38}
  **    Welcome to the Snakes Cafe!   **
  **    Please see our menu below.    **
  **
  ** To quit at anytime, type \"quit\" **
  {"*"*38}
  """))

menu_dict = {
  "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
  "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
  "Desserts": ["Ice Cream", "Cake", "Pie"],
  "Drinks": ["Coffee", "Tea", "Unicorn Tears"],
}

def menu():
  for key, value in menu_dict.items():
    print(f"{key}")
    print("-"*10)
    for i in value:
      print(i)
    print("")

def prompt():
  print(f"""{"*"*38}
  ** What would you like to order? **\n{"*"*38}
  """)
  order = {}
  while True:
    answer1 = str(input())
    
    if answer1 == 'quit':
      break
    
    if answer1 not in order:
      order[answer1] = 0

    order[answer1] += 1

    print(f"\n** {order[answer1]} orders of {answer1} have been added to your meal **\n")


def main():
  intro()
  menu()
  prompt()

if __name__ == "__main__":
    main()