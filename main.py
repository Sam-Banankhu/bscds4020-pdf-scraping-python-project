import pandas as pd
import pdfplumber
from tqdm import tqdm
import time

pdfPath = r"C:\Users\pandas\Pictures\Certificates\World Countries and Capital & Languages.pdf"


def __get_pdf_path__(path):
    pdf = pdfplumber.open(pdfPath)
    # print(pdf.metadata)
    # print(pdf.pages)
    # print(pdf.pages[0].extract_table()[1::])

    pages = pdf.pages.extract_table()

    return pages


def __extract_pages__(pages):
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

    return country, capital, currency, primaryLang

pdf_dict = {
    'country':[],
    'capital':[],
    'currency':[],
    'primaryLang':[]
}

def __create_repository__(country, capital, currency, primaryLang):
