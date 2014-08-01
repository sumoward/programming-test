"""
Write  a  function  that  finds  an  integer  in
 a  list  of  unsorted  integers  that   appears  only  once.
  Use  the  following  as  the  list  of  integers:
   [23,  901,  78,   1927,  56,  92,  567,  987,  12,  9,  45,  1936,  76,
     39,  82,  43,  78,  901,  56,  23,  92,   43,
       1927,  39,  9,  45,  567,  987,  12,  76,  82].
"""


def integer_find(number):
    pass
    list_integers = [23,  901,  78,   1927,
                     56,  92,  567,  987,  12,
                     9,  45,  1936,  76,
                     39,  82,  43,
                     78,  901,  56,  23,  92,   43,
                     1927,  39,  9,  45,  567,  987,  12,  76,  82]

    # sort the list
    list_integers.sort()
    # print(list_integers)
    # print(index)
    #print(len(list_integers))
    if number not in list_integers:
        # 2 1 for next in index and 1 for len does not start at 0
        return False
    # only get index if the number is present
    index = list_integers.index(number)
    if len(list_integers) == index + 1:
        return True
        # print(list_integers[number + 1])
    if number == list_integers[index + 1]:
        # print('here')
        return False

    return True


if __name__ == "__main__":
    number = 23
    print(integer_find(number))
    number = 1936
    print(integer_find(number))
    number = 7777
    print(integer_find(number))
