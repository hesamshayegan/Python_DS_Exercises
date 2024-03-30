def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    res = ""
    for i in range(len(phrase)):
        if phrase[i] == to_swap.lower():
            res += to_swap.upper()
        elif phrase[i] == to_swap.upper():
            res += to_swap.lower()
        else:
            res += phrase[i]
    print(res)
    return res