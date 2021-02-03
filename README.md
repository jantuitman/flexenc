#USAGE

Here is how you use this library:


## Iterate parts

this function lets you pretokenize texts using a decision table. The idea here is to divide text into somewhat broad categories and then process the text fragments of 1 category into tokens. This because we want to treat numbers, whitespace, words, in entirely different ways.  

The decision table is a structure that associates a category with a regex. We use a capture group, so there must be a pair of brackets in the regex. This could be used to drop some unwanted separators between the tokens, or to capture (with a lookahead expression) what we expect to come right after the category.

In the example below we use this feature to make sure we can match "word" (a lowercase word) and also "mixed_cap_word" (a word that might have capitals in the middle). To make sure a mixed_cap_word  isn't split up in a lowercase word and another word we end the regex of word with a lookahead expression that sais a non-letter should follow. This means "word" will match only words that exist entirely of lowercase letters.

```
decision_table = [
  ("whitespace"     ,r'^(\s+)' ),
  ("numeric"        ,r'^(\d+)' ),                  
  ("word"           ,r'^([a-z]+)(?=[^a-zA-Z])' ),                  
  ("start_cap_word" ,r'^([A-Z][a-z]*)' ),                  
  ("mixed_cap_word" ,r'^([a-zA-Z]+)' ),  
  ("punctuation"    ,r'^([,.!?]+)'),
  ("ignored"        ,r'^([^a-zA-Z \n\t]+)' )                
]

for v in iterate_parts("Hello this is a test. We have 33 trees in our garden, as you know.", decision_table):
  print(v)                
```

## CategoryTokenList

This class represents a list of tokens. It can be composed of multiple other tokenlists. for example you might want to have a separate tokenlist for numbers and for words.

```
list = CategoryTokenList()
list.addCategory("word", TokenList.wordPieces(10000))
list.addCategory("numeric", TokenList.custom(["#0","#1","#2","#3","#4","#5","#6","#6","#7,"#8","#9"]))

list.getTokens("numeric","#1") #will return a list containing 1 named token #1
list.getTokens("word","schoolwork") # will return a list of all the wordpieces



# Training of WordPieces
wordPieces = TokenList.wordPieces(10000)
wordPieces.train(["I","can","have","a","lot","of","different","words","and","subwords"])
# this will add the alphabet to the tokenlist, so that every word becomes parseable.
wordPieces.completeWithAlphabet()

# assigning an encoder to the custom tokenlist.
def encode(category,text, tokenlist):
  if text == "1": return [ tokenlist.getToken("#1") ]
  ...

customList = TokenList.custom(["#0","#1","#2","#3","#4","#5","#6","#6","#7,"#8","#9"])
customList.encoder = encode 

# set up encoders for categories that dont have their own token lists.
list.categoryEncoder("start_cap_word", lambda category, text: return [ StartCapToken ] + wordPieces.encode(text))
list.categoryEncoder("any_cap_word", lambda category, text: wordPieces.encode(text))

# using encode and decode:

tokens = list.encode(iterate_parts(text, desicion_table))

str = list.decode(tokens)

