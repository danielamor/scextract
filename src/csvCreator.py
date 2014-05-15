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
        with open('sc.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for value in list:
                array = value.GetList()
                spamwriter.writerow([array[0], array[1], array[2], array[3], array[4]])


