import pandas as pd
import pdfplumber

pdfPath = r"C:\Users\pandas\Pictures\Certificates\World Countries and Capital & Languages.pdf"
pdf = pdfplumber.open(pdfPath)
# print(pdf.metadata)
# print(pdf.pages)
# print(pdf.pages[0].extract_table()[1::])

pages = pdf.pages.extract_table()

country = []
capital = []
currency = []
primaryLang = []

for j in range(len(pages)):
    for i in range(len(pages[j].extract_table())):
        country.append(pages[j].extract_table()[i][0])
        capital.append(pages[j].extract_table()[i][1])
        currency.append(pages[j].extract_table()[i][-2])
        primaryLang.append(pages[j].extract_table()[i][-1])