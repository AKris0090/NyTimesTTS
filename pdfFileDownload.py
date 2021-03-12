import pdfkit
import os


def makePDF(link):
    try:
        os.mkdir(r"C:/Users/arjoo/PycharmProjects/NyTimesTTS/PDF")
    except FileExistsError:
        print("made directory already")
    name = r"PDF/article.pdf"
    path = r'C:/Users/arjoo/PycharmProjects/NyTimesTTS/wkhtmltopdf/bin/wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path)
    pdfkit.from_url(link, name, configuration=config)
    return name
