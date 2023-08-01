import requests
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

if __name__ == "__main__":
    scraper = RandomVerse()
    niv = scraper.pull_verse()
    print(niv)
