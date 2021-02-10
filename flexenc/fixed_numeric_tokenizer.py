from .abstract_token_list import AbstractTokenList;
from .token import Token


class FixedNumericTokenizer(AbstractTokenList):
  def __init__(self,numLength: int):
    self.start_token_index = 0 # will be set by parent
    self.category_name = "" # will be set by parent
    self.token_count = 10
    self.token_names = [
      '0','1','2','3','4','5','6','7','8','9',
    ]
    self.numLength = numLength
    self.insert_whitespace = False
    super().__init__()

  def encode_for_category(self, category : str, text: str):
    result = []
    if len(text) > self.numLength:
      text = text[0:self.numLength]
    if len(text) < self.numLength:
      prefix = "000000000000000000000000000"[0:self.numLength - len(text)]
    else:
      prefix = ""    
    for digit in prefix + text:
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
    begin = False
    result = ""
    for v in strvalues:
      if not begin:
        if v=='0':
          continue
        else:
          begin=True
      result = result + v    
    return result