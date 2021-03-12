from pdf2image import convert_from_path


def convertToJPG(path):
    name = r'PDImage/bufferImage'
    images = convert_from_path(path)
    for i in range(len(images)):
        images[i].save(name + str(i) + '.png', 'PNG')
    return name
