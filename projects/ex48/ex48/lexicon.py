# some import stuff mb

direction_list = ['north', 'east', 'south', 'west']
verb_list = ['go', 'stop', 'kill', 'eat']
stop_list = ['the', 'in', 'of', 'from', 'at', 'it']
noun_list = ['door', 'bear', 'princess', 'cabinet']

def scan(input_chain):

# break up the chain of words
  input_words = input_chain.split()
  how_many_words = len(input_words)
# create an empty list of (TYPE, WORD) tuples
  ret = []
# for each word of input check if it is a direction and return the tuple
  for i in range(how_many_words):
# check if it is a number
    try:
      the_number = int(input_words[i])
      ret.append(('number', the_number))
    except ValueError:
# assume it is a word
      temp_type = find_word_type(input_words[i])
      ret.append((temp_type, input_words[i]))
# return the list
  return ret

def find_word_type(word):
  if word in direction_list:
    return 'direction'
  elif word in verb_list:
    return 'verb'
  elif word in stop_list:
    return 'stop'
  elif word in noun_list:
    return 'noun'
  else:
    return 'error'

