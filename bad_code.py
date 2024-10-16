# bad_code.py

API_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"  # Hardcoded secret (Stripe API key)

def example_function():
  print("This is an example function")
  x = 42  # Unused variable (Linting issue: F841)
  print("Using the API key:", API_KEY)

example_function()  # Function call with no newline after (Linting issue: W292)
