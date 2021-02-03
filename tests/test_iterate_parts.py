import pytest
from flexenc import iterate_parts

def test_iterate_parts():
  decision_table = [
    ("whitespace"     ,r'^(\s+)' ),
    ("numeric"        ,r'^(\d+)' ),                  
    ("word"           ,r'^([a-z]+)(?=[^a-zA-Z])' ),                  
    ("start_cap_word" ,r'^([A-Z][a-z]*)' ),                  
    ("mixed_cap_word" ,r'^([a-zA-Z]+)' ),  
    ("punctuation"    ,r'^([,.!?]+)'),
    ("ignored"        ,r'^([^a-zA-Z \n\t]+)' )                
  ]

  result = iterate_parts("text Text 123", decision_table)
  assert next(result) == ("word","text")
  assert next(result) == ("whitespace"," ")
  assert next(result) == ("start_cap_word","Text")
  assert next(result) == ("whitespace"," ")
  assert next(result) == ("numeric","123")
  with pytest.raises(StopIteration):
    next(result)
