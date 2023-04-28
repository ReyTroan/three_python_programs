from PyPDF2 import PdfWriter, PdfReader
from getpass import getpass

pdfwriter = PdfWriter()
pdf = PdfReader('file.pdf')

for page in range(len(pdf.pages)):
    pdfwriter.add_page(pdf.pages[page])

password = getpass(prompt='Введите пароль: ')
pdfwriter.encrypt(password)

with open('guarded.pdf', 'wb') as file:
    pdfwriter.write(file)