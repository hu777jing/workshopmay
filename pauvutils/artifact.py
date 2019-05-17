"""
This module contains custom made classes for my research.
"""
class Artifact: #always use capital case when naming a class
    """This is a base class for cultural objects."""
    artifact="cultural object"
#    alist=[]
#a = Artifact()
#b = Artifact()
#print (a.alist, b.alist) 

#a.alist.append("yo!")

#print(a.alist)
#print(b.alist)
#    def __init__(self):
#	    self.title="A Book!"
#a = Artifact()
#b = Artifact()
#print (a.title)
#print (b.title)
#        self.tltle=title
    def __init__(self, title, filename):
        self.title=title
        with open(filename,'r') as rf:
            self.text = rf.read()
        self.process()
        self.index = 0
			
    def add_year(self, year):
        self.year=year
	
    def __str__(self):
        return self.title

    def process(self):
        self.tokens = self.text.lower().split(" ")
		
    def __iter__(self):
	    return self
	
    def __next__(self):
        if self.index < len(self.tokens):
            _index = self.index
            self.index += 1
            return self.tokens[_index]
        else:
            raise StopIteration

a = Artifact ("first book", "text.txt")
for word in a:
    print(word)
	
	
