from flexenc import FixedNumericTokenizer, Token

def test_get_token():
  token_list = FixedNumericTokenizer(numLength=4)
  token = token_list.getToken("category","7")
  assert Token(7,"7","category") == token

def test_encode():
  token_list = FixedNumericTokenizer(numLength=4)
  token_list.category_name = "numeric"
  tokens = token_list.encode_for_category("numeric","21")  

  assert [
    Token(0,"0","numeric"),
    Token(0,"0","numeric"), 
    Token(2,"2","numeric"), 
    Token(1,"1","numeric") 
  ] == tokens

def test_decode_tokens():
  tokens = [
    Token(0,"0","numeric"),
    Token(0,"0","numeric"), 
    Token(2,"2","numeric"), 
    Token(1,"1","numeric") 
  ]
  token_list = FixedNumericTokenizer(numLength=4)
  assert "21" == token_list.decode_tokens(tokens) 