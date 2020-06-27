# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")
  size=get_size()
  drink_type=get_drink_type()
  print("Alright, that\'s a "+ size + " "+ drink_type + "!")
  
  another_drink = input(" Would you like to order another drink? ")
  if (another_drink == "yes"):
    coffee_bot()
    
  else:
    print("Ok thank you for your order")

  name = input('Can I get your name please?')
  print ("Thanks, "+ name + "! Your drink(s) will be ready shortly")

#Defining a function call get_size that asks the user for the size of their drink
#and force them to choose again
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n>')
  if (res == 'a'):
    return 'Small'
  elif (res == 'b'):
    return 'Medium'
  elif (res == 'c'):
    return 'Large'
  else:
    print_message()
    return get_size()
#Warning message to user that they didn't enter the write choice
def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response')
#function that will ask the user for their drink order
def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>')
  if (res == 'a'):
    return 'Brewed Coffee'
  elif (res == 'b'):
    return 'Mocha'
  elif (res == 'c'):
    return order_latte()
  else:
    print_message()
    return get_drink_type()

#if user chooses a Latte
def order_latte():
  res = input('What kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>')
  if (res == 'a'):
    return 'latte'
  elif (res == 'b'):
    return 'Non-fat latte'
  elif (res == 'c'):
    return 'Soy late'
  else:
    print_message()
    return order_latte()

# Call coffee_bot()!

coffee_bot()
