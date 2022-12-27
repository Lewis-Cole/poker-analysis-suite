# - File: test.py
#   - series of tests to check other files are working as intended


from pokeranalysissuite.hand import parsecard, Hand

# test if function parsecard in hand.py is giving desired outputs
print(
    parsecard("7h") == [5, 2]
    and parsecard("Ac") == [12, 0]
    and parsecard("Qd") == [10, 1],
    ": function parsecard in hand.py",
)

# test if Hand class is giving desired outputs
h1 = Hand("7hAcQd9c9d")
h2 = Hand("7d8dQdTd9d9cJd")
h3 = Hand("7h8cJdTc9dAh2s")
h4 = Hand("7h4c3dTc5dAh2s")

print(
    h1.cards == [[5, 2], [12, 0], [10, 1], [7, 0], [7, 1]]
    and h2.cards == [[5, 1], [6, 1], [10, 1], [8, 1], [7, 1], [7, 0], [9, 1]]
    and h3.cards == [[5, 2], [6, 0], [9, 1], [8, 0], [7, 1], [12, 2], [0, 3]]
    and h4.cards == [[5, 2], [2, 0], [1, 1], [8, 0], [3, 1], [12, 2], [0, 3]],
    ": method cards in Hand class in hand.py",
)

print(
    h1.teststraight(h1.rankcount) == (False, None)
    and h2.teststraight(h2.rankcount) == (True, 10)
    and h3.teststraight(h3.rankcount) == (True, 9)
    and h4.teststraight(h4.rankcount) == (True, 3),
    ": function teststraight in Hand class in hand.py",
)

# testing hand strengths in hand class
h10 = Hand("AdTd4cKd2sQdJd")  # royalflush
print(
    (h10.strength, h10.straightflush, h10.straightflushrank) == (8, True, 12),
    ": royalflush strength in hand class",
)
h11 = Hand("9dTd4cKd2sQdJd")  # straightflush
print(
    (h11.strength, h11.straightflush, h11.straightflushrank) == (8, True, 11),
    ": straightflush strength in hand class",
)
h12 = Hand("TcTd4cThTsQdJd")  # fourofakind
print(
    (h12.strength, h12.fourofakind, h12.fourofakindrank, h12.fourofakindkicker)
    == (7, True, 8, 10),
    ": fourofakind strength in hand class",
)
h13 = Hand("TcTdQcQhTsQdJd")  # fullhouse
print(
    (h13.strength, h13.fullhouse, h13.fullhousetriprank, h13.fullhousepairrank)
    == (6, True, 10, 8),
    ": fullhouse strength in hand class",
)
h14 = Hand("Ad9d6d4d2dQdJd")  # flush
print(
    (h14.strength, h14.flush, h14.flushranks) == (5, True, [4, 7, 9, 10, 12]),
    ": flush strength in hand class",
)
h15 = Hand("3d6d4c4d2s5hJd")  # straight
print(
    (h15.strength, h15.straight, h15.straightrank) == (4, True, 4),
    ": straight strength in hand class",
)
h16 = Hand("3d4h4c4d2s5hJd")  # threeofakind
print(
    (h16.strength, h16.threeofakind, h16.threeofakindrank, h16.threeofakindkickers)
    == (3, True, 2, [3, 9]),
    ": threeofakind strength in hand class",
)
h17 = Hand("3d3h4c4d2sJhJd")  # twopair
print(
    (h17.strength, h17.twopair, h17.twopairranks, h17.twopairkicker)
    == (2, True, [2, 9], 1),
    ": twopair strength in hand class",
)
h18 = Hand("3d7d4c4d2s5hJd")  # pair
print(
    (h18.strength, h18.pair, h18.pairrank, h18.pairkickers) == (1, True, 2, [3, 5, 9]),
    ": pair strength in hand class",
)
h19 = Hand("3d7dTc4d2s5hJd")  # highcard
print(
    (h19.strength, h19.highcard, h19.highcards) == (0, True, [2, 3, 5, 8, 9]),
    ": highcard strength in hand class",
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
