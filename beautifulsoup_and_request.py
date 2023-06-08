#makes the html text better readable
from bs4 import BeautifulSoup
#fetch the website data
import requests

#fetch the data from the webpage
livedata=requests.get('https://frame.work/de/de/blog').text
#converts the data to
ConvertToBetterlHtmlText=BeautifulSoup(livedata,'lxml')

#filter out the informations for headline, date of the post and a short teaser text 
headline=ConvertToBetterlHtmlText.find(class_="grid gap-20").find_all(class_="font-semibold text-3xl lg:text-5xl leading-9 lg:leading-tight text-black")
date=ConvertToBetterlHtmlText.find(class_="grid gap-20").find_all(class_="pl-2")
text=ConvertToBetterlHtmlText.find(class_="grid gap-20").find_all(class_="text-base pt-2 pb-8")


  
#Displays all News posts from the Newspage from Framework
for i, headline in enumerate(headline):  
    print(f'\n{headline.text}\n{date[i].text}\n\n{text[i].text}')


