def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    lowercase_phrase = phrase.lower()
    vowels = 'aeiou'
    obj = {}
    for char in lowercase_phrase:
        # print(char)
        if char in vowels:
            
            if char in obj:
                obj[char] += 1
                
            else:
                obj[char] = 1

              
    return obj


