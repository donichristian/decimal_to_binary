# Define a function to convert a decimal number to binary
def decimal_to_binary(num):
    """
    Convert a decimal number to binary and print the binary representation.
    
    Parameters:
    num (int): The decimal number to be converted to binary.
    
    Returns:
    None
    """
    # Check if the number is greater than 1
    if num > 1:
        # Recursively call the function with the integer division of the number by 2
        decimal_to_binary(num // 2)
    # Print the remainder of the number divided by 2, without creating a new line
    print(num % 2, end='')

# Add user input and variable assignment
decimal_num = int(input("Enter a decimal number: "))

# Call the function with the user input as the argument and print the binary representation
decimal_to_binary(decimal_num)

# The big O notation of the given function decimal_to_binary is O(log n),
# where n is the input decimal number.

# step-by-step flow for the function `decimal_to_binary` with the input `num=10`:

# Step 1: 10 / 2 = 5 (Quotient)
# Step 2: Remainder = 0
# Step 1: 5 / 2 = 2 (Quotient)
# Step 2: Remainder = 1
# Step 1: 2 / 2 = 1 (Quotient)
# Step 2: Remainder = 0
# Step 1: 1 / 2 = 0 (Quotient)
# Step 2: Remainder = 1