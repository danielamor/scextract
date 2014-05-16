# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Daniel"
__date__ ="$14 mai 2014 23:04:51$"

import urllib.request
import re
import workClass
from bs4 import BeautifulSoup

class ScExtract(object):
    """Extract data from sc"""
    def __init__(self, accountName):
        self.accountName = accountName

    def getSoup(self, name , page):
        try:
            url = 'http://www.senscritique.com/' + name + '/collection/rating/all/all/all/all/all/list/page-' + str(page) + '/'
            html = urllib.request.urlopen(url).read()  
            return BeautifulSoup(html)
        except urllib.error.URLError as e:
            print('Url error: %s | %s' %(url, e))
        except urllib.error.HTTPError as e:
            print('Http error: %s | %s' %(url, e))        

    def getNbrPages(self):
        try:
            #get soup from url
            soup = self.getSoup(self.accountName, 1)
            #get number of total pages to extract
            pages = soup.findAll(attrs= {"class" : "eipa-anchor" })
            page = (pages[len(pages)-1].string).split('.')[3]
            return page
        except BaseException:
            print("Nbr pages extraction fail")
            return 0

    def scan(self):
        page = self.getNbrPages()
        list = []
        
        #each page
        for page in range(1, int(page)+2):          
                try:
                    #Extract all page               
                    soup = self.getSoup(self.accountName, page)
                    
                    #Get parents of all items
                    parents = soup.findAll(attrs= {"class" : "elco-collection-item" })    
                except BaseException:
                    print("Page extraction fail")
                    break

                #each item
                for index in range(len(parents)):   
                    try:
                        #Extract data from ONLY the parent
                        names = parents[index].findAll(attrs= {"class" : "elco-anchor" })
                        notes = parents[index].findAll("span", {"class" : "elrua-useraction-inner only-child" })
                        years = parents[index].findAll("span" , {"class" : "elco-date"})
                        directors = parents[index].findAll("a" , {"class" : "elco-baseline-a"})
                    except BaseException:
                        print("Children extraction fail")
                        break
                        
                    try:
                        #Extract value
                        name = names[0].string
                    except BaseException:
                        name = ""
                    
                    try:
                        note = re.sub(r'\s+', '', notes[1].string)
                    except BaseException:
                        note = ""
                        
                    try:
                        type = re.search(r"^(?:\\.|[^/\\])*/((?:\\.|[^/\\])*)/", names[0]['href']).group(1)   
                    except BaseException:
                        type = ""
                        
                    #Detect if years is not display on website
                    try:
                        year = re.search(r"(?<=\().*?(?=\))", years[0].string).group(0) 
                    except BaseException:
                        year = ""
                        
                    try:
                        href = names[0]['href']
                    except BaseException:
                        href = ""

                    director = ""   
                    for dir in range (len(directors)):
                        if dir < len(directors)-1:
                            director += directors[dir].string + ', ' 
                        else: 
                            director += directors[dir].string
                    
                    list.append(workClass.Work(type, name, director, year, note, href))
                    print('Page %s done' % page)
        print(len(list))                
        return list                        


