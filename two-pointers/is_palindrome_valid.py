"""
Is Palindrome Valid
Is a sequence os characters that reads the same forward and backward

Intput: s = "a dog! a panic in a pagoda.'
Output: True

--> Ignoring non-aplhanumeric
--> If not, the string is not a palindrome: return False

[fera ed e aref]
"""

def is_palindrome_valid(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left] != s[right]:
            return False
        left += 1 
        right -= 1
            
    return True

"""
Interview Tips
Confirm before using significant in-built functions
Before using an in-built function that simplifies the implementation, ask
the interview if it's okay to use it, or if they would prefer you implement
it yourself.

"""

def my_isalnum(input_string):
    """
    Checks is a string is alphanumeric.
    A string is considered alphanumeric if all characters is the string
    are alphabetic or numeric, and ther is at least one character.
    An empty string is not consider alphanumeric
    
    Args:
        input_string: The string to be checked.
    
    Returns:
        True if the string is alphanumeric, False otherwiser
    """ 
    if not input_string:
        return False
    for char in input_string:
        is_alpha = 'a' <= char.lower() <= 'z'
        is_digit = '0' <= char <= "9"
            
        if not (is_alpha or is_digit):
            return False
    return True