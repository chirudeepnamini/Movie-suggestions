import openpyxl,secrets
import streamlit as st
tolerance=st.slider("select a rating",5,9)
if tolerance==5:
	file_name='g5.xlsx'
if tolerance==6:
	file_name='g6.xlsx'
if tolerance==7:
	file_name='g7.xlsx'
if tolerance==8:
	file_name='g8.xlsx'
if tolerance==9:
	file_name='g9.xlsx'
wb=openpyxl.load_workbook(file_name)
sheet=wb['Sheet']
col=sheet['A']
tconst=col[secrets.randbelow(sheet.max_row)].value
from bs4 import BeautifulSoup
import requests
url="https://www.imdb.com/title/"+tconst
print(url)
r=requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
title=soup.find('h1',attrs={'class':""})
name=title.text.split('\xa0')[0]
year=title.text.split('\xa0')[1]
plot=soup.find('div',attrs={'class':"summary_text"})
actual_plot=' '.join(plot.text.split())
attvalue=name+" Poster"
imgtag=soup.find('img',attrs={'title':attvalue})
imgurl=imgtag.get('src')
print(imgurl)
st.write(url)
st.write(name)
st.write(year[1:-2])
st.write(actual_plot)
st.markdown("![couldn't load image](imgurl)")