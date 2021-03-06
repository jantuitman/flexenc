from .abstract_token_list import AbstractTokenList;
from .token import Token


class NumericTokenizer(AbstractTokenList):
  def __init__(self):
    self.start_token_index = 0 # will be set by parent
    self.category_name = "" # will be set by parent
    self.token_count = 16
    self.token_names = [
      '0','1','2','3','4','5','6','7','8','9',
    ]
    self.insert_whitespace = False
    super().__init__()

  def encode_for_category(self, category : str, text: str):
    result = []
    for digit in text:
      result.append(self.getTokenById(int(digit) + self.start_token_index))
    return result
  
  def getToken(self, category_name : str, token_name :str) -> Token:
    if token_name in self.token_names:
      index = self.token_names.index(token_name)
      return Token(index + self.start_token_index, token_name, category_name)
    else:
      raise ValueError("Unknown token name")  


  def getTokenById(self, id : int) -> Token:
    return Token(id, self.token_names[id - self.start_token_index], self.category_name)

  def decode_tokens(self, tokens : iter) -> str:
    strvalues = map(lambda x: x.token_name, tokens)
    return "".join(strvalues)