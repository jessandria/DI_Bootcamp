class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        word_list = self.text.split()
        word_count = word_list.count(word)
        if word_count == 0:
            return None
        else:
            return f"The word '{word}' appears {word_count} times in the text."

    def most_common_word(self):
        word_list = self.text.split()
        word_count = {}
        for word in word_list:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        most_common = max(word_count, key=word_count.get)
        return f"The most common word is '{most_common}'."

    def unique_words(self):
        word_list = self.text.split()
        unique_words = set(word_list)
        return list(unique_words)

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            text = file.read()
        return cls(text)


text_obj = Text.from_file('/Users/andriamanankasinajessie/Documents/DI_Bootcamp/week 3/day 5/dailychallenge/the_stranger.txt')

print(text_obj.word_frequency("the"))  
print(text_obj.most_common_word())     
print(len(text_obj.unique_words()))     


