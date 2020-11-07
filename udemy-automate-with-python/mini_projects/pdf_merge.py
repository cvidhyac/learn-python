# Demo file for PDF merge
# Concatenates two pdf files by appending content one below the other
# Because the PDF file format is

import PyPDF2


def read_pdf(file_path):
    file_one = open(file_path, "rb")
    return PyPDF2.PdfFileReader(file_one)


def append_pages_to_writer(pdf_reader, pdf_writer):
    for page_num in range(pdf_reader.numPages):
        pdf_writer.addPage(pdf_reader.getPage(page_num))
    return pdf_writer


def pdf_merge():
    pdf_reader_one = read_pdf(".././resources/sample_file.pdf")
    pdf_reader_two = read_pdf(".././resources/sample_file2.pdf")
    output_file = open(".././resources/combined_file.pdf", "wb")
    writer = PyPDF2.PdfFileWriter()
    writer = append_pages_to_writer(pdf_reader_one, writer)
    writer = append_pages_to_writer(pdf_reader_two, writer)
    writer.write(output_file)


pdf_merge()

