#from pypdf import PdfReader
import pdftotext
import sys
def extract_pdf_text(source,result=''):
#	pdf=PdfReader(source)
	pdf=pdftotext.PDF(source)
	text=''
#	for p in pdf.pages:
	for p in pdf:
#		text+=p.extract_text()+'\n'
		text+=p+'\n'
		print(p.extract_text()+'\n')
	if(result!=''):
		with open(result,'w') as file:
			file.write(text)
	else:
		return text
if  __name__=='__main__':
	if(1<len(sys.argv)):
		if(2<len(sys.argv)):
			extract_pdf_text(sys.argv[1],sys.argv[2])
		else:
			extract_pdf_text(sys.argv[1])
	else:
		print('no file names provided. Correct call is:\n\t<program name> <pdf to extract from> <file to write to *optional>')
