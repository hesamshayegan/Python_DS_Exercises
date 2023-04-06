def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # to_list = [char for char in phrase]
    to_list = list(phrase)
    to_list.reverse()
    reversed_phrase = "".join(to_list)
    return reversed_phrase