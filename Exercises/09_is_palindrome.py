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
    lowered_phrase = phrase.lower()

    lowered_phrase_nospace = lowered_phrase.replace(" ","")

    to_list = list(lowered_phrase_nospace)
    to_list.reverse()
    reversed_phrase = "".join(to_list)
    
    if reversed_phrase == lowered_phrase_nospace:
        return True
    else: return False
    
    