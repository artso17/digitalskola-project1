from .library_items import LibraryItem

class Cd(LibraryItem):
    def __init__(self,artist,title,subject):
        super().__init__(title,None,subject)
        self.artist = artist

    
