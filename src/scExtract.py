# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Daniel"
__date__ ="$14 mai 2014 23:04:51$"

import urllib.request
import re
import workClass
from enum import Enum
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
        previousLen = 0

        #each page
        #for page in range(1, int(page)+2):
        for page in range(1, 2):
                #extract each Type               
                soup = self.getSoup(self.accountName, page)
                #extract movies and notes class
                names = soup.findAll(attrs= {"class" : "elco-anchor" })
                notes = soup.findAll("span", {"class" : "elrua-useraction-inner only-child" })
                years = soup.findAll("span" , {"class" : "elco-date"})
                directors = soup.findAll("a" , {"class" : "elco-baseline-a"})

                
                noteindex = 1

                for index in range(len(names)):
                    note = re.sub(r'\s+', '', notes[noteindex].string)
                    name = names[index].string
                    year = re.search(r"(?<=\().*?(?=\))", years[index].string).group(0)
                    type = re.search(r"^(?:\\.|[^/\\])*/((?:\\.|[^/\\])*)/", names[0]['href']).group(1)    
                    if type == "film" or type == "serie":
                        director = ""
                        for dir in directors[index]:
                            director += dir.string + ','
                        list.append(workClass.Movie(name, director, year, note))
                    noteindex+=2
                        
                        
                for t in list:
                    print (t.GetList() + '/n')


