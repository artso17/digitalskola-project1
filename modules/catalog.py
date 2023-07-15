from .library_items import LibraryItem
from .book import Book
from .magazine import Magazine
from .cd import Cd
from .dvd import Dvd

class Catalog:
    def __init__(self,catalogs):
        self.catalogs = catalogs

    def search(self,input_search):
        list_results = []
        for catalog in self.catalogs:
            for item in catalog:
                if input_search in item.title.lower():
                    if type(item) == Book:
                        list_results.append( f'Title: {item.title}, DDS Number: {item.dds_num}, Type Catalog: {item.__class__.__name__}')
                    elif type(item) == Magazine:
                        list_results.append( f'Title: {item.title}, Volume: {item.volume}, Type Catalog: {item.__class__.__name__}')
                    elif type(item) == Cd:
                        list_results.append( f'Title: {item.title}, Artist: {item.artist}, Type Catalog: {item.__class__.__name__}')
                    elif type(item) == Dvd:
                        list_results.append( f'Title: {item.title}, Genre: {item.genre}, Type Catalog: {item.__class__.__name__}')

        return list_results
                    