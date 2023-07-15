from .library_items import LibraryItem

class Magazine(LibraryItem):
    def __init__(self,volume,issue,title,subject):
        super().__init__(title,None,subject)
        self.volume = volume
        self.issue  = issue
    
