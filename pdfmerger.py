import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    # instantiate pdf writer
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(f'./pdfs/{pdf}')
    merger.write('./pdfs/merged.pdf')


pdf_combiner(inputs)

exit()
