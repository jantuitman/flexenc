from .abstract_token_list import AbstractTokenList;
from .token import Token
from collections import OrderedDict

class CategoryTokenList(AbstractTokenList):
  def __init__(self):
    self.start_token_index = 0
    self.token_count = 1 # token 0 is reserved.
    self.categories = OrderedDict()
    self.insert_whitespace = False
    super().__init__()

  def addCategory(self, category_name :str,token_list : AbstractTokenList):    
    token_list.start_token_index = self.token_count
    self.token_count += token_list.token_count
    self.categories[category_name] = token_list
    token_list.category_name = category_name

  def encode_for_category(self, category : str, text: str):
    if category in self.categories:
      return self.categories[category].encode_for_category(category, text)
    else:
      raise ValueError("Unknown category")     

  def getToken(self, category_name : str, token_name :str) -> Token:
    if category_name in self.categories:
      return self.categories[category_name].getToken(category_name, token_name)
    else:
      raise ValueError("Unknown category")  

  def getTokenById(self, id : int) -> Token:
    for category_name, category in self.categories.items():
      if category.start_token_index <= id and id < category.start_token_index + category.token_count:
        return category.getTokenById(id)
    raise ValueError("token id out of range")    

  # this should return a string which has no whitespace on the left and the right side.
  # but it will add whitespace between tokens if self.insert_whitespace = True
  def decode_tokens(self, tokens : iter) -> str:  
    result = []
    temp_tokens = []
    previous_cat = None
    for token in tokens:
      if token.category != previous_cat:
        if len(temp_tokens) > 0:
          s = self.categories[previous_cat].decode_tokens(temp_tokens)
          temp_tokens  = [];
          result.append(s)
        previous_cat = token.category
        temp_tokens.append(token)
      else:
        temp_tokens.append(token)
    if len(temp_tokens) > 0:
      s = self.categories[previous_cat].decode_tokens(temp_tokens)
      result.append(s)
    sep = " " if self.insert_whitespace else ""  
    return sep.join(result)

