from .abstract_token_list import AbstractTokenList;
from .token import Token


class CustomTokenList(AbstractTokenList):
  def __init__(self, token_names : list):
    self.start_token_index = 0 # will be set by parent
    self.category_name = "" # will be set by parent
    self.token_count = len(token_names)
    self.token_names = token_names
    self.insert_whitespace = False
    self.encoder = lambda category, text, token_list: self.defaultEncode(category, text, token_list)
    super().__init__()

  def encode_for_category(self, category : str, text: str):
    return self.encoder(category, text, self)   
  
  def getToken(self, category_name : str, token_name :str) -> Token:
    if token_name in self.token_names:
      index = self.token_names.index(token_name)
      return Token(index + self.start_token_index, token_name, category_name)
    else:
      raise ValueError("Unknown token name")  


  def getTokenById(self, id : int) -> Token:
    return Token(id, self.token_names[id - self.start_token_index], self.category_name)

  # this should return a string which has no whitespace on the left and the right side.
  # but it will add whitespace between tokens if self.insert_whitespace = True
  def decode_tokens(self, tokens : iter) -> str:  
    sep = " " if self.insert_whitespace else ""  
    return sep.join(map(lambda x: x.stringValue(), tokens))




  def defaultEncode(self, category, text, token_list):
    if text in self.token_names:
      token = self.getToken(category, text)
      return [ token ]
    else:
      raise ValueError(f"Can't encode: {text}")  