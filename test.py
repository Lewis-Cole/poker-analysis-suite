# - File: test.py
#   - series of tests to check other files are working as intended


from pokeranalysissuite.hand import parsecard, Hand

# test if function parsecard in hand.py is giving desired outputs
print(
    str(
        parsecard("7h") == [5, 2]
        and parsecard("Ac") == [12, 0]
        and parsecard("Qd") == [10, 1]
    )
    + " : function parsecard in hand.py"
)

# test if Hand class method cards is giving desired outputs
h1 = Hand("7hAcQd9c9d")
h2 = Hand("7d8dQdTd9d9cJd")
h3 = Hand("7h8cJdTc9dAh2s")
h4 = Hand("7h4c3dTc5dAh2s")

print(
    str(
        h1.cards == [[5, 2], [12, 0], [10, 1], [7, 0], [7, 1]]
        and h2.cards == [[5, 1], [6, 1], [10, 1], [8, 1], [7, 1], [7, 0], [9, 1]]
        and h3.cards == [[5, 2], [6, 0], [9, 1], [8, 0], [7, 1], [12, 2], [0, 3]]
        and h4.cards == [[5, 2], [2, 0], [1, 1], [8, 0], [3, 1], [12, 2], [0, 3]]
    )
    + " : method cards in Hand class in hand.py"
)

print(
    str(
        h1.teststraight(h1.rankcount) == (False, None)
        and h2.teststraight(h2.rankcount) == (True, 10)
        and h3.teststraight(h3.rankcount) == (True, 9)
        and h4.teststraight(h4.rankcount) == (True, 3)
    )
    + " : function teststraight in Hand class in hand.py"
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
