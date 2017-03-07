

# Caesar Cipher




abc =  ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ABC = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
space = [" "]
sentence = input("Enter sentence to encrypt:    ")
shift = int(input("Input shift value:    "))
crypted = ""

for i in sentence:
        if i in abc:
                index = abc.index(i)
                index += shift
                if index>25:
                        index -= 26
                output = abc[index]
        if i in ABC:
                index = ABC.index(i)
                index += shift
                if index>25:
                        index -= 26
                output = ABC[index]
        if i in space:
                output = " "
        crypted = crypted + output

print(crypted)
