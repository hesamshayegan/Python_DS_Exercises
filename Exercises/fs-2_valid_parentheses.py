def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    seen = []

    for item in parens:
        if item == '(':
            seen.append(item)
        elif item == ')':
            if '(' in seen:
                seen.pop()
            else:
                seen.append(')')

    if len(seen) == 0:
        return True
    
    else:
        return False
    
valid_parentheses("(()())")