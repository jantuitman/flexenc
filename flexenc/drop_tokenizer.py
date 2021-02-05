from .abstract_token_list import AbstractTokenList;
from .token import Token
from collections import OrderedDict

class DropTokenizer(AbstractTokenList):
  def __init__(self, insert_whitespace : bool = True):
    self.start_token_index = 0
    self.token_count = 1
    self.category_name = ""
    self.insert_whitespace = insert_whitespace
    super().__init__()

  def encode_for_category(self, category : str, text: str):
    return [ Token(self.start_token_index, "<drop/>",category,"") ]     

  def getToken(self, category_name : str, token_name :str) -> Token:
    if token_name == "<drop/>":
      return Token(self.start_token_index, "<drop/>",category_name,"") 
    else:  
      raise ValueError("Unknown token")  

  def getTokenById(self, id : int) -> Token:
    return Token(self.start_token_index, "<drop/>",self.category_name,"") 

  # this should return a string which has no whitespace on the left and the right side.
  # but it will add whitespace between tokens if self.insert_whitespace = True
  def decode_tokens(self, tokens : iter) -> str:  
    return "" if not self.insert_whitespace else " "  
