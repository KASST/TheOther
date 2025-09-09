"""
A collection of utility functions for string manipulation.
"""

def reverse_and_capitalize(text: str) -> str:
    """
    Reverses a string and capitalizes the first letter.

    This function takes a string as input, reverses its order,
    and then capitalizes the first letter of the reversed string.

    Args:
        text: The input string to process.

    Returns:
        The processed string.
        
    Example:
        >>> reverse_and_capitalize("hello")
        'Olleh'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    reversed_text = text[::-1]
    return reversed_text.capitalize()