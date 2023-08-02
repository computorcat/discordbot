import requests
import random
from bs4 import BeautifulSoup

class RandomVerse:
    def __init__(self):
        pass

    def pull_verse(self):
        page = requests.get('https://dailyverses.net/random-bible-verse')
        soup = BeautifulSoup(page.content, 'html.parser')
        verse = soup.find(class_='v1') # v1 is the class of the verse
        verse = verse.text
        return verse
    
    def pull_quran(self):
        page = requests.get('http://ayatalquran.com/random')
        soup = BeautifulSoup(page.content, 'html.parser')
        verse = soup.find(id='aya_text')
        verse = verse.text
        return verse
    
    def rand_pull(self):
        rand = random.randint(0, 1)
        if rand == 0:
            return self.pull_verse()
        else:
            return self.pull_quran()
        
        

if __name__ == "__main__":
    scraper = RandomVerse()
    niv = scraper.rand_pull()
    print(niv)
