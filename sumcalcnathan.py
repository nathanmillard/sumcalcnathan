# Program Name: SumCalculatorYourName
# Description: Calculates the sum of all integers from 0 up to a user-defined number.

def main():
    # Prompt the user to enter a positive integer
    user_input = input("Enter a positive integer: ")
    
    # Convert the input string to an integer
    target_number = int(user_input)
    
    # Initialize the running total sum to 0
    total_sum = 0
    
    # Initialize the loop counter variable to 0
    counter = 0
    
    # Loop execution continues as long as counter is less than or equal to target_number
    while counter <= target_number:
        # Add the current counter value to the running total
        total_sum += counter
        
        # Increment the counter by 1 to move to the next integer
        counter += 1
        
    # Output the final calculated sum to the console
    print(f"The sum of all integers from 0 to {target_number} is: {total_sum}")

# Standard boilerplate to execute the main function
if __name__ == "__main__":
    main()
