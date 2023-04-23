from typing import List, Optional

from strplus.cases import *


def to_list(text: str) -> List[str]:
    """

    Converts a string to a list of strings, where each word is a separate element in the list.

    Args:
        text (str): The input string.

    Returns:
        List[str]: A list of strings, where each word in the input string is a separate element in the list.

    !!! Example "Converting a string to a list"
        This example shows how to use `to_list()` to convert a string to a list.

        === "Example 1"
            ```python
            to_list('hello world')
            ```
            ['hello', 'world']

        === "Example 2"
            ```python
            to_list('HelloWorld')
            ```
            ['Hello', 'World']

        === "Example 3"
            ```python
            to_list('some-mixed_string With spaces_underscores-and-hyphens')
            ```
            ['some', 'mixed', 'string', 'With', 'spaces', 'underscores', 'and', 'hyphens']

        === "Example 4"
            ```python
            to_list('123abc')
            ```
            ['123abc']

    Tip: Use tips
        - If you need to convert a string to a list of integers or floats, you can use list comprehension to convert each element to the desired type.
        - If you need to remove duplicates from the list, you can convert it to a set and then back to a list.

    Info: Important
        - For best results, avoid using punctuation or non-alphanumeric characters in the input string.
        - This function uses regular expressions to identify words in the input string.

    """
    text = text.strip()

    if not text:  # If the input string is empty or only whitespace, return an empty list
        return []

    # Remove any non-alphanumeric characters and split the string into words
    word_list = sum([re.findall(r"[a-zA-Z0-9]+", word) for word in re.sub("([A-Z][a-z]+)", r"_\1", re.sub("([A-Z]+)", r"_\1", text)).split()], [])

    return word_list


def get_separator(input_string, separator_list: Optional[List[str]] = None):
    """
    
    Returns the most frequent separator character in an input string.

    Args:
        input_string (str): The input string to analyze.
        separator_list (Optional[List[str]], optional): A list of separator characters to consider. Defaults to None.

    Returns:
        Union[str, None]: The most frequent separator character in the input string, or None if there are no separators.

    !!! Example "Finding the most frequent separator character"
        This example shows how to use `get_separator()` to find the most frequent separator character in a string.

        === "Example 1"
            ```python
            get_separator("John, Doe; Jane | Doe")
            ```
            ','

        === "Example 2"
            ```python
            get_separator("John Doe Jane Doe")
            ```
            " "

        === "Example 3"
            ```python
            get_separator("A/B/C")
            ```
            '/'

    Tip: Use tips
        - If you want to specify a custom list of separator characters, pass it as the `separator_list` argument.
        - If you want to find the second most frequent separator character (or any other rank), you can modify the code to return a list of separator characters sorted by frequency.

    Info: Important
        - The function assumes that any character that appears at least once in the input string is a potential separator.
        - The function uses a common list of separator characters by default, but this list may not be appropriate for all types of input strings.
        - The function returns None if there are no separators in the input string.
    
    """   
    
    # Common separator list by priority!
    common_separators = [",", ";", "|", " ", "\t", ":", "/", "\\", "\n"]

    # Setting the separator list
    separator_list_target = separator_list if separator_list is not None and len(separator_list) > 0 else common_separators

    sep_frequency = {sep: input_string.count(sep) for sep in separator_list_target if input_string.count(sep) > 0}
    most_frequent_separator = None

    if len(sep_frequency) > 0:
        max_value = max(sep_frequency.values())
        max_frequency = [key for key, value in sep_frequency.items() if value == max_value]
        sep_sorted_by_priority = sorted(max_frequency, key=lambda x: separator_list_target.index(x))
        most_frequent_separator = sep_sorted_by_priority[0]

    return most_frequent_separator
