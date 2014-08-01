"""
Write  a  function  that  accepts  a  word  (string)  and 
 a  list  of  words  (list  or   tuple  of  strings)  and 
  return  back  a  list  with  the  valid  anagrams  for
  the   word  inside  the  given  words  list.

"""

def anagram(word, word_list):
    if len(word_list) == 0:
        return []
    # print(word_list)
    new_list = []
    word_len = len(word)
# set all words to lower case
    for entry in word_list:
        if len(entry) == word_len:
        # print(entry)
            new_list.append(entry.lower())
    # print(new_list)
    word_list = new_list
# remove any duplicates
    word_list = set(word_list)
# if the word itself is in the list remove it
    if word in word_list:
        word_list.remove(word)
    new_list = []
    #print(word, word_list)
    word = (list(word))
    #print(word)
    word.sort()
    #print(word)
    for entry in word_list:
        entry_list = list(entry)
        entry_list.sort()
        #print(entry_list)
        if word == entry_list:
            #print('here')
            new_list.append(entry)
    #print(new_list)
    #sort the list to make testing easier
    new_list.sort()
    #print(new_list)
    return new_list


if __name__ == "__main__":
    word = 'dog'
    word_list = ['cat', 'dog', 'got', 'sheep', 'GOT', 'cat', 'DOG', 'god']
    print(anagram(word, word_list))
    word_list = ()
    print(anagram(word, word_list))
    word_list = ['cat', 'dog', 'got', 'sheep', 'GOT', 'cat', 'DOG']
    print(anagram(word, word_list))
    word_list = ['god','god','god']
    print(anagram(word, word_list))
    word = 'aeprs'
    #has 12 anagrams
    word_list = ['cat', 'dog', 'got', 'sheep', 'GOT', 'cat', 'DOG', 'god','apers', 'apres', 'asper', 'pares', 'parse', 'pears', 'prase', 'presa', 'rapes', 'reaps', 'spare', 'spear']
    print(anagram(word, word_list))
    print(len(anagram(word, word_list)))


