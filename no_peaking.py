
# 1. Note the variable account_types, the list of account types.
login_types = ["admin", "user", "guest"]
# 2. Create a function called gatekeeper that returns the following error message strings in the following scenarios:
def gatekeeper(login):
  # For “admin”:
  if login == "admin":
    # program says “You have the privileges.”
    return "You have the privileges"
    # For “user”:
  if login == "user":
    # program says “You have limited privileges.”
    return "You have limited privileges."
    # For “guest”:
  if login == "guest":
    # program says “You have no privileges.”
    return "You have no privileges."
# 3. Call your function with a string and print what it returns. 
print(gatekeeper("admin"))
# 4. How could this code be improved? Make it better. Think about what other scenarios you should cover in your if logic.
 
def better_gatekeeper(login):
  # For “admin”:
  if login == "admin":
    # program says “You have the privileges.”
    return "You have the privileges"
    # For “user”:
  if login == "user":
    # program says “You have limited privileges.”
    return "You have limited privileges."
    # For anything else, including “guest”:
    # You could argue this makes it less aware of the different login types better_gatekeeper expects. You could just add this else statement after the "if "guest" check, but then you're duplicating code. Tomayto, tomahto.
  else:
    # program says “You have no privileges.”
    return "You have no privileges."
# 5. Create a function called check_balance that takes one parameter, loan_balance.
def check_balance(loan_balance):
  # 6. If loan_balance is zero or more, it says “you don’t owe any money”
  if loan_balance >= 0:
    return "You don’t owe any money!"
  else:
    # 7. If loan_balance is negative, it  says “you owe $X” where X is the amount
    return "You owe: " + str(loan_balance)

# 8. Call your function with a negative and positive number and print what it returns.
print(check_balance(-300))
print(check_balance(800))
