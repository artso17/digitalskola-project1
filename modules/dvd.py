from .library_items import LibraryItem

class Dvd(LibraryItem):
    def __init__(self,actors,director,genre,title,subject):
        super().__init__(title,None,subject)
        self.actors     = actors
        self.director   = director
        self.genre      = genre
