#makes the html text better readable
from bs4 import BeautifulSoup
#fetch the website data
import requests

#fetch the data from the webpage
livedata=requests.get('https://frame.work/de/de/blog').text
#converts the data to
ConvertToBetterlHtmlText=BeautifulSoup(livedata,'lxml')

headline=ConvertToBetterlHtmlText.find(class_="grid gap-20").find_all(class_="font-semibold text-3xl lg:text-5xl leading-9 lg:leading-tight text-black")
date=ConvertToBetterlHtmlText.find(class_="grid gap-20").find_all(class_="pl-2")
text=ConvertToBetterlHtmlText.find(class_="grid gap-20").find_all(class_="text-base pt-2 pb-8")
#link=ConvertToBetterlHtmlText.find_all(class_="ocus:ring-1 focus:ring-dark-light text-dark-light whitespace-nowrap block flex justify-center items-center transition-colors duration-300 ease-in-out hover:no-underline disabled:cursor-not-allowed font-semibold focus:outline focus:outline-offset-2 focus:outline-2 focus:outline-on-surface rounded-full max-w-max min-w-min bg-white text-on-surface border-on-surface border hover:bg-surface-hover no-underline", href=True)

data=ConvertToBetterlHtmlText.find_all(class_="lg:flex justify-between items-center pt-16 lg:pt-24") 


  

for i, headline in enumerate(headline):  
    print(f'\n{headline.text}\n{date[i].text}\n\n{text[i].text}')


