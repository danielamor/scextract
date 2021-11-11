# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Daniel"
__date__ ="$14 mai 2014 23:03:25$"

class Work(object):
	def __init__(self, type, title, artist, year, note, href):
            self.type = type
            self.title  = title
            self.artist = artist
            self.year  = year
            self.note = note
            self.href = href
	def GetList(self):
            return [self.type, self.title, self.artist, self.year, self.note, self.href]
