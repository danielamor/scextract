# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import scExtract
import csvCreator

__author__="Daniel"
__date__ ="$14 mai 2014 23:01:54$"

if __name__ == "__main__":
    sc = scExtract.ScExtract("rtpmomo")
    list = sc.scan()
    print (csvCreator.CsvCreator(list))
