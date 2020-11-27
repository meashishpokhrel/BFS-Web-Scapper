#COde Written by Ashish Pokhrel Roll 38

#Objective: 
# Completed Web Scrapper in BFS Appraoch

#At First let us import the Library:

import requests
from bs4 import BeautifulSoup 

#All the Links for the Scrapping in BBC
#BBC NEWS 
#Sub Category of News, Sports and more


print('***************************Scrapping BBC Webiste NEws, Sport and More in BFS**************************')
print("\n")
print('***************************BBC | NEWS |**************************')
print('***************************BBC | NEWS | Technology**************************')
print("\n")

#here We are targetting the URL That we are gonna SCarp
#Set inital Depth to 1
# THis targets the news category 
# and technology sub category of the BBC 
input_url = "https://www.bbc.com/news/technology/"
depth = 1
  
#Definning A Function Crawler 
#which scrapss the titles and headlines from the URL

def level_crawler(URL):
    URL = requests.get(URL)
    soup = BeautifulSoup(URL.text, 'html.parser')
    headlines = soup.select(".gs-c-promo-heading__title")
    #For headlines
    
    titles = set()
        
    for headline in headlines:
        titles.add(headline.get_text())
    
    return titles
    #This will be returning all the tiles scraped from the site

 # We have used a BFS approach 
    # considering the structure as 
    # a tree. It uses a queue based 
    # approach to traverse 
    # links upto a particular depth. 
    
queue = [] 
queue.append(input_url) 
for j in range(depth): 
    for count in range(len(queue)): 
        url = queue.pop(0)
        urls = level_crawler(url)
        for i in urls: 
            queue.append(i) 

#This will print inly 15 headings from 
# the tiles set stores in queuew. 
for item in (queue[:15]):
    print(item)

print('***************************BBC | NEWS | ELECTION**************************')


#here We are targetting the URL That we are gonna SCarp
#Set inital Depth to 1
input_url = "https://www.bbc.com/news/election/"
depth = 1
  

#This is the BFS Approach
queue = [] 
queue.append(input_url) 
for j in range(depth): 
    for count in range(len(queue)): 
        url = queue.pop(0)
        urls = level_crawler(url)
        for i in urls: 
            queue.append(i) 


for item in (queue[:15]):
    print(item)

print("\n")
print('***************************BBC | NEWS | BUSINESS**************************')

input_url = "https://www.bbc.com/news/business"
depth = 1

#This is the BFS Approach

queue = [] 
queue.append(input_url) 
for j in range(depth): 
    for count in range(len(queue)): 
        url = queue.pop(0)
        urls = level_crawler(url)
        for i in urls: 
            queue.append(i) 

for item in (queue[:15]):
    print(item)

print("\n")
print('***************************BBC | SPORTS |**************************')
print('***************************BBC | SPORTS | TENNIS**************************')



input_url1 = "https://www.bbc.com/sport/tennis"
depth = 1
  
# Set for storing urls with different domain 
#links_extern = set() 

#This is the BFS Approach

queue = [] 
queue.append(input_url1) 
for j in range(depth): 
    for count in range(len(queue)): 
        url = queue.pop(0)
        urls = level_crawler(url)
        for i in urls: 
            queue.append(i) 

for item in (queue[:15]):
    print(item)
print("\n")
print('***************************BBC | SPORTS | CRICKET**************************')
# Set for storing urls with same domain 

input_url1 = "https://www.bbc.com/sport/cricket"
depth = 1
  
# Set for storing urls with different domain 
#links_extern = set() 

#This is the BFS Approach

queue = [] 
queue.append(input_url1) 
for j in range(depth): 
    for count in range(len(queue)): 
        url = queue.pop(0)
        urls = level_crawler(url)
        for i in urls: 
            queue.append(i) 

for item in (queue[:15]):
    print(item)
print("\n")
print('***************************BBC | SPORTS | GOLF**************************')
# Set for storing urls with same domain 

input_url1 = "https://www.bbc.com/sport/golf"
depth = 1
  
# Set for storing urls with different domain 
#links_extern = set() 

#This is the BFS Approach

queue = [] 
queue.append(input_url1) 
for j in range(depth): 
    for count in range(len(queue)): 
        url = queue.pop(0)
        urls = level_crawler(url)
        for i in urls: 
            queue.append(i) 

for item in (queue[:15]):
    print(item)

# Completed Web Scrapper in BFS Appraoch


