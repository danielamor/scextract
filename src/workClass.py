# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Daniel"
__date__ ="$14 mai 2014 23:03:25$"

class Movie(object):
	def __init__(self, title, director, year, note):
            self.title  = title
            self.director = director
            self.year  = year
            self.note = note
	def GetList(self):
            return [self.title,self.director, self.year, self.note]

class Series(object):
	def __init__(self, title, director, year, note):
            self.title  = title
            self.director = director
            self.year  = year
            self.note = note
	def GetList(self):
            return [self.title,self.director, self.year, self.note]	
		
class Music(object):
	def __init__(self, title, artist, album, year, note):
            self.title  = title
            self.artist = artist
            self.album = album
            self.year  = year
            self.note = note
	def GetList(self):
            return [self.title, self.artist, self.album, self.year, self.note]	
		
class Book(object):
	def __init__(self, title, writer, editor, year, note):
            self.title = title
            self.writer = writer
            self.editor = editor
            self.note = note
            self.year = year
	def GetList(self):
            return [self.title, self.writer, self.editor, self.year, self.note]	
