from modules.book import Book
from modules.cd import Cd
from modules.dvd import Dvd
from modules.magazine import Magazine
from modules.catalog import Catalog
import json

book1 = Book('1345-4555',
             'John doe',
             'book1 title',
             '0882378111',
             'book1 subject',
             )

book2 = Book('1345-4552',
             'Max doe',
             'book2 title',
             '0882378222',
             'book2 subject',
             )

book3 = Book('1345-4553',
             'Denny doe',
             'book3 title',
             '0882378333',
             'book3 subject',
             )


magazine1 = Magazine(volume     = '1',
                     issue      = 'edisi 1 jan 2001',
                     title      = 'magazine1 title',
                     subject    = 'magazine1 subject'
                     )

magazine2 = Magazine(volume     = '2',
                     issue      = 'edisi 2 jan 2002',
                     title      = 'magazine2 title',
                     subject    = 'magazine2 subject'
                     )

magazine3 = Magazine(volume     = '3',
                     issue      = 'edisi 3 jan 2003',
                     title      = 'magazine3 title',
                     subject    = 'magazine3 subject'
                     )

cd1 = Cd(artist     = 'artist1',
         title      = 'cd1 title',
         subject    = 'cd1 subject'
         )

cd2 = Cd(artist     = 'artist2',
         title      = 'cd2 title',
         subject    = 'cd2 subject'
         )

cd3 = Cd(artist     = 'artist3',
         title      = 'cd3 title',
         subject    = 'cd3 subject'
         )

dvd1 = Dvd(actors   = 'actor1',
           director = 'director1',
           genre    = 'genre1',
           title    = 'dvd1 title',
           subject  = 'dvd1 subject'
           )

dvd2 = Dvd(actors   = 'actor2',
           director = 'director2',
           genre    = 'genre2',
           title    = 'dvd2 title',
           subject  = 'dvd2 subject'
           )

dvd3 = Dvd(actors   = 'actor3',
           director = 'director3',
           genre    = 'genre3',
           title    = 'dvd3 title',
           subject  = 'dvd3 subject'
           )

books       = [book1,book2,book3]
magazines   = [magazine1,magazine2,magazine3]
cds         = [cd1,cd2,cd3]
dvds        = [dvd1,dvd2,dvd3]

f = open('files/data.json')
data = json.load(f)
for i in data:
    if i['catalog'] == 'book':
        books.append(Book(isbn      = i['isbn'],
                          authors   = i['authors'],
                          dds_num   = i['dds_num'],
                          title     = i['title'],
                          subject   = i['subject'],
                          )
        )
    elif i['catalog'] == 'magazine':
        magazines.append(Magazine(volume    = '1',
                                  issue     = i['issue'],
                                  title     = i['title'],
                                  subject   = i['subject']
                                  )
            
        )
    elif i['catalog'] == 'cd':
        cds.append(Cd(artist    = i['artist'],
                      title     = i['title'],
                      subject   = i['subject']
                      )
        )
    elif i['catalog'] == 'dvd':
        dvds.append(Dvd(actors  = i['actors'],
                        director= i['director'],
                        genre   = i['genre'],
                        title   = i['title'],
                        subject = i['subject']
           )
        )


catalogs    = [books,magazines,cds,dvds]
cat         = Catalog(catalogs=catalogs)
results     = cat.search('dvd')
for i in results: print(i)



