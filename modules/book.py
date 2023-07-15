from .library_items import LibraryItem

class Book(LibraryItem):
    def __init__(self,isbn,authors,dds_num,title,subject):
        super().__init__(title,None,subject)
        self.isbn       = isbn
        self.authors    = authors
        self.dds_num    = dds_num
    
