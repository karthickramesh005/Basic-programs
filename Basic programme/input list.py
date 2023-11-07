user_input = input("Enter a list of numbers separated by commas: ")

# Split the input string into a list using the comma as the delimiter
user_list = user_input.split(",")

# Convert the list of strings to a list of integers (or floats if needed)
try:
    user_list = [int(item) for item in user_list]
except ValueError:
    print("Invalid input. Please enter a list of numbers separated by commas.")

# Now 'user_list' contains the list of numbers entered by the user
print("User's list:", user_list)
