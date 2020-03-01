import PyPDF2



# ROTATE PDF

# rb mode is in binary mode
with open('pdfs/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    print(reader.numPages)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('pdfs/crooked.pdf', 'wb') as newFile:
        writer.write(newFile)





exit()