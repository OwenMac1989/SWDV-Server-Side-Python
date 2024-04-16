from dataclasses import dataclass

# must be coded before Book class, as Book class has an Authors type hint
# isn't a data class because has an attribute that's a list
class Authors:
    def __init__(self):
        self.__list = []

    def add(self, author):
        self.__list.append(author)

    @property
    def count(self):
        return len(self.__list)
    def __str__(self):
        ## aStr = String of Authors
        aStr = ""
        ##a = Author
        for a in self.__list:
            aStr += str(a) + ", "
        aStr = aStr[:-2]
        return aStr
    def __iter__(self):
        for a in self.__list:
            yield a
    
@dataclass
class Book:
    title:str = ""
    authors:Authors = None

    def __str__(self):
        return f"{self.title} by {self.authors}"
    
@dataclass
class Author:
    firstName:str = ""
    lastName:str = ""
    def __str__(self):
        s = self
        return f"{s.firstName} {s.lastName}"




