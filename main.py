import pandas as pd
import pdfplumber

pdfPath = r"C:\Users\pandas\Pictures\Certificates\World Countries and Capital & Languages.pdf"
with pdfplumber.open(pdfPath) as pdf:
    print(pdf.metadata)
    print(pdf.pages)
    print(pdf.pages[0].extract_table()[1::])
