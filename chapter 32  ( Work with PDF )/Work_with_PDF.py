import PyPDF2

############## READ PDF FILE

my_file=open("chapter 0.pdf","rb")

pdf_reader=PyPDF2.PdfFileReader(my_file)


# print no. of pages

print(pdf_reader.numPages)

# Read pdf page by page

page_one=pdf_reader.getPage(0)
print(page_one.extractText())

# Read full pdf

for i in range(pdf_reader.numPages) :
    pages=pdf_reader.getPage(i)
    print(pages.extractText())


##### WRITE PDF FILE

pade1=pdf_reader.getPage(0)

output_file=open("new_pdf.pdf","wb")


pdf_writer=PyPDF2.PdfFileWriter()

pdf_writer.addPage(pade1)
pdf_writer.write(output_file)



my_file.close()
output_file.close()