# - File: test.py
#   - series of tests to check other files are working as intended


from pokeranalysissuite.hand import parsecard

# test if function parsecard in hand.py is giving desired outputs
print(
    parsecard("7h") == [5, 2]
    and parsecard("Ac") == [12, 0]
    and parsecard("Qd") == [10, 1]
)


# template function
def templatefunction() -> None:
    """
    Summary line.

    Extended description of function.

    >>> templatefunction(examplearguments)
    exampleoutput

    Arguments
    ---------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    int
        Description of return value

    """

    return
