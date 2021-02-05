from flexenc import CustomTokenList, Token

def test_get_token():
  token_list = CustomTokenList(["a","b","c","d"])
  token = token_list.getToken("category","c")
  assert Token(2,"c","category") == token

def test_default_encode_behaviour():
  token_list = CustomTokenList(["a","b","c","d"])
  assert [ Token(3,"d","category") ] == token_list.encode_for_category("category","d")  

def test_custom_encode():
  def my_encode(category, text, token_list):
    return [ token_list.getToken(category,"a"), token_list.getToken(category,"b") ]
  
  token_list = CustomTokenList(["a","b","c","d"])
  token_list.encoder = my_encode
  assert [
    Token(0,"a","category"), 
    Token(1,"b","category") ] == token_list.encode_for_category("category", "the text")

 
def test_getTokenById():
  token_list = CustomTokenList(["a","b","c","d"])
  token_list.start_token_index = 4
  token_list.category_name = "foo"
  assert Token(5,"b","foo") == token_list.getTokenById(5)

