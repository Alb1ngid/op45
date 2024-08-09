#принципы ооп абстракция, множ наследование
from les3 import Nowella,Reads,Book

# супер класс - object

class Manga(Nowella):

    def reads(self):
        print(f'я люблю мангу: {self.title}')


manga=Manga('берсерк','кентаро миура',2500,'70x70')
# manga.reads()
# print(manga)
#MRO-порядок выполнения методов
# print(Manga.mro())
class Anime(Nowella,Reads):

    def __init__(self, title, author, price, pnj,name):
        Nowella.__init__(self,title, author, price, pnj)
        Reads.__init__(self,name)

    def reads(self):
        Book.reads(self)
        Reads.reads(self)

anime=Anime('Naruto','кисимото',2500,'70x70','beka')
print(anime)
anime.reads()
anime.anime()

print(Anime.mro())

# print(Anime.mro())

# не нарушать порядок наследования
# в цепочке классов только у одного класса должны быть магические методы


