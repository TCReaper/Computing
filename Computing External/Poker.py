

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



hand = [(2,1),(3,3),(4,2),(5,4),(7,1)]
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
        fourkind = 0
        threekind = 0
        twokind = 0
        onekind = 0
        for i in freqFreq:
                if i == 4:
                        fourkind = 1
                elif i == 3:
                        threekind = 1
                elif i == 2:
                        twocount = freqFreq[2]
                        twokind = twocount
                elif i == 1:
                        onecount = freqFreq[1]
                        onekind = onecount
        if onekind == 5:
                process = True
                while process:
                        if suites.count(suites[0]) == 5:
                                if maxValue - minValue == 4:
                                        setvalue = 9
                                        #return "It is a straight flush!"
                                elif 14 in cards: 
                                        print(cards)
                                        if cards[3] - cards [0] == 3:
                                                setvalue = 9
                                                #return "It is a straight flush!"
                                else:
                                        setvalue = 1
                                        process = False
                        else:
                                if maxValue - minValue == 4:
                                        setvalue = 5
                                        #return "It is a straight!"
                                elif 14 in cards: 
                                        print(cards)
                                        if cards[3] - cards [0] == 3:
                                                setvalue = 5
                                                #return "It is a straight!"
                                else:
                                        setvalue = 1
                                        process = False
                                
        elif suites.count(suites[0]) == 5:
                setvalue = 6
                #return "It is a flush!"
        
        elif fourkind == 1:
                setvalue = 8
                #return "It is a 4 of a kind!"
        
        elif threekind == 1:
                if twokind == 1:
                        setvalue = 7
                        #return "It is a full house!"
                else:
                        setvalue = 4
                        #return "It is a 3 of a kind!"
        elif twokind > 0:
                if twokind == 2:
                        setvalue = 3
                        #return "It is a two pair!"
                else:
                        setvalue = 2
                        #return "It is a single pair!"

        else:
                setvalue = 1

        evaluated = setvalue * 1000
        print(cards)
        highestcard = max(cards)
        highestcardindex = cards.index(highestcard)
        highestcardsuite = suites[highestcardindex]
        highestcard = highestcard * 10
        evaluated = evaluated + highestcard + highestcardsuite
        print(evaluated)
        
print(check())














