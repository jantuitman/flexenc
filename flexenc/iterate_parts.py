import re

class Tokenset:
  def foo(self):
    print("hello")



def iterate_parts(text : str, desicion_table : list):
  """
  :param text: the text to tokenize
  :param desicion_table: table with tuples (category,regex)
	will iterate through text and yield (category,text) pairs 
  """		
  text = re.sub(r'^\s+','', text)
  while text != "":
    matched = False
    for rule in desicion_table:
      label = rule[0]
      match_result = re.match(rule[1], text)
      if match_result:
        matched = True
        yield (label, match_result[1])
        text = text[match_result.end():]
        break
    if not matched:
      yield ("match_error", text)