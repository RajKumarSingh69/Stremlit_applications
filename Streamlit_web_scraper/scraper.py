import streamlit as st
from bs4 import BeautifulSoup
import requests

st.markdown("<h1 style='text-align: center;'>Web Scraper</h1>", unsafe_allow_html=True)

# Creating form
with st.form("search"):
    keyword = st.text_input("Enter your keyword")
    search = st.form_submit_button("search")

placeholder=st.empty()
if search:
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup = BeautifulSoup(page.content, 'lxml')
    rows = soup.find_all("div", class_="bugb2")
    col1,col2=placeholder.columns(2)
    print(f"Number of rows found: {len(rows)}")
    #img class name:-SpgDA

    for row in rows:
        figures=row.find_all("figure")
        for i in range(2):
            img=figures[i].find("img",class_="I7OuT DVW3V L1BOa")
            lis=img['srcset'].split("?")
            if i==0:
                col1.image(lis[0])
            else:
                col2.image(lis[0])






