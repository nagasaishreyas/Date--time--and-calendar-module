def match_words(words):
    ctr = 0
    lst = []
    for word in words:
      if len(word) > 1 and word[0] == word[-1]:
        ctr  += 1
        lst.append(word)
 
    print("list of words with first and last characters same \n", lst )
    return ctr

count = match_words(['shreyas', 'abcda', 'adhsqwedgywfed', 'cghdfcjctyqfcyic', 'dvwevftwetyrf6td'])
print("number of words with first and last characters same", count)