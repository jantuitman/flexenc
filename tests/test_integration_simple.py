import pytest
from flexenc import iterate_parts, CustomTokenList, CategoryTokenList,ReduceWhitespaceTokenizer, LetterTokenizer,DropTokenizer,NumericTokenizer



decision_table = [
  ("whitespace"     ,r'^(\s+)' ),
  ("numeric"        ,r'^(\d+)' ),                  
  ("word"           ,r'^([a-zA-Z]+)' ),                  
  ("math"           ,r'^([\+\-\*\/=])' ),                  
  ("ignored"        ,r'^([^a-zA-Z\+\-\*\/= \n\t]+)' )                
]

main = CategoryTokenList()
main.addCategory("whitespace",ReduceWhitespaceTokenizer())
main.addCategory("numeric",NumericTokenizer())
main.addCategory("word",LetterTokenizer())
main.addCategory("math",CustomTokenList(["+","-","*","/","="]))
main.addCategory("ignored",DropTokenizer())

def test_just_letters_and_numbers():
  tokens = main.encode(iterate_parts("The quick brown fox jumps over the lazy cow 21 times",decision_table))
  text = main.decode_tokens(tokens)
  assert "The quick brown fox jumps over the lazy cow 21 times" == text

def test_just_a_sum():
  tokens = main.encode(iterate_parts("10 + 7 = 17",decision_table))
  text = main.decode_tokens(tokens)
  assert "10 + 7 = 17" == text
