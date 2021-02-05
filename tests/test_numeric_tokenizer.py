from flexenc import NumericTokenizer, Token

def test_get_token():
  token_list = NumericTokenizer()
  token = token_list.getToken("category","7")
  assert Token(7,"7","category") == token
  token = token_list.getToken("category","*100")
  assert Token(12,"*100","category") == token

def test_encode():
  token_list = NumericTokenizer()
  token_list.category_name = "numeric"
  tokens = token_list.encode_for_category("numeric","456")  

  assert [
    Token(4,"4","numeric"),
    Token(12,"*100","numeric"), 
    Token(5,"5","numeric"),
    Token(11,"*10","numeric"), 
    Token(6,"6","numeric"),
    Token(10,"*1","numeric") 
  ] == tokens