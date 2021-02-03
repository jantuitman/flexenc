from dataclasses import dataclass

@dataclass
class Token:
  """ Class representing an encoded token """
  token_index : int
  token_name : str
  category : str  
