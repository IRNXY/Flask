MIN_WORD_SIZE = 2 # min size of a word in the output

class Node(object):
    def __init__(self, letter='', final=False, depth=0):
        self.letter = letter
        self.final = final
        self.depth = depth
        self.children = {}
    def add(self, letters):
        node = self
        for index, letter in enumerate(letters):
            if letter not in node.children:
                node.children[letter] = Node(letter, index==len(letters)-1, index+1)
            node = node.children[letter]
    def anagram(self, letters):
        tiles = {}
        for letter in letters:
            tiles[letter] = tiles.get(letter, 0) + 1
        min_length = len(letters)
        return self._anagram(tiles, [], self, min_length)
    def _anagram(self, tiles, path, root, min_length):
        if self.final and self.depth >= MIN_WORD_SIZE:
            word = ''.join(path)
            length = len(word.replace(' ', ''))
            if length >= min_length:
                yield word
            path.append(' ')
            for word in root._anagram(tiles, path, root, min_length):
                yield word
            path.pop()
        for letter, node in self.children.items():
            count = tiles.get(letter, 0)
            if count == 0:
                continue
            tiles[letter] = count - 1
            path.append(letter)
            for word in node._anagram(tiles, path, root, min_length):
                yield word
            path.pop()
            tiles[letter] = count

def load_dictionary(path):
    result = Node()
    for line in open(path, 'r'):
        word = line.strip().lower()
        result.add(word)
    return result

def main(input_word):
    words = load_dictionary('C:\\Users\\72556\\PycharmProjects\\web\\web9\\words.txt')
    input_word = input_word.lower()
    count = 0
    for word in words.anagram(input_word):
        print(word)
        count += 1
    print('%d results.' % count)

input_word = 'превосходство'
main(input_word)