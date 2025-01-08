def ft_filter(function, iterable):
    """
    ft_filter is a recoded version of the filter built-in function.
    The description in the original documentation is : Return an iterator \
    yielding those items of iterable for which function(item) is true.
    If function is None, return the items that are true.
    """

    if (function):
        return (item for item in iterable if function(item))
    else:
        return (item for item in iterable if item)
