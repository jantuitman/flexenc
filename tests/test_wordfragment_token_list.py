import pytest
from flexenc import WordFragmentTokenList


def test_train():
  token_list = WordFragmentTokenList("word",500)
  token_list.load_training_words(["is","is","over","in","under","wish","was",
    "bread","beer","butter","meat","fish",
    "giraffe","lion","zebra","horse","cow","sheep",
    "apple","orange","banana","mango","fruit",
    "he","she","it","does","not","was","were","has","is","of","a","an","the","he","she","it"

    ])
  token_list.learn()
  print("\nMy tokens:")
  for word, token in token_list.tokens.items():
    print(token)
