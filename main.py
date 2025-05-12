import pyttsx3
import PyPDF2
from tkinter.filedialog import *
from tkinter import *



file = askopenfilename()

pdfreader = PyPDF2.PdfReader(file)
numPages = len(pdfreader.pages)

for num in range(0,numPages):
    page = pdfreader.pages[num]
    text = page.extract_text()

    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()
