from abc import ABC, abstractmethod
from .token import Token
 
class AbstractTokenList:
    
  @abstractmethod
  def encode_for_category(self, category : str, text : str):
    pass
  
  @abstractmethod
  def getToken(self, category_name : str, token_name :str) -> Token:
    pass

  @abstractmethod
  def getTokenById(self, id : int) -> Token:
    pass

  def encode(self, generator : iter):
    result = []
    for category, text in generator:
      result.extend(self.encode_for_category(category, text))  
    return result

  @abstractmethod  
  def decode_tokens(self, tokens : iter) -> str:  
    pass        

  def decode(self, data : iter) -> str:
    return self.decode_tokens(map(self.getTokenById, data) )

