# Poker analysis suite 
Suite of analysis tools for poker 

## Objectives 
- Produce improved version of 'Poker-Solver' 
  - find the best poker hand for a set of 7 cards 
  - compare the showdown strength of two 7 card hands 
  - find the equity of two given hands 
  - find the equity of a given hand against a given range of hands 
- Produce a cumulative density plot for the equity distributions 
  - x-axis = cumulative density (high to low) 
  - y-axis = equity 

## Plan 
- File: hand.py 
  - function parsecard() input: string (len = 2) rank and suit string (e.g. '7h'), output: list (len = 2) int for rank and suit (e.g. [5, 2] - ranks: 0 = "2", 5 = "7", 9 = "J", 12 = "A"; suits: 0 = "c", 1 = "d", 2 = "h", 3 = "s") 
  - class hand() input: list (len = no. of cards) cards (e.g. [[5, 2], [2, 2], [10, 2], [10, 3], [5, 1]]), card is list (len = 2) int for rank and suit (e.g. [5, 2]) 
  - determine strength of hand 
- File: parse.py 
  - function parseboard() input: string (6 <= len <= 10) board string, output: list (len = input length/2) card strings (len = 2) 
  - function parserange() input: string equilab range, output: list of hand strings (len = 4) 
- File: equitycalc.py 
  - function calculateequity() input: ranges/hands, output: equity (hand by hand) 
- File: graph.py 
  - produces desired graph 
- File: test.py 
  - series of tests to check other files are working as intended 

### File: hand.py 
- determine hand strength 
  - handstrength: 9 = "royalflush", 8 = "straightflush", 7 = "fourofakind", 6 = "fullhouse", 5 = "flush", 4 = "straight", 3 = "threeofakind", 2 = "twopair", 1 = "pair", 0 = "highcard" 
  - function testflush() output: (boolean, flushsuit, flushcards) 
  - function teststraight() output: (boolean, straightrank) [note: go from highest to lowest rank] 
  - straightflush: testflush() then teststraight() on flushcards output: (boolean, straightflushrank) 
  - royalflush: if straightflush then is straightflushrank = "A" output: boolean
  - function generaterankdata() output: rankdata = list (len = 14) no. of cards of each rank in hand 
  - fourofakind: if 4 in rankdata output: (boolean, quads, kicker) 
  - fullhouse: if 3 in rankdata twice, or 3 and 2 in rank data ouput: (boolean, trips, pair) 
  - flush: if testflush() output: (boolean, highflushcards) 
  - straight: teststraight() on cards output: (boolean, straightrank) 
  - threeofakind: if 3 in rankdata output: (boolean, trips, kickers) 
  - twopair: if 2 in rankdata twice output: (boolean, firstpair, secondpair, kicker) 
  - pair: if 2 in rankdata output: (boolean, pair, kickers) 
  - highcard: else output: (highcards) 
