from .custom_token_list import CustomTokenList;
from .token import Token


class LetterTokenizer(CustomTokenList):
  def __init__(self):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    super().__init__(list(map(lambda x:x, letters)))

  def encode_for_category(self, category : str, text: str):
    result = []
    for letter in text:
      result.extend(self.encoder(category, letter, self))
    return result   

    
