

#       Positive Square List

n = int(input("Type in where you want your perfect squares to end:   "))
g = open("2. n.txt", "w")
g.write(str(n))
g.close()
def squares(n):

        current_square = 4
        squareList =[1]
        while current_square <= n:
                squareList.append(current_square)
                current_square = (len(squareList) + 1)**2
        return squareList
        
print(squares(n))

#       Saving


def saver():
        current_square = 4
        squareList =[1]
        while current_square <= n:
                squareList.append(current_square)
                current_square = (len(squareList) + 1)**2

        f = open("1. PosiSquares.txt", "w")
        for i in squareList:
                f.write(str(i) + "\n") 
        f.close()

saver()
