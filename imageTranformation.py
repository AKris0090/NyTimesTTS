import cv2 as cv


def applySharpenAndBlur(image):
    return cv.GaussianBlur(image, (1, 1), 0)


def crop(filePath, start, stop, pageWidth):
    length = stop - start
    img = cv.imread(filePath)
    croppedIMG = img[start:(start + length), 0: pageWidth]
    cv.imwrite(r"PDImage/temp.png", croppedIMG)
    return


def toGray(name, pageCount):
    imgGray = cv.imread(name + str(pageCount) + '.png', cv.IMREAD_GRAYSCALE)
    cv.imwrite(r'PDImage/gray' + str(pageCount) + '.png', imgGray)
    return imgGray


def toBinary(grayArray, thresh, pageCount):
    imgBinary = cv.threshold(grayArray, thresh, 255, cv.THRESH_BINARY)[1]
    cv.imwrite(r'PDImage/binary' + str(pageCount) + '.png', imgBinary)
    return imgBinary


def addVerticalGapLines(arr, arr2, pageCount):
    img = arr2.copy()
    imgLength = len(img[0])
    for i in range(len(arr)):
        start = arr[i][0]
        end = arr[i][1]
        cv.line(img, (0, start), (imgLength - 1, end), (0, 0, 255), 2)
    cv.imwrite(r'PDImage/withVerticalWhiteGaps' + str(pageCount) + '.png', img)


def addVerticalGapLines2(arr, arr2, pageCount):
    img = arr2.copy()
    imgLength = len(img[0])
    for i in range(len(arr)):
        start = arr[i][0]
        end = arr[i][1]
        cv.line(img, (0, start), (imgLength - 1, end), (0, 0, 255), 2)
    cv.imwrite(r'PDImage/combinedVGaps' + str(pageCount) + '.png', img)


def makeBlack(arr, arr2):
    img = arr2.copy()
    imgLength = len(img[0]) - 1
    for i in range(len(arr)):
        current = arr[i]
        for j in range(current[1] - current[0]):
            for k in range(imgLength):
                img[j + current[0]][k] = 0
    cv.imwrite(r'PDImage/v4.png', img)
