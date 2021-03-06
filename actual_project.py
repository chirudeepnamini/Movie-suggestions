import openpyxl,secrets
import streamlit as st
def suggestion(tolerance):
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
	sheet=wb['Sheet1']
	col=sheet['A']
	tconst=col[secrets.randbelow(sheet.max_row)].value
	return tconst
tolerance=st.slider("select a rating",5,9)
tconst=suggestion(tolerance)
key="9e579f61"
from bs4 import BeautifulSoup
import requests,json
while(1):
	url="http://www.omdbapi.com/?i={}&apikey={}".format(tconst,key)
	r=requests.get(url)
	actcont=json.loads(r.content)
	if "Episode" in actcont:
		tconst=suggestion(tolerance)
		print(tconst)
	else:
		break
actual_plot=actcont["Plot"]
year=actcont["Year"]
name=actcont["Title"]
imgurl=actcont["Poster"]
imdb_url="https://www.imdb.com/title/"+tconst
st.write(name)
st.write(year)
st.write(actual_plot)
imdb_url='[Go to IMDB]'+'('+imdb_url+')'
st.markdown(imdb_url,unsafe_allow_html=True)
processed_name=name.split(' ')
processed_name='+'.join(processed_name)+'+'+year
google_url=google_url='https://www.google.com/search?q='+processed_name
google_url='[Go to google]'+'('+google_url+')'
st.markdown(google_url,unsafe_allow_html=True)
justwatch_url='https://www.justwatch.com/in/search?q='+processed_name
justwatch_url='[Search in justwatch]'+'('+justwatch_url+')'
st.markdown(justwatch_url,unsafe_allow_html=True)
st.image(imgurl,width=300)
