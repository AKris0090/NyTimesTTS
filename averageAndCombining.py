def getAverage(arr):
    totalLength = 0
    for i in range(len(arr) - 1):
        current = arr[i]
        nextGap = arr[i + 1]
        totalLength += nextGap[0] - current[1]
    average = totalLength / (len(arr) - 1)
    return average


def combine(arr, average, thresh):
    newGaps = []
    for i in range(len(arr) - 1):
        current = arr[i]
        length = current[1] - current[0] # if size of text block is less than average,
        if not length <= (average - thresh):
            newGaps.append((current[0], current[1]))
    return newGaps
