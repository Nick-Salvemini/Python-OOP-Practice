"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    '''
    A class that takes a file path for a text file with lines of words, returns how many words are in the file, and stores them in a list to return words from the file randomly

    Attributes
    ____________________________
    path: str
        the file path to the text file with a list of words
    ____________________________
    '''

    word_list = []

    def __init__(self, path):
        self.path = path

        self.count_and_list_words()

    def __str__(self):
        return f'Read and store the file located at {self.path}'
    
    def count_and_list_words(self):
        '''
        Searches for the file in the path, creates a count of how many words are in the file and returns the count in a string, and adds each word into a list


        '''
        count = 0
        file = open(self.path)

        for line in file:
            count += 1
            self.word_list.append(line.strip('\n'))

        file.close()

        print(f'{count} words read') 

    def random(self):
        '''
        Returns a random word from the list of words generated at instantiation
        '''
        return choice(self.word_list)

class SpecialWordFinder(WordFinder):
    '''
    A version of the WordFinder class that also takes into account blank or commented-out lines
    '''
    def __init__(self, path):
        super().__init__(path)
    
    def count_and_list_words(self):
        '''
        Differs from the super-class version by adding a step to confirm that the line is not empty or commented out (starts with a #)
        '''
        count = 0
        file = open(self.path)

        for line in file:
            if line.strip() and line.startswith('#') == False:
                count += 1
                self.word_list.append(line.strip('\n'))

        file.close()

        print(f'{count} words read')