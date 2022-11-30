import docx
import re
import openpyxl
from collections import defaultdict

 regular = "\d{0,}\.\d{2}\s*\грн"

 def changeRow_sub(new , parag):
     return re.sub(regular, str(new), parag.text)

 def changeRow(new , name):
     doc = docx.Document(name)
     for paragraph in doc.paragraphs:
         paragraph.text = changeRow_sub(new , paragraph)
     doc.save("WordFile2.docx")

 if __name__ =="__main__":
     new = "Have a good day!"
     changeRow(new , "WordFile.docx")