import random
import string

def generate_password(length, lowercase=True, uppercase=True, numbers=True, symbols=True):
  """Generates a random password based on user-specified options."""
  characters = ""
  if lowercase:
    characters += string.ascii_lowercase
  if uppercase:
    characters += string.ascii_uppercase
  if numbers:
    characters += string.digits
  if symbols:
    characters += string.punctuation

  if not (lowercase or uppercase or numbers or symbols):
    characters += string.ascii_lowercase + string.digits

  password = ''.join(random.sample(characters, length))
  return password

def main():
  while True:
    try:
      length = int(input("Enter desired password length (minimum 8 characters): "))
      if length < 8:
        print("Password length must be at least 8 characters.")
      else:
        break
    except ValueError:
      print("Invalid input. Please enter a number.")

  complexity = {
    "lowercase": input("Include lowercase letters (y/n)? ").lower() == "y",
    "uppercase": input("Include uppercase letters (y/n)? ").lower() == "y",
    "numbers": input("Include numbers (y/n)? ").lower() == "y",
    "symbols": input("Include symbols (y/n)? ").lower() == "y",
  }

  password = generate_password(length, **complexity)
  print(f"Your generated password is: {password}")

if __name__ == "__main__":
  main()
