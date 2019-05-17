"""
This module contains custom made classes for my research.
"""
class Artifact: #always use capital case when naming a class
	"""This is a base class for cultural objects."""
	artifact="cultural object"

	def __init__(self, title):
		self.title=title
		self.extant=True
		
	def __str__(self):
		return self.title
        

	def is_not_extant(self):
		self.extant=False
		
class Book(Artifact):
	"""This class describes a book object."""
	tpye="book"
	def __init__(self, title, year, author, filename):
		Artifact.__init__(self,title)
		self.author=author
		self.add_year(year)
		self.add_text(filename)
	
	def add_year(self, year):
		self.year=year
	def add_text(self,filename):
		with open(filename,'r') as rf:
			self.text=rf.read()
	def process(self):
		self.tokens = self.text.lower().spilit(" ")
	def clean(self,words_to_remove):
		for wrod in words_to_remove:
			self.tokens=[token for token in self.tokens if token != word]
	
	def divide(self):
		self.chapters=self.text.split("Chapter")
			
class Tapestry (Artifact):
	"""This class describes a tapestry object."""
	tpye="tapestry"
class Sculpture (Artifact):
	"""This class describes a sculpture object."""	
	tpye="sculpture"
class Song (Artifact):
	"""This class describes a song object."""
	tpye="song"
		
if __name__ == "__name__":
	a=Novel('my text','Hemmingway',1932,'text.txt','adventure')
a = Book("my book","1983","Lu Xun","text.txt")

a.clean(["it"])
print(a.tokens)
