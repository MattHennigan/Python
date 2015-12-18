"""
varienceTest.py:

Varience in poker is defined as the upswings and downswings that a player can expect in their game.
In its most simple form, variance is attributed to luck. Poker is majorly based on chance, and hence one cannot expect to win all the time.
Even with the best starting hand in the game (two aces), one can only expect to win the hand 85.2% of the time (every 4 out of 5).
This program is designed to demonstrate a very basic form of variance; the difference between how often you receive either two aces or two
kings compared to the amount you can expect to receive them (1 in every 220 hands on average for each).

This is calculated by virtually dealing thousands of hands and then recording each time the player receives a hand that has been specified.
The program will then perform calculations on the data to produce a value for the long term variance of a player (in receiving Aces or Kings),
the closer this number is to one, the smaller the variance. If the program is run for only a small number of hands we can see that the variance
is very volatile, however as the number of hands dealt is increased the variance will get closer to the expected value (variance → 1).
"""


import random
import time
from termcolor import colored, cprint

# Create a deck of possible cards that can be dealt to a player.
possibles = ["Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts",
             "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts", 
             "Ace of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds",
             "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds", 
             "Ace of Spades", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades", 
             "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades", 
             "Ace of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs", 
             "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs"]

# Assign counters for the number of hands dealt, the number of times the player received pocket Aces or pocket Kings.
count = 0
count_for_aces = 0
count_for_kings = 0

# Create empty lists which will contain integer values for how many hands were dealt until player received either pocket Aces or Kings.
aceCount = []
kingCount = []

def clear_terminal():
    """
    'clear_terminal()' uses ANSI escape codes to clear the screen.
    https://en.wikipedia.org/wiki/ANSI_escape_code
    """

    CSI = chr(27)

    # 1) We need to clear the entire screen. Note this leaves the cursor
    # wherever it was.

    # CSI "[" n "J"
    # Clears part of the screen. If n is 0 (or missing), clear from cursor to
    # end of screen. If n is 1, clear from cursor to beginning of the screen.
    # If n is 2, clear entire screen (and moves cursor to upper left on
    # DOS ANSI.SYS).
    print(CSI + "[2J", end='')

    # 2) Move the cursor back to the top left corner so the next time we print
    # something it appears there.

    # CSI "[" n ";" m "H"
    # Moves the cursor to row n, column m. The values are 1-based, and default
    # to 1 (top left corner) if omitted. A sequence such as CSI ;5H is a synonym
    # for CSI 1;5H as well as CSI 17;H is the same as CSI 17H and CSI 17;1H
    print(CSI + "[H", end='')


while True:
    # Deal the player's first card.
    firstCard = random.choice(possibles)
    # Ensure the player cannot receive the same card twice by temporarily removing the first card from 'possibles'.
    possibles.remove(firstCard)
    # Deal the player's second card.
    secondCard = random.choice(possibles)
    # Create list to contain players hand.
    myCards = []
    # Double check to ensure system does not deal the same card twice.
    if firstCard != secondCard:
        for idx, item in enumerate("x"):
            myCards.append(firstCard)
            myCards.append(secondCard)
            # print(myCards)
            possibles.append(firstCard)
            # A hand has been dealt, add 1 to all counters.
            count += 1
            count_for_aces += 1
            count_for_kings +=1
            time.sleep(0.00001)

            if "Ace" in firstCard and "Ace" in secondCard:
                # print("You received pocket aces on hand number:", count_for_aces)
                aceCount.append(count_for_aces)
                # Player has received pocket Aces so reset count_for_aces to zero.
                count_for_aces = 0
                # Calculate how many times player has received pocket aces so far.
                ace_num = len(aceCount)
                # Calculate how often the player receives pocket aces.
                average_acecount = sum(aceCount) / ace_num
                # Number of times pockets aces have been received.
                king_num = len(kingCount)
                # Exception handling for the case that king_num is equal to zero.
                if king_num == 0:
                    average_kingcount = sum(kingCount) / 1
                else:
                    average_kingcount = sum(kingCount) / king_num
                kingVariance = average_kingcount / 220
                aceVariance = average_acecount / 220
                
                # Create coloured text to display variance
                positive = colored('Positive variance!', 'magenta', attrs=['bold'])
                negative = colored('Negative variance!', 'red', attrs=['bold'])
                even = colored('Even variance!', 'yellow', attrs=['bold'])
                
                # Display hand information
                print("Average Ace Count:", average_acecount)
                print("Pocket aces received", ace_num, "times.")
                print("Ace Variance:", aceVariance, "\n")
                if aceVariance > 1:
                    print(positive)
                if aceVariance < 1:
                    print(negative)
                if aceVariance == 1:
                    print(even)
                print("\n")
                
                print("Average King Count:", average_kingcount)
                print("Pocket Kings received", king_num, "times.")
                print("King Variance:", kingVariance, "\n")
                if kingVariance > 1:
                    print(positive)
                if kingVariance < 1:
                    print(negative)
                if kingVariance == 1:
                    print(even)
                print("\n")
                clear_terminal()
            
            if "King" in firstCard and "King" in secondCard:
                # print("You received pocket kings on hand number:", count_for_kings)
                kingCount.append(count_for_kings)
                # Player has received pocket Kings so reset count_for_aces to zero.
                count_for_kings = 0
                # Calculate how many times player has received pocket kings so far.
                king_num = len(kingCount)
                # Calculate how often the player receives pocket kings.
                average_kingcount = sum(kingCount) / king_num
                # Number of times pockets kings have been received.
                ace_num = len(aceCount)
                # Exception handling for the case that ace_num is equal to zero.
                if ace_num == 0:
                    average_acecount = sum(aceCount) / 1
                else:
                    average_acecount = sum(aceCount) / ace_num
                kingVariance = average_kingcount / 220
                aceVariance = average_acecount / 220
                
                # Create coloured text to display variance
                positive = colored('Positive variance!', 'magenta', attrs=['bold'])
                negative = colored('Negative variance!', 'red', attrs=['bold'])
                even = colored('Even variance!', 'yellow', attrs=['bold'])
                
                # Display hand information
                print("Average Ace Count:", average_acecount)
                print("Pocket aces received", ace_num, "times.")
                print("Ace Variance:", (average_acecount / 220), "\n")
                if aceVariance > 1:
                    print(positive)
                if aceVariance < 1:
                    print(negative)
                if aceVariance == 1:
                    print(even)
                print("\n")
                
                print("Average King Count:", average_kingcount)
                print("Pocket Kings received", king_num, "times.")
                print("King Variance:", (average_kingcount / 220), "\n") 
                if kingVariance > 1:
                    print(positive)
                if kingVariance < 1:
                    print(negative)
                if kingVariance == 1:
                    print(even)
                print("\n")   
                clear_terminal()       
