def findPokerHand(hand):

    ranks = []
    suits = []
    possibleRanks = []

    for card in hand:
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
        else:
            rank = card[0:2]
            suit = card[2]

        if rank == "A":
            rank = 14

        if rank == "K":
            rank = 13

        if rank == "Q":
            rank = 12

        if rank == "J":
            rank = 11

        ranks.append(int(rank))
        suits.append(suit)

    sortedRanks = sorted(ranks)


    # Royal Flush && Straight Flush && Flush
    if suits.count(suits[0]) == 5:
        # Royal FLush
        if 14 in sortedRanks and 13 in sortedRanks and 12 in sortedRanks and 11 in sortedRanks and 10 in sortedRanks:
            possibleRanks.append(10)

        # Straight Flush
        elif all(sortedRanks[i] == sortedRanks[i - 1] + 1 for i in range(1, len(sortedRanks))):
            possibleRanks.append(9)

        # Flush
        else:
            possibleRanks.append(6)


    # Straight
    # 10 11 12 13 14
    # 11 == 10+1 True
    elif all(sortedRanks[i] == sortedRanks[i - 1] + 1 for i in range(1, len(sortedRanks))):
        possibleRanks.append(5)

    handUniqueVals = list(set(sortedRanks))


    #Four of a kind and Full House
    #3 3 3 3 5 --> set --> 3 5 --> Four of a kind --> if 3 == 4
    #3 3 3 5 5 --> set --> 3 5 --> Full house --> if 3 == 3
    if len(handUniqueVals) == 2:
        for val in handUniqueVals:
            if sortedRanks.count(val) == 4: #Four of a kind
                possibleRanks.append(8)

            elif sortedRanks.count(val) == 3: #Full house
                possibleRanks.append(7)


    #Three of a kind and two pairs
    # 5 5 5 6 7 --> set --> 5 6 7 --> Three of a kind
    # 5 5 6 6 7 --> set --> 5 6 7 --> Two pair
    if len(handUniqueVals) == 3:
        for val in handUniqueVals:
            if sortedRanks.count(val) == 3: #three of a kind
                possibleRanks.append(4)
            elif sortedRanks.count(val) == 2: #two pair
                possibleRanks.append(3)


    #Pair
    #4 4 5 6 7 --> set --> 4 5 6 7 --> 4 Unique --> Pair
    if len(handUniqueVals) == 4:
        possibleRanks.append(2)

    if not possibleRanks:
        possibleRanks.append(1)

    #print(max(possibleRanks))
    pokerHandRanks = {10:"Royal Flush", 9:"Straight Flush", 8:"Four of a Kind", 7:"Full House", 6:"Flush",
                    5:"Straight", 4:"Three of a Kind", 3:"Two Pair", 2:"Pair", 1:"High"}

    output = pokerHandRanks[max(possibleRanks)]

    print(hand,output,"\n")

    return output


#Demo Data
if __name__ == '__main__':
    findPokerHand(["AH", "KH", "QH", "JH", "10H"]) # Royal Flush
    findPokerHand(["QC", "JC", "10C", "9C", "8C"])  # Straight Flush
    findPokerHand(["5H", "5S", "5D", "5C", "QH"]) # Four of a Kind
    findPokerHand(["2H", "2S", "2D", "10C", "10H"])  # Full House
    findPokerHand(["KH", "7H", "6H", "10H", "2H"])  # Flush
    findPokerHand(["10H", "9C", "8D", "7S", "6H"])  # Straight
    findPokerHand(["7H", "7D", "7S", "QS", "3H"])  # Three of a kind
    findPokerHand(["JH", "JS", "5D", "5S", "7H"])  # Two Pair
    findPokerHand(["AH", "AC", "KD", "JH", "7S"])  # Pair
    findPokerHand(["KH", "8S", "3D", "10C", "2H"])  # High Card
