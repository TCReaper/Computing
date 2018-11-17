def ReadLog():
    file_handle = open("WEBLOG.txt")
    log_data = []
    for line in file_handle:
        name, date = line.strip().split("|")
        date = date.split(":")[0]
        for i in range(len(log_data)):
            if log_data[i][0] == name:
                for j in range(len(log_data[i][1])):
                    if log_data[i][1][j] == date:
                        break
                else:
                    log_data[i][1].append(date)
                break
        else:
            log_data.append([name, [date]])
    file_handle.close()
    return log_data

def ProcessLog():
    file_handle = open("SUMMARY.txt", "w")
    log_data = ReadLog()
    for data in log_data:
        file_handle.write("{0:<20}{1}".format(data[0], ",".join(data[1])) \
                          + "\n")
    file_handle.close()

    high = 0
    accessed_by = []
    for i in range(len(log_data)):
        if len(log_data[i][1]) > high:
            high = len(log_data[i][1])
            accessed_by = [log_data[i][0]]
        elif len(log_data[i][1]) == high:
            accessed_by.append(log_data[i][0])
    print("Highest frequency (days): ", high)
    print("Accessed by:")
    for name in accessed_by:
        print(name)
    
            
        
