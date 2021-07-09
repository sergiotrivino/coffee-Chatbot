# Defining the functions
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  cup = user_cup()
  drink_prep = iced_or_hot()
  print(f"Alright, that's a {size} {drink_type}!")
  print(f"You'll get your {drink_type}, {drink_prep} as you requested, and in your {cup}.")
  name = input("Can I get your name please? \n")
  print(f"Thanks, {name}! Your drink will be ready shortly.")

def print_message():
  print("I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.") 

def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n")
  if res == "a":
    return "latte"
  elif res == "b":
    return "non-fat latte"
  elif res == "c":
    return "soy latte"
  else :
    print_message()
    return order_latte()

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == "a":
    return "small"
  elif res == "b":
    return "medium"
  elif res == "c":
    return "large"
  else:
    print_message()
    return get_size()

def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n")
  if res == "a":
    return "brewed coffee"
  elif res == "b":
    return "mocha"
  elif res == "c":
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def user_cup():
  res = input("What type of cup would you like? \n[a] Plastic Cup \n[b] My own reusable cup \n")
  if res == "a":
    return "plastic cup"
  elif res == "b":
    return "own cup"
  else: 
    print_message()
    return user_cup()

def iced_or_hot():
  res = input("How would you like your drink? \n[a] Hot \n[b] Iced \n")
  if res == "a":
    return "hot"
  elif res == "b":
    return "icedd"
  else:
    print_message()
    return iced_or_hot()

# Call coffee_bot()!
coffee_bot()
