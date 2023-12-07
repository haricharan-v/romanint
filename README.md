# Roman to Integer Converter

This Python script converts a given Roman numeral to its integer equivalent.

## Usage

To use this script, follow these steps:

1. Run the script using a Python interpreter.

   ```bash
   python roman_to_integer.py
   ```

2. Enter a Roman numeral when prompted.

   ```plaintext
   Enter a Roman numeral: XIV
   ```

3. View the result.

   ```plaintext
   The integer equivalent of XIV is 14.
   ```

## Input (STDIN)

The script takes a Roman numeral as input from the user through the standard input (STDIN).

## Output (STDOUT)

The script outputs the integer equivalent of the provided Roman numeral to the standard output (STDOUT).

## Error Handling

If an invalid Roman numeral is entered, the script will print an error message and return `None`. You can customize the error handling based on your requirements.

## Example

```python
# Example usage:
user_input = input("Enter a Roman numeral: ")
result = romanToInt(user_input)
if result is not None:
    print(f"The integer equivalent of {user_input} is {result}.")
```

## Note

- The script uses a dictionary (`roman_numerals`) to map Roman numerals to their corresponding integer values.
- It iterates through the input Roman numeral and calculates the integer equivalent.
- The `try-except` block is used to handle the case of an invalid Roman numeral (e.g., containing characters not in the `roman_numerals` dictionary).
- Feel free to customize the error handling or modify the script to suit your specific needs.

**Note:** Ensure that you have a proper Python environment set up to run the script.
