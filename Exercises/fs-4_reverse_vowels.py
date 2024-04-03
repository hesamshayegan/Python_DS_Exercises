def reverse_vowels(phrase):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    left = 0
    right = len(phrase) - 1
    vowels = 'aieouAIEOU'

    s = list(phrase)

    while left<right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] in vowels:
            right -= 1
        elif s[right] in vowels:
            left += 1

        else:
            left += 1
            right -= 1

    return "".join(s)

reverse_vowels("Hello!")