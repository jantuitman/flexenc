from .abstract_token_list import AbstractTokenList;
from .token import Token
from collections import Counter, defaultdict
import re

class WordFragmentTokenList(AbstractTokenList):
  def __init__(self, category : str,max_token_count : int, required_vocabulary : list = None):
    self.start_token_index = 0
    self.category = category
    self.token_count = max_token_count
    self.train_words = []
    self.encoder = lambda category, text, token_list: self.defaultEncode(category, text, token_list)
    if required_vocabulary is None:
      required_vocabulary = []
      for s in "abcdefghijklmnopqrstuvwxyzABCDEFFGHIJKLMNOPQRSTUVWXYZ":
        required_vocabulary.append(s)
      required_vocabulary.append("</w>")  
    self.required_vocabulary = required_vocabulary
    self.tokens = {}
    super().__init__()

  def load_training_words(self, words : iter):
    for word in words:
      self.train_words.append(word)

  

  def learn(self, iterations : int = 50):    
    vocabulary = self.learn_vocabulary(self.build_vocabulary(self.train_words), iterations)
    delete_frequency = 0
    ntokens_to_delete = 0
    while len(vocabulary.keys()) - ntokens_to_delete > self.token_count - len(self.required_vocabulary):
      delete_frequency += 1
      ntokens_to_delete = sum(value <= delete_frequency for value in vocabulary.values())
      # TODO IN THE FUTURE, if we delete every token with a
      # frequency <= delete_frequency, we will have enough
      # room in our vocabulary.
      # but, we might delete a little bit too much.
      # for now we just delete but in the future we might add some logic to preserve part of
      # the highest frequency tokens in the group we delete.
    remove_keys = [token for token, value in vocabulary.items() if value <= delete_frequency]       
    for key in remove_keys:
          del vocabulary[key]
    self.build_tokens(vocabulary)      
  
  def encode(self, category : str, word : str):
    #TODO copy this from the colab document
    pass
  
  def getToken(self, category_name : str, token_name :str) -> Token:
    if token_name in self.tokens:
      t = self.tokens[token_name]
      return Token(t.index + self.start_token_index, t.token_name, category_name, t.string_value, t.freq)
    else:
      raise ValueError("token not found: "+ token_name)

  #------------------------------ helpers -------------------------
  def build_tokens(self, vocabulary):
    count = 0
    for word,freq in vocabulary.items():
      text = word.replace(" ","").replace("</w>"," ")
      self.tokens[word] = Token(count, word, self.category,string_value = text,freq = freq)
      count += 1
    for word in self.required_vocabulary:
      if not word in self.tokens:
        text = word.replace(" ","").replace("</w>"," ")
        self.tokens[word] = Token(count, word, self.category,string_value = text,freq = 1)
        count += 1


  def build_vocabulary(self, words :list) -> dict:
    #split 
    subtokens = [
       " ".join(word) + " </w>"
       for word in words
    ]
    return Counter(subtokens)
  
  def count_pair_frequency(self, vocab : dict) -> dict:
    pairs = defaultdict(int)
    for word, frequency in vocab.items():
      symbols = word.split()
      for i in range(len(symbols) - 1):
        pairs[symbols[i],symbols[i+1]] += frequency
    return pairs


  def merge_vocabulary(self, pair: tuple, pair_freq: int, vocabulary : dict) -> dict:
    result_vocabulary = {}
    bigram = re.escape(' '.join(pair))
    # search for (not preceded with non whitespace) the bigram (not followed by any non whitespace)
    replacer = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in vocabulary:
      merged_word = replacer.sub(''.join(pair), word)
      result_vocabulary[merged_word] = vocabulary[word]

    result_vocabulary["".join(pair)] = pair_freq
    return result_vocabulary 

  def learn_vocabulary(self, vocabulary : dict, num_merges: int) -> dict:
    for i in range(num_merges):
      pairs = self.count_pair_frequency(vocabulary)
      if not pairs:
        return vocabulary
      best = max(pairs, key=pairs.get)
      print("best", pairs[best])
      vocabulary = self.merge_vocabulary(best, pairs[best], vocabulary)
    return vocabulary