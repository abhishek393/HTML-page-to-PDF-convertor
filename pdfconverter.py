from bs4 import BeautifulSoup
from PyPDF2 import PdfFileMerger
import pdfkit
import requests
import re
import os

resp = requests.get("http://www.tangowithdjango.com/book17/")
soup=BeautifulSoup(resp.text,'html.parser')
link_no=0
book_link = []
for tag in soup.find_all('div',class_="toctree-wrapper compound"):
    ul_tag=tag.contents[1]
    li_tag=ul_tag.contents[1]
    while li_tag.next_sibling.next_sibling != None:
        li_tag = li_tag.next_sibling.next_sibling
        link = li_tag.contents[0].get('href')
        if str(link).find('.html#') == -1:
            pdfkit.from_url("http://www.tangowithdjango.com/book17/"+ link , 'Book'+ str(link_no) + '.pdf')
            book_link.append('Book' + str(link_no) + '.pdf')
            link_no = link_no+1

merger = PdfFileMerger()
for pdf in book_link:
    merger.append(pdf)
    os.remove(pdf)

merger.write("Final_Book.pdf")

    

    


