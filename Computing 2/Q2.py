# Takes integer, prints out digits in word form


def wordform(n, length, current, Final):
        
        if current == length:
                print(Final)
        
        else:
                if n[current] == "0":
                        Final = Final + " zero"
                        return Final + wordform(n, length, current + 1, Final)
                
                elif n[current] == "1":
                        Final = Final + " one"
                        return Final + wordform(n, length, current + 1, Final)
                
                elif n[current] == "2":
                        Final = Final + " two"
                        return Final + wordform(n, length, current + 1, Final)
                
                elif n[current] == "3":
                        Final = Final + " three"
                        return Final + wordform(n, length, current + 1, Final)
                
                elif n[current] == "4":
                        Final = Final + " four"
                        return Final + wordform(n, length, current + 1, Final)
                
                elif n[current] == "5":
                        Final = Final + " five"
                        return Final + wordform(n, length, current + 1, Final)
                
                elif n[current] == "6":
                        Final = Final + " six"
                        return Final + wordform(n, length, current + 1, Final)
                
                elif n[current] == "7":
                        Final = Final + " seven"
                        return Final + wordform(n, length, current + 1, Final)
                
                elif n[current] == "8":
                        Final = Final + " eight"
                        return Final + wordform(n, length, current + 1, Final)
                
                elif n[current] == "9":
                        Final = Final + " nine"
                        return Final + wordform(n, length, current + 1, Final)
                else:
                        print("It's not a word!")





n = input("What positive integer would you like to convert to words?    ")
length = len(str(n))
current = 0
Final = " "


wordform(n, length, current, Final)
