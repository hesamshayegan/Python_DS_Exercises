def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    list = [] 
    if to_swap.islower() == True:
        for char in phrase:
            if to_swap == char:
                list.append(char.upper())
            elif char == to_swap.upper():
                list.append(char.lower())    
            else:
                list.append(char)
        return "".join(list)
    
    elif to_swap.isupper() == True:
        
        for char in phrase:
            if to_swap == char:
                list.append(char.lower())
            if char == to_swap.lower():
                list.append(char.upper())    
            else:
                list.append(char)
        return "".join(list)
    
