

#       Caesar Cipher


def cypher():
        plain =    ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
        caesar = ["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"," "]

        word = input("Give me a sentence to encrypt:    ")
        output = ""
        for letter in word:
                index = plain.index(letter)
                printed = caesar[int(index)]
                output = output + printed
        print(output)

run = True
while run:
        print("")
        cypher()
        ask = input("Do you want to continue encrypting?  [yes/no]   ").lower()
        
        if ask in ["no","nope","n"]:
                run = False
        
