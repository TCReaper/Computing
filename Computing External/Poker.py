

##        5 card poker

##        Deck:
##                4 Suites:
##                        Spades Hearts Clubs Diamonds
##                13 Cards:
##                        2 3 4 5 6 7 8 9 10 J Q K A
##
##        Hand:
##                Straight Flush:
##                        5 Cards in continuous sequence
##                        5 Cards in same suite
##                4 of a kind:
##                        4 Cards of same number
##                Full-House:
##                        3 of a kind
##                        2 of a kind
##                Flush:
##
##                Straight:
##
##                3 of a kind:
##
##                2 Pairs:
##
##                1 Pair:
##
##                High Card:

##
##        Evaluate...
##                card_value_frequency
##                hand_sequence
##                suite_frequency



hand = [(3,1),(2,1),(3,1),(4,2),(5,3)]
cards = []
suites = []
cardFreq = {}
freqFreq = {}
suiteFreq = {}

for tup in hand:
        cards.append(int(tup[0]))

cards.sort()

for card in cards:
        if card in cardFreq:
                cardFreq[card] += 1
        else:
                cardFreq[card] = 1

print(cardFreq)

for key in cardFreq.keys():
        if cardFreq[key] in freqFreq:
                freqFreq[cardFreq[key]] += 1
        else:
                freqFreq[cardFreq[key]] = 1

print(freqFreq)

for tup in hand:
        suites.append(tup[1])

print(suites)

for suite in suites:
        if suite in suiteFreq:
                suiteFreq[suite] += 1
        else:
                suiteFreq[suite] = 1
                
print(suiteFreq)

maxValue = max(cards)
minValue = min(cards)

def check():
        if freqFreq[1] == 5:
                if maxValue - minValue == 4:
                        return "It is a straight flush!"
                elif 14 in cards:
                        print(cards)
                        if cards[3] - cards [0] == 3:
                                return "It is a straight flush!"
        elif suites.count(suites[0]) == 5:
                return "It is a straight flush!"
        

print(check())














