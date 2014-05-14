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
        list = {}
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

                #movie name
                print (names[0].string)
                #note
                print (re.sub(r'\s+', '', notes[1].string))
                #directors
                print (directors[0].string)
                             
                #type name             
                #extract from names the href work type
                type = re.search(r"^(?:\\.|[^/\\])*/((?:\\.|[^/\\])*)/", names[0]['href']).group(1)
                
                #year
                year = re.search(r"(?<=\().*?(?=\))", years[0].string).group(0)


                noteindex = 1

                for index in names:
                    if type == "films":
                        workClass.Movie(names[index].string, directors[index])

                        
                        list.append(workClass.Movie())


