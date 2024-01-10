# Exception Handlers are placed in this file. Each handle ValueErrors for incorrectly typed options from the user.

# This function is used to check whether Y or N was entered for Yes/No questions. It will raise and catch a ValueError exception if any value other than Y/N is entered
def value_checker_YN(value):
  while value:
    try:
      if value == 'Y':
        return value
      elif value == 'N':
        return value
      else:
        raise ValueError ("Value entered was not Y or N")
    except ValueError:
        value = input("Please Enter Y or N: ").upper()
        value_checker_YN(value)

# This function is used to check whether the menu option entered is a listed option or not. It will raise and catch a ValueError if not.
def value_checker_options(value):
  while value:
    try:
      if value == 'i':
        return value
      elif value == 'r':
        return value
      elif value == 'v':
        return value
      elif value == 's':
        return value
      elif value == 't':
        return value
      elif value == 'q':
        return value
      else:
        raise ValueError ("Value entered was not a listed option")
    except ValueError:
        value = input("Please Enter a letter from the options listed above: ").lower()
        value_checker_options(value)