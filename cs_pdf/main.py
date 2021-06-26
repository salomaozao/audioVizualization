import PyPDF2 as reader
from PyPDF2.pdf import ContentStream
from PyPDF2.generic import TextStringObject
from PyPDF2.utils import isString, b_, u_, ord_, chr_, str_, formatWarning
import types


pdf = reader.PdfFileReader('sample.pdf')
pdf_complex = reader.PdfFileReader('P1_PER_MAT1_198a224_U4C12_EF1_SAB_PNLD23_LE_T.pdf')

pages = pdf_complex.pages

def findInDict(needle,haystack):
    for key in haystack.keys():
        try:
            value = haystack[key]
        except:
            continue
        if key == needle:
            return value
        if type(value) == types.DictType or isinstance(value,pyPdf.generic.DictionaryObject):  
            x = findInDict(needle,value)
            if x is not None:
                return x

answer = findInDict('/MYOBJECT',pdf.resolvedObjects).getData()

def extractText__():
    text = str("")
    content=pdf_complex.getPage(0)["/Contents"].getObject()
    if not isinstance(content, ContentStream):
        content = ContentStream(content, pdf_complex)
        print(content.operations[0])
        return text
    



print(f"""
{"_"*100}
{extractText__()}
{"_"*100}
""")

# {pdf_complex.getPage(0)["/Contents"].getObject()}
#Annotations references are in ...getPage(x)["/Annots"]
#Annotations are linked to some object. How to access this object?

