import pandas as pd # library for data manipulation
import pdfplumber # library for scraping pdfs
from tqdm import tqdm
import time

pdfPath = r"C:\Users\pandas\Pictures\Certificates\World Countries and Capital & Languages.pdf"


# method to get the path of the PDF and return pages data
def __get_pdf_path__(path):
    pdf = pdfplumber.open(pdfPath)
    # print(pdf.metadata)
    # print(pdf.pages)
    pages = pdf.pages  # .extract_table()
    return pages


# method to extract data from pages and save in list
def __extract_pages__(pages):
    country = []
    capital = []
    currency = []
    language = []

    # loop to extract all pages of the pdf. and return lists of columns head
    for j in range(len(pages)):
        print(f"PDF Extraction in progress...Page {j+1}..")
        for i in range(len(pages[j].extract_table())):
            country.append(pages[j].extract_table()[i][0])
            capital.append(pages[j].extract_table()[i][1])
            currency.append(pages[j].extract_table()[i][-2])
            language.append(pages[j].extract_table()[i][-1])

    return country, capital, currency, language


# dictionary for creating final repository
pdf_dict = {
    'country': [],
    'capital': [],
    'currency': [],
    'language': []
}


# methond to add data into a dictionary and return a pandas dataframe
def __create_repository__(country, capital, currency, language):
    pdf_dict['country'].extend(country)
    pdf_dict['capital'].extend(capital)
    pdf_dict['currency'].extend(currency)
    pdf_dict['language'].extend(language)

    # creating a pandas dataframe
    return pd.DataFrame(pdf_dict)


# methods of binding all methods together
def __process__(path):
    country, capital, currency, language = __extract_pages__(__get_pdf_path__(path))
    df = __create_repository__(country, capital, currency, language)
    print(df.head())
    df.to_csv("countries dataset.csv", index=False)
    df.to_csv("countries dataset.txt", index=False, sep="\n")


# instantiating the extraction process
__process__(pdfPath)