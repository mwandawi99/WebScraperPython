from bs4 import BeautifulSoup
import requests

# # #An example on how to send requests to a server and receive a repsonse back.
# url = "http://quotes.toscrape.com/"
# res = requests.get(url)
# #print(res)  ##<200> #prints out HTTP code

# #######Fetches Source Code by utilizing BeautifilSoup Library##########

# soup = BeautifulSoup(res.text,'html.parser')
# #print(soup) #prints all source code 
# #################################################
# soup.find('div') #to print out first div in the source code
# print(soup.find('h1').text) #prints out the text contained in the first header.


########Setting up virtual environment to install packages###########
#python -m venv env
#pip install requests
#pip install beautifulsoup4
################################################################

########Fetched content from a site using CSS selectors such as 'class'#############
url = "http://quotes.toscrape.com/"
res =requests.get(url)
soup=BeautifulSoup(res.text,'html.parser')
print(soup.find('h1').text)  
##First Heading(h1) Text 
print(soup.find('a',{'class':'tag'}).text) 
##returns the text from the anchor tag with class `tag`   
print(soup.find('div', {'class': 'tags'}))
##returns the first div tag with the class `tags`