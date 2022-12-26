# - File: test.py
#   - series of tests to check other files are working as intended


from pokeranalysissuite.hand import parsecard, Hand

# test if function parsecard in hand.py is giving desired outputs
print(
    parsecard("7h") == [5, 2]
    and parsecard("Ac") == [12, 0]
    and parsecard("Qd") == [10, 1]
)

# test if Hand class method cards is giving desired outputs
print(
    Hand("7hAcQd9c9d").cards == [[5, 2], [12, 0], [10, 1], [7, 0], [7, 1]]
    and Hand("7dAdQd9c9d").cards == [[5, 1], [12, 1], [10, 1], [7, 0], [7, 1]]
    and Hand("7h8cJdTc9d").cards == [[5, 2], [6, 0], [9, 1], [8, 0], [7, 1]]
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
