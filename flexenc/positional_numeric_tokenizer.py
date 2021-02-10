from .abstract_token_list import AbstractTokenList;
from .token import Token


class PositionalNumericTokenizer(AbstractTokenList):
  def __init__(self):
    self.start_token_index = 0 # will be set by parent
    self.category_name = "" # will be set by parent
    self.token_count = 16
    self.token_names = [
      '0','1','2','3','4','5','6','7','8','9',
      '*1','*10','*100','*1000','*10000','*100000'
    ]
    self.insert_whitespace = False
    super().__init__()

  def encode_for_category(self, category : str, text: str):
    text1 = text[::-1]
    if len(text1) > 5:
      raise ValueError("support up to 5 digits")
    digit_pos = 10  
    result = []
    for digit in text1:
      result.append(self.getTokenById(digit_pos  + self.start_token_index))
      result.append(self.getTokenById(int(digit) + self.start_token_index))
      digit_pos += 1
    # reverse again  
    return result[::-1]  

  
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
    reverse_list = tokens[::-1]
    digit_pos = 10
    success = True
    value = 0
    multiplier = 1
    for index,token in enumerate(reverse_list):
      if index % 2 == 0:
        if token.token_name != self.token_names[digit_pos]:
          success = False
          break
        if index > 0:
          multiplier = multiplier * 10  
        digit_pos += 1
      if index % 2 == 1:
        if len(token.token_name) > 1:
          success = False
          break
        value = value + int(token.token_name) * multiplier  
              
    if success:    
      return str(value)      

    # not successfull: return all token names concatenated
    return "+".join(map(lambda x: x.token_name,tokens))  
