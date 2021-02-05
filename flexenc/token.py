from dataclasses import dataclass

@dataclass
class Token:
  """ Class representing an encoded token """
  token_index : int
  token_name : str
  category : str  
  string_value : str = ""
  freq : int = 1

  def __repr__(self):
    return f"{self.stringValue()} "
  
  def stringValue(self):
    if self.string_value != "":
      return self.string_value
    else:
      return self.token_name  