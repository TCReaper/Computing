import time


# rationals


running = True
while running:
        number = input("Enter a number to save, or X to exit:   ")
        if number.lower() == "x":
                print("Exiting...")
                time.sleep(1)
                running = False
        else:
                try:
                        number = int(number)
                except ValueError:
                        print("That wasn't a number....  Try again <3")
                        print("")

                else:
                        f = open("3. List.txt", "a")
                        f.write(str(number) + "\n")
                        f.close()
                              
                        
