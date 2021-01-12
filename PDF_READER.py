import PyPDF2 

reader = PyPDF2.PdfFileReader('assets/a.pdf')
print(reader)
print(reader.getPage(1).extractText())