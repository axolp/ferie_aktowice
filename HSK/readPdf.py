import PyPDF2

 
# creating a pdf file object
pdfFileObj = open('hsk789.pdf', 'rb')
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)
#pageObj = pdfReader.pages[10] 
# extracting text from page
#print(pageObj.extract_text())

f = open("hsk789.txt", "a",  encoding="utf-8")
for i in range(1, len(pdfReader.pages)):
    page= pdfReader.pages[i]
    #print(page.extract_text())
    try:
        f.write(str(page.extract_text())+'\n')
    except:
        f.write("error")

f.close()
 
# closing the pdf file object
pdfFileObj.close()