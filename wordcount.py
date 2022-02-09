"""Count words in file."""

# open text file
# iterate through each word
# count each word
# create a dictionary

def word_count(text_file):
  
  file = open(text_file)

  words = []
  word_dict = {}

  for line in file:
    line = line.rstrip()
    words.extend(line.split(" "))

  # punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  # for word in words:
  #   for char in word:
  #     if char in punc:
  #       word = word.replace(char, "")
  for word in words:
    word_dict[word] = word_dict.get(word, 0) + 1

  for key, value in word_dict.items():
    print("{} {}".format(key, value))



    
word_count("test.txt")
