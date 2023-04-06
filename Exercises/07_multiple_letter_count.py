def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    count = 0
    phrase_freq = {}

    for char in phrase:
        if char in phrase_freq:
            count += 1
        
            phrase_freq[char] = count
        else:
            count = 1
            
            phrase_freq[char] = count

    return phrase_freq

