


debug_mode = True

n  = input("positive integer: ")

tempPermutations = [["",n]]
finalPermutations = []
output = []

itr = 1
while len(tempPermutations) > 0:
        print(str(itr))
        currentPermutations = tempPermutations[0]
        if debug_mode:
                print("\tRemoving: [" + currentPermutations[0] + "," + currentPermutations[1] + "]")
        tempPermutations = tempPermutations[1:]
        for i in range(len(currentPermutations[1])):
                if len(currentPermutations[1][:i]+currentPermutations[1][i+1:])>0:
                        if debug_mode:
                                print("\tAdding to temp: [" + currentPermutations[0]+currentPermutations[1][i] + "," \
                                        + currentPermutations[1][:i]+currentPermutations[1][i+1:] + "]")
                                tempPermutations.append([currentPermutations[0]+currentPermutations[1][i] ,  \
                                                 currentPermutations[1][:i]+currentPermutations[1][i+1:]])
        
                else:
                        if debug_mode:
                                print("\tAdding to final: [" + currentPermutations[0]+currentPermutations[1][i] + "," \
                                      + currentPermutations[1][:i]+currentPermutations[1][i+1:] + "]")
                                finalPermutations.append([currentPermutations[0]+currentPermutations[1][i] , \
                                                  currentPermutations[1][:i]+currentPermutations[1][i+1:]])
        itr += 1 


for i in finalPermutations:
        output.append(i[0])

print("\n")
print("\n")
print("\n")
print(output)
