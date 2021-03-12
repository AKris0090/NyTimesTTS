import pytesseract
from PIL import Image
import os

miscellaneous = []
average = 0


def makeString(filePath):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\[USER]\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filePath))
    return text


def getText(filePath):
    file = open(filePath)
    return file.read()


def createFile(textStuff, name):
    try:
        os.mkdir(r"C:/Users/'[USER]'/PycharmProjects/test/TextFiles")
    except FileExistsError:
        print(" ")
    file = open(r"TextFiles/" + str(name), "w+")
    file.write(textStuff)
    file.close()


def split(text, delimiter):
    return text.split(delimiter)


def findBodyText(text):
    find = 'By '
    lines = split(text, "\n")
    index = 0
    try:
        while True:
            if find in lines[index]:
                break
            else:
                index += 1
    except IndexError:
        print('complete')
    find2 = "Contact Us:"
    index2 = 0
    try:
        while True:
            if find2 in lines[index2]:
                break
            else:
                index2 += 1
    except IndexError:
        print('')
    bodyText = ""
    for i in range((index + 1), index2 - 1):
        if "Frequently Asked Questions" not in lines[i]:
            bodyText += lines[i] + "\n"
    return bodyText
