def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    lst = list(phrase)

    revered_lst = lst[::-1]

    return ('').join(revered_lst)