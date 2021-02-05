import pytest
from flexenc import iterate_parts, CustomTokenList, CategoryTokenList,ReduceWhitespaceTokenizer, LetterTokenizer,DropTokenizer,NumericTokenizer



decision_table = [
  ("whitespace"     ,r'^(\s+)' ),
  ("numeric"        ,r'^(\d+)' ),                  
  ("word"           ,r'^([a-zA-Z]+)' ),                  
  ("ignored"        ,r'^([^a-zA-Z \n\t]+)' )                
]

main = CategoryTokenList()
main.addCategory("whitespace",ReduceWhitespaceTokenizer())
main.addCategory("numeric",NumericTokenizer())
main.addCategory("word",LetterTokenizer())
main.addCategory("ignored",DropTokenizer())

def test_integration1():
  tokens = main.encode(iterate_parts("The quick brown fox jumps over the lazy cow 21 times",decision_table))
  text = main.decode_tokens(tokens)
  assert "The quick brown fox jumps over the lazy cow 21 times" == text
