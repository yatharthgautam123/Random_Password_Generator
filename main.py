import random
import string


def generate_password(length=12):
  """
    Generate a random password of specified length.

    Parameters:
    length (int): Length of the password to generate. Default is 12.

    Returns:
    str: Randomly generated password.
    """
  # Define the pool of characters to choose from
  characters = string.ascii_letters + string.digits + string.punctuation
  # Generate password by choosing random characters from the pool
  password = ''.join(random.choice(characters) for i in range(length))
  return password


def main():
  """
    Main function to prompt user input and generate passwords.
    """
  try:
    # Prompt user for the number of passwords to generate
    num_passwords = int(
        input("How many passwords would you like to generate? "))
    # Prompt user for the length of each password
    password_length = int(input("Enter the length of each password: "))
    # Generate and print each password
    for i in range(num_passwords):
      password = generate_password(password_length)
      print("Password {}: {}".format(i + 1, password))
  except ValueError:
    # Handle invalid input errors
    print(
        "Please enter valid integer values for the number of passwords and password length."
    )


if __name__ == "__main__":
  main()
