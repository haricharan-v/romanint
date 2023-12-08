def romanToInt(s: str) -> int:
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}

    integer = 0

    try:
        # iterate over the characters in the given Roman numeral string
        for i in range(len(s)):
            # check if the current digit in the Roman numeral is smaller than the next one
            if i < len(s) - 1 and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
                # subtract the value of the current Roman numeral digit from the integer
                integer -= roman_numerals[s[i]]
            else:
                # add the value of the current Roman numeral digit to the integer
                integer += roman_numerals[s[i]]
    except KeyError:
        print("Please enter a proper Roman numeral.")
        return None  # You can choose how to handle this case (e.g., return a special value or raise an exception)

    return integer

while True:
    user_input = input("Enter a Roman numeral: ")
    result = romanToInt(user_input)
    if result is not None:
        print(f"The integer equivalent of {user_input} is {result}.")

    try_again = input("Do you want to try again? (yes/no): ")
    if try_again.lower() != 'yes':
        break

    print()  # Add a newline for better formatting
