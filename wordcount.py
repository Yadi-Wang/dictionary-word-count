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

  for word in words:
    word_dict[word] = word_dict.get(word, 0) + 1

# my_dict = {'a': 1, 'b': 2, 'c': 3}

# for key, value in my_dict.items():
#     print("key = {}, value = {}".format(key, value))

  for key, value in word_dict.items():
    print("{} {}".format(key, value))
  
  return word_dict


    
word_count("test.txt")
