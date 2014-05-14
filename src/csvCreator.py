# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Daniel"
__date__ ="$14 mai 2014 23:04:07$"

import csv
class CsvCreator(object):
    """save all data to csv"""
    
    def __init__(self, array):
        self.array = array
        with open('sc.csv', 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';' , quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for key, value in array.items():
                spamwriter.writerow([unidecode(key), value])
        return super(csvCreator, self).__init__(*args, **kwargs)


