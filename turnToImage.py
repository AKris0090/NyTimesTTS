from pdf2image import convert_from_path
import os


def convertToJPG(path):
    try:
        os.mkdir(r"C:/Users/arjoo/PycharmProjects/test/PDImage")
    except FileExistsError:
        print("made that too...")
    name = r'PDImage/bufferImage'
    images = convert_from_path(path)
    for i in range(len(images)):
        images[i].save(name + str(i) + '.png', 'PNG')
    return name
