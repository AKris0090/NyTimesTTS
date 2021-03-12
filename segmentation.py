def verticalWhiteGaps(arr):
    lineCount = 0
    yValLineGaps = []
    lastFullWhite = 0
    lastLineWhite = True
    while lineCount < len(arr):
        if not checkFullWhite(arr[lineCount]) and lastLineWhite:
            yValLineGaps.append((lastFullWhite, lineCount - 1))
            lastLineWhite = False
        elif not lastLineWhite and checkFullWhite(arr[lineCount]):
            lastFullWhite = lineCount - 1
            lastLineWhite = True
        lineCount += 1
    length = len(arr)
    try:
        lineCount = length - 1
        while checkFullWhite(arr[lineCount]):
            lineCount -= 1
        yValLineGaps.append((lineCount, len(arr)))
        return yValLineGaps
    except IndexError:
        print('Page is blank!')


def checkFullWhite(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            return False
    return True
