import PyPDF2
import pyttsx3

# Path to the PDF file
pdf_path = 'Crypto101.pdf'

# Read the PDF
pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
target_page = pdf_reader.pages[24]
text_content = target_page.extract_text()

# Initialize the text-to-speech engine
tts_engine = pyttsx3.init()

# Speak out the text
tts_engine.say(text_content)
tts_engine.runAndWait()
