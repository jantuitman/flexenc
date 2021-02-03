from abc import ABC, abstractmethod
from .token import Token
 
class AbstractTokenList:
    
    @abstractmethod
    def encode(self, category : str, text : str):
      pass
    
    @abstractmethod
    def getToken(self, category_name : str, token_name :str) -> Token:
      pass

    def encode_stream(self, generator):
      result = []
      for category, text in generator:
        result.extend(self.encode(category, text))  
      return result

class CustomTokenList(AbstractTokenList):
  def __init__(self, token_names : list):
    self.start_token_index = 0
    self.token_count = len(token_names)
    self.token_names = token_names
    self.encoder = lambda category, text, token_list: self.defaultEncode(category, text, token_list)
    super().__init__()

  def encode(self, category : str, text: str):
    return self.encoder(category, text, self)   
  
  def getToken(self, category_name : str, token_name :str) -> Token:
    if token_name in self.token_names:
      index = self.token_names.index(token_name)
      return Token(index + self.start_token_index, token_name, category_name)
    else:
      raise ValueError("Unknown token name")  

  def defaultEncode(self, category, text, token_list):
    if text in self.token_names:
      token = self.getToken(category, text)
      return [ token ]
    else:
      raise ValueError(f"Can't encode: {text}")  



class CategoryTokenList(AbstractTokenList):
  def __init__(self):
    self.start_token_index = 0
    self.token_count = 0
    self.categories = {}
    super().__init__()

  def addCategory(self, category_name :str,token_list : AbstractTokenList):    
    token_list.start_token_index = self.token_count + 1
    self.token_count += token_list.token_count
    self.categories[category_name] = token_list

  def encode(self, category : str, text: str):
    if category in self.categories:
      return self.categories[category].encode(category, text)
    else:
      raise ValueError("Unknown category")     

  def getToken(self, category_name : str, token_name :str) -> Token:
    if category_name in self.categories:
      return self.categories[category_name].getToken(category_name, token_name)
    else:
      raise ValueError("Unknown category")  
