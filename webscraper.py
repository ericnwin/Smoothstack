# Author: Eric Nguyen
from bs4 import BeautifulSoup
import requests
'''
Web scrapping exercise
Rules of this Project :
1.	Extracting/Downloading the data from html page.
2.	Extracting a particular content in the webpage.
3.	Location of information of interest in the html page. Identify the common pattern.
4.	Give instructions to the extractor which class is title column
5.	Search by Tag and Tag by class.
6.	Search the text file with beautiful soup object.

Problem Statement :

Count the total number of views for a given video in youtube for a given keyword.
Keyword :python
'''

url = "https://www.youtube.com/results?search_query=python"
result = requests.get(url)
soup_object = BeautifulSoup(result.text, "html.parser")
print(soup_object.prettify())
