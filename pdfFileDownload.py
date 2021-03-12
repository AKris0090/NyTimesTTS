import pdfkit


def makePDF(link):
    name = r"PDF/article.pdf"
    path = r'C:/Users/arjoo/PycharmProjects/test/wkhtmltopdf/bin/wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path)
    pdfkit.from_url(link, name, configuration=config)
    return name
