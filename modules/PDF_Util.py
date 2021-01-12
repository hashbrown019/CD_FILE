import PyPDF2
import os

class pdf:
	def getpdf(pdf,page):
		pdfFileObj = open(pdf, 'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		print(pdfReader.numPages)
		pageObj = pdfReader.getPage(page) 
		return pageObj

	def pdfToImage(pdffile,page):
		doc = fitz.open(pdffile)
		page = doc.loadPage(page-1)
		pix = page.getPixmap()
		output = "assets/temp/temp.png"
		ret = pix.writePNG(output)
		return ret
