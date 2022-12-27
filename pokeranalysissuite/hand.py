# - File: hand.py
#   - function parsecard() input: string (len = 2) rank and suit string (e.g. '7h'), output: list (len = 2) int for rank and suit
#       (e.g. [5, 2] - ranks: 0 = "2", 5 = "7", 9 = "J", 12 = "A"; suits: 0 = "c", 1 = "d", 2 = "h", 3 = "s")
#   - class Hand() input: list (len = no. of cards) cards (e.g. [[5, 2], [2, 2], [10, 2], [10, 3], [5, 1]]), card is list (len = 2) int for rank and suit (e.g. [5, 2])
#   - determine strength of hand

# - determine hand strength
#   - handstrength: 9 = "royalflush", 8 = "straightflush", 7 = "fourofakind", 6 = "fullhouse", 5 = "flush",
#       4 = "straight", 3 = "threeofakind", 2 = "twopair", 1 = "pair", 0 = "highcard"
#   - function testflush() output: (boolean, flushsuit, flushcards)
#   - function teststraight() output: (boolean, straightrank) [note: go from highest to lowest rank]
#   - straightflush: testflush() then teststraight() on flushcards output: (boolean, straightflushrank)
#   - royalflush: if straightflush then is straightflushrank = "A" output: boolean
#   - function generaterankdata() output: rankdata = list (len = 14) no. of cards of each rank in hand
#   - fourofakind: if 4 in rankdata output: (boolean, quads, kicker)
#   - fullhouse: if 3 in rankdata twice, or 3 and 2 in rank data ouput: (boolean, trips, pair)
#   - flush: if testflush() output: (boolean, highflushcards)
#   - straight: teststraight() on cards output: (boolean, straightrank)
#   - threeofakind: if 3 in rankdata output: (boolean, trips, kickers)
#   - twopair: if 2 in rankdata twice output: (boolean, firstpair, secondpair, kicker)
#   - pair: if 2 in rankdata output: (boolean, pair, kickers)
#   - highcard: else output: (highcards)


ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
suits = ["c", "d", "h", "s"]


def parsecard(cardstring: str) -> list:
    """
    >>> parsecard("7h")
    [5, 2]

    >>> parsecard("Ac")
    [12, 0]

    >>> parsecard("Qd")
    [10, 1]

    Argument
    --------
    cardstring : str
        string (len = 2) containing card rank and suit e.g. "7h"

    Returns
    -------
    list
        list (len = 2) containing int representing card rank and suit e.g. [5, 2]

    """

    if len(cardstring) != 2:
        raise ValueError("String must have length 2")

    if not cardstring[0] in ranks:
        raise ValueError(
            "First character of string must be a rank from the following list: "
            + str(ranks)
        )

    if not cardstring[1] in suits:
        raise ValueError(
            "Second character of string must be a suit from the following list: "
            + str(suits)
        )

    return [ranks.index(cardstring[0]), suits.index(cardstring[1])]


class Hand:
    """
    Summary line.

    Arguments
    ---------
    cardsstring : str
        string containing all cards in hand e.g. "7hAcQd9c9d"

    Methods
    -------
    cards
        argument: none
        returns: list containing cards e.g. [[5, 2], [12, 0], [10, 1], [7, 0], [7, 1]]

    """

    def __init__(self, cardsstring: str) -> None:
        self.cardsstring = cardsstring
        self.cards = [
            parsecard(cardsstring[i : i + 2]) for i in range(0, len(cardsstring), 2)
        ]
        self.strength = self.determinestrength()

    def determinestrength(self) -> int:
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

        self.rankcount = [0 for i in ranks]
        self.suitcount = [0 for i in suits]

        for card in self.cards:
            self.rankcount[card[0]] += 1
            self.suitcount[card[1]] += 1

        # test for straightflush
        self.flushsuits = [self.suitcount.index(i) for i in self.suitcount if i >= 5]
        for flushsuit in self.flushsuits:
            self.flushrankcount = [0 for i in ranks]
            for card in self.cards:
                if card[1] == flushsuit:
                    self.flushrankcount[card[0]] += 1
            (self.straightflush, self.straightflushrank) = self.teststraight(
                self.flushrankcount
            )
            if self.straightflush:
                if self.straightflushrank == 12:
                    return 9
                return 8

        # test for fourofakind
        self.quads = [
            i for i in range(0, len(self.rankcount)) if self.rankcount[i] == 4
        ]

        self.trips = [
            i for i in range(0, len(self.rankcount)) if self.rankcount[i] == 3
        ]
        self.pairs = [
            i for i in range(0, len(self.rankcount)) if self.rankcount[i] == 2
        ]

    def teststraight(self, cardsrankcount: list) -> tuple[bool, int]:
        """
        Summary line.

        Extended description of function.

        >>> teststraight([0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 1, 0, 1])
        (False, None)

        >>> teststraight([0, 0, 0, 0, 0, 1, 1, 2, 1, 1, 1, 0, 0])
        (True, 10)

        >>> teststraight([1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1])
        (True, 3)

        Arguments
        ---------
        cardsrankcount : list
            list of card ranks e.g. [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1]

        Returns
        -------
        tuple(bool, int)
            (bool = there is a straight, int = rank of straight)

        """

        straightcounter = 0

        for i in range(1, len(cardsrankcount) + 1):
            if cardsrankcount[-i] >= 1:
                straightcounter += 1
                if straightcounter == 5:
                    return (True, 17 - i)
            if cardsrankcount[-i] == 0:
                straightcounter = 0

        if cardsrankcount[-1] >= 1:
            straightcounter += 1
            if straightcounter == 5:
                return (True, 3)

        return (False, None)
