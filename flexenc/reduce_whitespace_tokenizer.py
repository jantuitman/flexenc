from .abstract_token_list import AbstractTokenList;
from .token import Token
from collections import OrderedDict

class ReduceWhitespaceTokenizer(AbstractTokenList):
  def __init__(self, keep_newlines : bool = False, keep_spaces : bool = True):
    self.start_token_index = 0
    self.token_count = 2
    self.category_name = ""
    self.keep_newlines = keep_newlines
    self.keep_spaces = keep_spaces
    self.insert_whitespace = False
    super().__init__()

  def encode_for_category(self, category : str, text: str):
    if not self.keep_spaces:
      return []
    if self.keep_newlines and "\n" in text:
      return [ Token(self.start_token_index + 1, "<line/>",category,"\n") ]     
    else:
      return [ Token(self.start_token_index, "<space/>",category," ") ]     
  
  def getToken(self, category_name : str, token_name :str) -> Token:
    if token_name == "<line/>":
      return Token(self.start_token_index + 1, "<line/>",category_name,"") 
    elif token_name == "<space/>":
      return Token(self.start_token_index, "<space/>",category_name,"") 
    else:  
      raise ValueError("Unknown token")  

  def getTokenById(self, id : int) -> Token:
    if id == self.start_token_index:
      return Token(self.start_token_index, "<space/>",self.category_name,"") 
    elif id == self.start_token_index + 1:
      return Token(self.start_token_index + 1, "line/>",category_name,"") 
    else:  
      raise ValueError("Unknown token")  

  # this should return a string which has no whitespace on the left and the right side.
  # but it will add whitespace between tokens if self.insert_whitespace = True
  def decode_tokens(self, tokens : iter) -> str:  
    s = " " if self.insert_whitespace else ""
    if len(tokens) > 0:
      s = " "
    if any(map(lambda token: token.token_name == "<line/>",tokens)):
      s = "\n"
    return s  