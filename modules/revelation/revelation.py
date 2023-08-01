import random
class Revelation:
    def __init__(self):
        pass

    def generate_revelation(self):
        # get dictionary.txt
        with open('modules/revelation/dictionary.txt', 'r') as f:
            dictionary = f.read()
        # split dictionary.txt into a list
        dictionary = dictionary.split('\n')
        # get random words from dictionary.txt
        # 5 times
        words = []
        for i in range(5):
            word = random.choice(dictionary)
            # add the words to a list
            words.append(word)
        # join the words in the list together with a line break
        words = '\n'.join(words)
        f.close()
        return words
    
if __name__ == "__main__":
    revelation = Revelation()
    print(revelation.generate_revelation())