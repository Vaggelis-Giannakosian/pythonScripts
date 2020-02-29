import PyPDF2

# CLEAN VERSION
writer = PyPDF2.PdfFileWriter()
watermark = PyPDF2.PdfFileReader(open('./pdfs/wtr.pdf','rb'))
mergedPdf = PyPDF2.PdfFileReader(open('./pdfs/merged.pdf','rb'))

for i in range(mergedPdf.getNumPages()):
    page = mergedPdf.getPage(i)
    page.mergePage(watermark.getPage(0))
    writer.addPage(page)

with open ('./pdfs/watermarked.pdf','wb') as newFile:
    writer.write(newFile)

exit()

# VERBOSE VERSION
with open('./pdfs/wtr.pdf', 'rb') as wtr:
    # get the watermark PageObject
    wtrReader = PyPDF2.PdfFileReader(wtr)
    wtr = wtrReader.getPage(0)

    with open('./pdfs/merged.pdf', 'rb') as file:
        # read the merged pdf
        mergedReader = PyPDF2.PdfFileReader(file)
        pagesCount = mergedReader.getNumPages()
        # iterate each page and add watermark
        for i in range(pagesCount):
            page = mergedReader.getPage(i)
            page.mergePage(wtr)
            writer.addPage(page)

        # save the result to another pdf
        with open('./pdfs/watermarked.pdf', 'wb') as newFile:
            writer.write(newFile)

exit()