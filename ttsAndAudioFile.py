import pyttsx3


def makeCohesive(text):
    textToReturn = ''
    pages = text.split("\n\n")
    for page in pages:
        textToReturn += page.replace("\n", " ") + "\n"
    return textToReturn


def toFile(text, fileName):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # setting up new voice rate
    engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

    # """VOICE"""
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male 1 for female

    engine.save_to_file(text, fileName)
    engine.runAndWait()
