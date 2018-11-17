def get_highest_freq(file):
    f = open(file)
    freq_data = []
    for line in f:
        if line.strip().isalpha():
            freq_data.append([line.strip()])
        elif line.strip().isdigit():
            freq_data[-1].append(int(line.strip()))
    f.close()
    freq_data = quick_sort(freq_data, 1)
    return freq_data[0][0]


def quick_sort(array, index):
    if len(array) < 2:
        return array
    left = []
    right = []
    pivot = array[0]
    for i in range(1, len(array)):
        if array[i][index] > pivot[index]:
            left.append(array[i])
        else:
            right.append(array[i])
    return quick_sort(left, index) + [pivot] + quick_sort(right, index)



def amended_get_highest_freq(file):
    f = open(file)
    freq_data = []
    for line in f:
        if line.strip().isalpha():
            freq_data.append([line.strip()])
        elif line.strip().isdigit():
            freq_data[-1].append(int(line.strip()))
    f.close()
    freq_data = quick_sort(freq_data, 1)
    for i in range(1, len(freq_data)):
        if freq_data[i][1] < freq_data[0][1]:
            break
    freq_data = freq_data[:i]
    return [freq_data[i][0] for i in range(len(freq_data))]
