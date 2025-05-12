import pyttsx3
import PyPDF2
from tkinter.filedialog import *
from tkinter import *
import tkinter.font as tkFont


def getFile():
    file = askopenfilename(filetypes=[("PDF file", "*.pdf")])

    playFile(file)

def playFile(pdfFile):

    pdfreader = PyPDF2.PdfReader(pdfFile)
    numPages = len(pdfreader.pages)

    for num in range(0,numPages):
        page = pdfreader.pages[num]
        text = page.extract_text()

        player = pyttsx3.init()
        player.say(text)
        player.runAndWait()


window = Tk()
window.geometry("800x600")
window.title("PDF TTS")
window.config(background="black")

main_font = tkFont.Font(family="Arial", size=25)

testLabel = Label(window, text="Click the button to get started",background="black", fg="green", font=main_font)
testLabel.pack()

fileButton = Button(name="file", text="Select PDF", font=main_font)
fileButton.pack()

window.mainloop()
