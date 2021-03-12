import cv2 as cv
import os
from imageTranformation import toGray, toBinary, addVerticalGapLines, crop, applySharpenAndBlur
from makeText import makeString, findBodyText, createFile
from pdfFileDownload import makePDF
from segmentation import verticalWhiteGaps
from turnToImage import convertToJPG

link = 'https://www.nytimes.com/2021/03/10/us/politics/biden-covid-relief-bill.html'
binaryThresh = 254


def printArr(arr):
    for a1 in range(len(arr)):
        for b1 in range(len(arr[i])):
            print(arr[a1][b1], end=" ")
        print("\n")


def makeBWArray():
    path = makePDF(link)
    convertToJPG(path)


def getNumPages():
    count = 0
    while True:
        try:
            open(r"PDImage/bufferImage" + str(count) + ".png")
            count += 1
        except FileNotFoundError:
            return count


allText = ''
makeBWArray()
numPages = getNumPages()
for i in range(numPages):
    try:
        imgPath = r'PDImage/bufferImage'
        grayArray = toGray(imgPath, i)
        binaryArray = toBinary(grayArray, binaryThresh, i)
        verticalLineGaps = verticalWhiteGaps(binaryArray)
        addVerticalGapLines(verticalLineGaps, binaryArray, i)
        for j in range(len(verticalLineGaps) - 1):
            here = verticalLineGaps[j]
            nextOne = verticalLineGaps[j + 1]
            bounds = (here[1], nextOne[0])
            crop((imgPath + str(i) + ".png"), bounds[0], bounds[1], len(binaryArray[0]))
            try:
                img2 = applySharpenAndBlur(cv.imread(r"PDImage/temp.png"))
                cv.imwrite(r"PDImage/temp.png", img2)
                text = makeString(r'PDImage/temp.png')
                text = text.replace("\n", " ")
                allText += text + "\n"
            except TypeError:
                print('Page is blank!')
    except FileNotFoundError:
        break
    allText += "\n\n"
    print("Page " + str(i + 1) + " Done!")
os.remove(r"PDImage/temp.png")
createFile(allText, r"text")
body = findBodyText(allText)
createFile(body, r"bodyText")
