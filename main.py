import pyttsx3
from pypdf import PdfReader  # or: from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfilename

book = askopenfilename()
pdfreader = PdfReader(book)
pages = len(pdfreader.pages)

speaker = pyttsx3.init()

for num in range(0, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()