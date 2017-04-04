
# I dropped biology for a reason.

def bio_sucks():
    file_name = input("Exact File Name (incl. the txt):    ")
    f = open(file_name,"r")
    after_origin = False
    sequence = ""
    for line in f:
        for i in line.split():
            if i.lower() == "origin":
                after_origin = True
            elif i == "//":
                break
            elif after_origin is True:
                try:
                    int(i)
                except ValueError:
                    sequence += i
                else:
                    continue
                
    sequence = sequence[:len(sequence)]
    return sequence

print(bio_sucks())
