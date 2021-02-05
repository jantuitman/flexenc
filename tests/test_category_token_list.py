from flexenc import CategoryTokenList,CustomTokenList, Token


def test_tokencount():
  token_list = CategoryTokenList()
  assert token_list.token_count == 1
  token_list.addCategory("category1", CustomTokenList(["a","b","c","d"]))
  assert token_list.token_count == 5
  token_list.addCategory("category2", CustomTokenList(["e","f","g","h"]))
  assert token_list.token_count == 9


def test_get_token():
  token_list = CategoryTokenList()
  token_list.addCategory("category1", CustomTokenList(["a","b","c","d"]))
  token_list.addCategory("category2", CustomTokenList(["e","f","g","h"]))
  assert Token(3,"c","category1") == token_list.getToken("category1","c")
  assert Token(6,"f","category2") == token_list.getToken("category2","f")

def test_encode():
  def myStream():
    yield ("category1","a")
    yield ("category2","f")

  token_list = CategoryTokenList()
  token_list.addCategory("category1", CustomTokenList(["a","b","c","d"]))
  token_list.addCategory("category2", CustomTokenList(["e","f","g","h"]))

  assert [ Token(1,"a","category1") , 
    Token(6,"f","category2")] == token_list.encode(myStream())

def test_getTokenById():
  token_list = CategoryTokenList()
  token_list.addCategory("category1", CustomTokenList(["a","b","c","d"]))
  token_list.addCategory("category2", CustomTokenList(["e","f","g","h"]))
  assert Token(8,"h", "category2") == token_list.getTokenById(8)
  assert Token(4,"d", "category1") == token_list.getTokenById(4) 

           