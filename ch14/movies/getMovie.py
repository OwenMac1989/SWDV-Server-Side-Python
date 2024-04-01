from dataclasses import dataclass

@dataclass
class Movie:
    title:str = ""
    year:int = 1900

    def getStr(self):
        return f"{self.title} ({self.year})"
        
        