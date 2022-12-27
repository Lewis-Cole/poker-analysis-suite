"""
File: hand.py

Variables
---------
ranks: list
suits: list

Functions
---------
parsecard
    converts card data from str to list of int
    argument: str e.g. "7h"
    returns: list e.g. [5, 2]

Classes
-------
Hand
    objects represent poker hands
    argument: str e.g. "3d4h4c4d2s5hJd"
    Properties
        cards: list
        cardsstring: str
        flush: bool
        flushrankcount: list
        flushranks: list
        flushsuits: list
        fourofakind: bool
        fourofakindkicker: int
        fourofakindrank: int
        fullhouse: bool
        fullhousepairrank: int
        fullhousetriprank: int
        highcard: bool
        highcards: list
        pair: bool
        pairkickers: list
        pairrank: int
        pairs: list
        quads: list
        rankcount: list
        straight: bool
        straightflush: bool
        straightflushrank: int
        straightrank: int
        strength: int
        suitcount: list
        threeofakind: bool
        threeofakindkickers: list
        threeofakindrank: int
        trips: list
        twopair:bool
        twopairkicker: int 
        twopairranks: list
    Methods
        teststraight
            argument: list
            returns: tuple[bool, int]

"""


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
    Objects represent poker hands

    Argument
    --------
    cardsstring : str
        string containing all cards in hand e.g. "3d4h4c4d2s5hJd"

    Properties
    ----------
        cards: list
        cardsstring: str
        flush: bool
        flushrankcount: list
        flushranks: list
        flushsuits: list
        fourofakind: bool
        fourofakindkicker: int
        fourofakindrank: int
        fullhouse: bool
        fullhousepairrank: int
        fullhousetriprank: int
        highcard: bool
        highcards: list
        pair: bool
        pairkickers: list
        pairrank: int
        pairs: list
        quads: list
        rankcount: list
        straight: bool
        straightflush: bool
        straightflushrank: int
        straightrank: int
        strength: int
        suitcount: list
        threeofakind: bool
        threeofakindkickers: list
        threeofakindrank: int
        trips: list
        twopair: bool
        twopairkicker: int
        twopairranks: list

    Methods
    -------
        teststraight
            argument: list
            returns: tuple[bool, int]

    """

    def __init__(self, cardsstring: str) -> None:
        self.cardsstring = cardsstring
        self.cards = [
            parsecard(cardsstring[i : i + 2]) for i in range(0, len(cardsstring), 2)
        ]
        self.strength = self.determinestrength()

    def determinestrength(self) -> int:
        """
        Returns
        -------
        int
            hand strength
            8 = straightflush
            7 = fourofakind
            6 = fullhouse
            5 = flush
            4 = straight
            3 = threeofakind
            2 = twopair
            1 = pair
            0 = highcard

        """

        self.rankcount = [0 for i in ranks]
        self.suitcount = [0 for i in suits]

        for card in self.cards:
            self.rankcount[card[0]] += 1
            self.suitcount[card[1]] += 1

        # test for flush
        self.flush = False
        self.flushsuits = [
            i for i in range(0, len(self.suitcount)) if self.suitcount[i] >= 5
        ]
        if len(self.flushsuits) >= 1:
            self.flush = True

        # test for straightflush
        self.straightflush = False
        for flushsuit in self.flushsuits:
            self.flushrankcount = [0 for i in ranks]
            for card in self.cards:
                if card[1] == flushsuit:
                    self.flushrankcount[card[0]] += 1
            (self.straightflush, self.straightflushrank) = self.teststraight(
                self.flushrankcount
            )
            if self.straightflush:
                return 8  # straightflush

        # test for fourofakind
        self.fourofakind = False
        self.quads = [
            i for i in range(0, len(self.rankcount)) if self.rankcount[i] == 4
        ]
        if len(self.quads) >= 1:
            self.fourofakind = True
            self.fourofakindrank = max(self.quads)
            self.fourofakindkicker = max(
                [card[0] for card in self.cards if card[0] != self.fourofakindrank]
            )
            return 7  # fourofakind

        # test for fullhouse
        self.fullhouse = False
        self.trips = [
            i for i in range(0, len(self.rankcount)) if self.rankcount[i] == 3
        ]
        self.pairs = [
            i for i in range(0, len(self.rankcount)) if self.rankcount[i] == 2
        ]
        if len(self.trips) >= 2 or (len(self.trips) >= 1 and len(self.pairs) >= 1):
            self.fullhouse = True
            self.fullhousetriprank = max(self.trips)
            self.fullhousepairrank = max(
                [i for i in self.trips if i != self.fullhousetriprank] + self.pairs
            )
            return 6  # fullhouse

        # return flush result
        if self.flush:
            self.flushranks = sorted(
                [card[0] for card in self.cards if card[1] in self.flushsuits]
            )[-5:]
            return 5  # flush

        # test for straight
        self.straight = False
        (self.straight, self.straightrank) = self.teststraight(self.rankcount)
        if self.straight:
            return 4  # straight

        # test for threeofakind
        self.threeofakind = False
        if len(self.trips) >= 1:
            self.threeofakind = True
            self.threeofakindrank = max(self.trips)
            self.threeofakindkickers = sorted(
                [card[0] for card in self.cards if card[0] != self.threeofakindrank]
            )[-2:]
            return 3  # threeofakind

        # test for twopair
        self.twopair = False
        if len(self.pairs) >= 2:
            self.twopair = True
            self.twopairranks = sorted(self.pairs)[-2:]
            self.twopairkicker = max(
                [card[0] for card in self.cards if not card[0] in self.twopairranks]
            )
            return 2  # twopair

        # test for pair
        self.pair = False
        if len(self.pairs) >= 1:
            self.pair = True
            self.pairrank = max(self.pairs)
            self.pairkickers = sorted(
                [card[0] for card in self.cards if card[0] != self.pairrank]
            )[-3:]
            return 1  # pair

        # return highcard kickers
        self.highcard = True
        self.highcards = sorted([card[0] for card in self.cards])[-5:]
        return 0  # highcard

    def teststraight(self, cardsrankcount: list) -> tuple[bool, int]:
        """
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
