def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowels = {'o', 'a', 'e', 'u', 'i'}
    lowered_phrase = phrase.lower()
    res = {}

    for char in lowered_phrase:
        if char in vowels:
            if char not in res:
                res[char] = 1
            else:
                res[char] += 1

    return res