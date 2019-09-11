

#                  A friendly game of Rock Scissors Paper Lizard Spock

##                Scissors cuts Paper
##                Paper covers Rock
##                Rock crushes Lizard
##                Lizard poisons Spock
##                Spock smashes Scissors
##                Scissors decapitates Lizard
##                Lizard eats Paper
##                Paper disproves Spock
##                Spock vaporises Rock
##                and as it always has
##                Rock crushes Scissors.

def game():
        print("")
        print("                                                           Rock, Scissors, Paper, Lizard, Spock ! ")
        print("")
        user1 = input("Player 1 please input your move:    ").lower()
        user2 = input("Player 2 please input your move:    ").lower()
        movelist = ["scissors","paper","rock","spock","lizard"]
        if user1 not in movelist or user2 not in movelist:
                print("THAT'S NOT A MOVE")
                return None

        if user1 == "paper":
                if user2 == "scissors":
                        lose = 1
                elif user2 == "lizard":
                        lose = 1
                else:
                        lose = 0
        elif user1 == "rock":
                if user2 == "paper":
                        lose = 1
                elif user2 == "spock":
                        lose = 1
                else:
                        lose = 0
        elif user1 == "scissors":
                if user2 == "spock":
                        lose = 1
                elif user2 == "rock":
                        lose = 1
                else:
                        lose = 0
        elif user1 == "spock":
                if user2 == "lizard":
                        lose = 1
                elif user2 == "paper":
                        lose = 1
                else:
                        lose = 0
        elif user1 == "lizard":
                if user2 == "scissors":
                        lose = 1
                elif user2 == "rock":
                        lose = 1
                else:
                        lose = 0

        if lose == 0:
                print("Player 1 played "+ user1 + " against Player 2's " + user2 + " and wins!")
        elif lose == 1:
                print("Player 2 played "+ user2 + " against Player 1's " + user1 + " and wins!")
                
game()
