def delete_all_occurrences(s, char_to_delete):
    """
    This function takes in a string and a character,
    and returns a version of the string that has all
    the occurrences of the character removed.
    >>> delete_all_occurrences('This is a test', 't')
    'This is a es'
    >>> delete_all_occurrences('Summer is here!', 'e')
    'Summr is hr!'
    >>> delete_all_occurrences('---0---', '-')
    '0'
    >>> delete_all_occurrences('', 'a')
    ''
    """
    result = ''
    for i in range(len(s)):
        current_char = s[i]
        if current_char != char_to_delete:
            result += current_char
    return result

