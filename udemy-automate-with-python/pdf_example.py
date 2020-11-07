# Usage of pypdf2
# Uses a PdfFileReader and PdfFileWriter similar to Java IO streams
# We use a os.open file to read the file as a binary stream (rb/wb)
# Content can be added or updated, but it cannot modify content owing to
# complex format in pdf

import PyPDF2
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def open_pdf_file(file_path):
    file_stream = open(file_path, 'rb')
    pdf_file = PyPDF2.PdfFileReader(file_stream)
    logging.info("Number of pages in file :" + str(pdf_file.numPages))

open_pdf_file("./resources/sample_file.pdf")
