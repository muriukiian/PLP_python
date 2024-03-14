import json
import difflib

with open('data.json', 'r') as json_file:
  dictionary = json.load(json_file)

def getDefinition(word):
  word_lower = word.lower()
  if word_lower in dictionary:
    return dictionary[word_lower]
  else:
    similar_word = difflib.get_close_matches(word_lower, dictionary.keys(), n =6)
    if similar_word:
      suggestions = similar_word[0]
      return f'Word not found, did you mean {suggestions}'
    else:
      return f'word not found'
    
word = input("Enter word: ")
definition = getDefinition(word)
print(definition)
