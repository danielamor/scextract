# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Daniel"
__date__ ="$14 mai 2014 23:04:51$"

import urllib.request
import re
import time
import workClass
from bs4 import BeautifulSoup

class ScExtract(object):
    """Extract data from sc"""
    def __init__(self, accountName):
        self.accountName = accountName

    def getSoup(self, name , page):
        html = urllib.request.urlopen('http://www.senscritique.com/' + name + '/collection/rating/all/all/all/all/all/list/page-' + str(page) + '/').read()    
        return BeautifulSoup(html)
    
    def getNbrPages(self):
        #get soup from url
        soup = self.getSoup(self.accountName, 1)
        #get number of total pages to extract
        pages = soup.findAll(attrs= {"class" : "eipa-anchor" })
        page = (pages[len(pages)-1].string).split('.')[3]
        return page

    def scan(self):
        page = self.getNbrPages()
        list = []
        
        #each page

        lastlenght = 0
        #for page in range(1, 2):
        for page in range(1, int(page)+2):
                time.sleep(1)
                print(len(list)-lastlenght)
                lastlenght=(len(list))
                #Extract all page               
                soup = self.getSoup(self.accountName, page)
           
                #Get parents of all items
                parents = soup.findAll(attrs= {"class" : "elco-collection-item" })              

                #each item
                for index in range(len(parents)):                 
                    #Extract data from ONLY the parent
                    names = parents[index].findAll(attrs= {"class" : "elco-anchor" })
                    notes = parents[index].findAll("span", {"class" : "elrua-useraction-inner only-child" })
                    years = parents[index].findAll("span" , {"class" : "elco-date"})
                    directors = parents[index].findAll("a" , {"class" : "elco-baseline-a"})
                       
                                          
                    #Extract value
                    name = names[0].string
                    note = re.sub(r'\s+', '', notes[1].string)
                    type = re.search(r"^(?:\\.|[^/\\])*/((?:\\.|[^/\\])*)/", names[0]['href']).group(1)   
                    
                    #Detect if years is not display on website
                    if years:
                        year = re.search(r"(?<=\().*?(?=\))", years[0].string).group(0)   
                    else:
                        year = ""

                    director = ""   
                    for dir in range (len(directors)):
                        if dir < len(directors)-1:
                            director += directors[dir].string + ', ' 
                        else: 
                            director += directors[dir].string
                    
                    list.append(workClass.Work(type, name, director, year, note, names[0]['href']))

        print(len(list))                
        return list                        


