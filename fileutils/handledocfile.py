import os

import docx

print(os.getcwd())
doct=docx.Document('C:\\Users\\1003633\Desktop\\docfile.docx')
para=doct.paragraphs[0].text
print(para[0])
