# - File: parse.py
#   - function parseboard() input: string (6 <= len <= 10) board string, output: list (len = input length/2) card strings (len = 2)
#   - function parserange() input: string equilab range, output: list of hand strings (len = 4)


def parseboard(boardstring: str) -> list:
    """
    >>> parseboard("7h4s3c")
    ["7h", "4s", "3c"]

    Argument
    --------
    boardstring : str
        string (6 <= len <= 10) board string e.g. "7h4s3c"

    Returns
    -------
    list
        list (len = len(boardstring)/2) containing str cardstring e.g. ["7h", "4s", "3c"]

    """

    return


def parserange(rangestring: str) -> list:
    """
    Convert equilab format range strings into list of handstrings.

    >>> parserange("99")
    ["9c9d", "9c9h", "9c9s", "9d9h", "9d9s", "9h9s"]

    Argument
    --------
    rangestring : str
        equilab format range string e.g. "99", "JJ+", "AQo, KK+", "KQs-K9s, KQo-KJo"

    Returns
    -------
    list
        list containing str handstring e.g. ["9c9d", "9c9h", "9c9s", "9d9h", "9d9s", "9h9s"]

    """

    return
