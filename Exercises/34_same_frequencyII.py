def create_freq(str):

    freq = {}

    for char in str:
        freq[char] = freq.get(char, 0) + 1

    return freq


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    if create_freq(str(num1)) == create_freq(str(num2)):
        return True
    
    return False