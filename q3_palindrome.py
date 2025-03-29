"""
Q3:  Given a string, determine if it's a palindrome after removing all 
non-alphanumeric  characters. A character is alphanumeric if 
it's either a letter or a number.
"""

def is_palindrome(input_string: str) -> bool:
    input_string = input_string.lower()
    alphanumeric_string = "".join([char for char in input_string if char.isalnum()])
    return alphanumeric_string == alphanumeric_string[::-1]

def is_palindrome_two_pointers(input_string: str) -> bool:
    """Checks if a string is a palindrome using two pointers."""
    input_string = input_string.lower()
    left, right = 0, len(input_string) - 1

    while left < right:
        while left < right and not input_string[left].isalnum():
            left += 1
        while left < right and not input_string[right].isalnum():
            right -= 1

        if input_string[left] != input_string[right]:
            return False
        left += 1
        right -= 1

    return True  # Empty string and all other cases.  

if __name__ == "__main__":
    input_string = "a dog! a panic in a pagoda."
    #print(is_palindrome(input_string))
    print(is_palindrome_two_pointers(input_string))
    print(is_palindrome_two_pointers("abbabba"))
    print(is_palindrome_two_pointers("a"))
    print(is_palindrome_two_pointers("A Best Day"))
    print(is_palindrome_two_pointers("!@#$%^&*()"))
