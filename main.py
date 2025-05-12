import pyttsx3
import PyPDF2
from tkinter.filedialog import *
from tkinter import *
import tkinter.font as tkFont


def getFile():
    file = askopenfilename(filetypes=[("PDF file", "*.pdf")])

    playFile(file)

def setVolume(percentage):
    player.setProperty("volume", int(percentage)/100)

def setSpeed(wordsPerMinute):
    player.setProperty("rate", int(wordsPerMinute))

def playFile(pdfFile):

    pdfreader = PyPDF2.PdfReader(pdfFile)
    numPages = len(pdfreader.pages)

    for num in range(0,numPages):
        page = pdfreader.pages[num]
        text = page.extract_text()

        player.say(text)
        player.runAndWait()

player = pyttsx3.init()

window = Tk()
window.geometry("800x600")
window.title("PDF TTS")
window.config(background="black")

main_font = tkFont.Font(family="Arial", size=25)
secondary_font = tkFont.Font(family="Arial", size=15)

buttonLabel = Label(window, text="Click the button to get started",background="black", fg="green", font=main_font)
buttonLabel.pack()

fileButton = Button(window, name="file", text="Select PDF", font=main_font, command=getFile)
fileButton.pack()

volumeLabel = Label(window, text="Volume", font=secondary_font, background="black", fg="green")
volumeLabel.pack()

volumeSlider = Scale(window, from_=0, to=100, orient="horizontal", command=setVolume)
volumeSlider.pack()

speedLabel = Label(window, text="Speed(Words per minute)", font=secondary_font, background="black", fg="green")
speedLabel.pack()

speedSlider = volumeSlider = Scale(window, from_=150, to=300, orient="horizontal", command=setSpeed)
speedSlider.pack()


window.mainloop()
