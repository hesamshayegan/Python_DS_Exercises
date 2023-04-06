def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    new_list =[]

    for item in lst:
            if  (item != 0 and item != '' and item and 
            item != False and item != None and 
            item != [] and item != () and item!= {}):
                new_list.append(item)
    return new_list

