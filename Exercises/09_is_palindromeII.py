def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    removed_space = ""
    for i in range(len(phrase)):
        if phrase[i] != " ":
            removed_space += phrase[i]

    reversed_phrase = ""
    for i in range(len(phrase)-1, -1, -1):
        if phrase[i] != " ":
            reversed_phrase += phrase[i]

    return reversed_phrase.lower() == removed_space.lower()