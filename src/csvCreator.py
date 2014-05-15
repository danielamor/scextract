# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Daniel"
__date__ ="$14 mai 2014 23:04:07$"

import csv
class CsvCreator(object):
    """save all data to csv"""
    
    def __init__(self, list):
        self.list = list
        with open('sc.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for value in list:
                array = value.GetList()
                try:
                    spamwriter.writerow([array[0], array[1], array[2], array[3], array[4]])
                except Exception:
                    spamwriter.writerow([array[5]])
                    print(type,"","",array[3],array[4],array[5])
                    print ("Encoding error")

