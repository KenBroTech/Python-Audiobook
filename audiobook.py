import pyttsx3
import PyPDF2
book = open('book.pdf', 'rb')
bookPDF = PyPDF2.PdfFileReader(book)
totalPage = bookPDF.getNumPages()
speaker = pyttsx3.init()
for num in range(totalPage):
    getPage = bookPDF.getPage(num)
    getText = getPage.extractText()
    speaker.say(getText)
    speaker.runAndWait()
