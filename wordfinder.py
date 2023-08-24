"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """Retrieves random words from a dictionary (file)."""

    def __init__(self, path):
        """Init the WordFinder. Use path to load words array."""
        self._path = path
        with open(path, 'r') as f:
            words = f.readlines()
            self._words = [word.strip() for word in words]

    def random(self):
        """Retrieves a random word from the words array."""
        return random.choice(self._words)


class SpecialWordFinder(WordFinder):
    """Retrieves random words from a dictionary (file) that are not blank lines or comments."""

    def __init__(self, path):
        """Super init the WordFinder. Update words array to remove blank lines and comments."""
        super().__init__(path)
        self._words = [word for word in self._words if not word.startswith('#') and len(word) > 0]


word_finder = WordFinder('words.txt')
print(word_finder.random())
print(word_finder.random())
print(word_finder.random())
print(word_finder.random())

special_word_finder = SpecialWordFinder('complex.txt')
print(special_word_finder.random())
print(special_word_finder.random())
print(special_word_finder.random())
