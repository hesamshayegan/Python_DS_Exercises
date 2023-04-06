def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    cap_phrase = phrase.replace(phrase[0],phrase[0].upper(),1)
    return cap_phrase

