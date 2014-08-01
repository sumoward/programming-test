"""
Write  a  program  that  prints  the  numbers  from  1  to  100.  But  for  multiples   of  thee  print 
fizz instead  of  the  number  and  for  multiples  of  five  print
   buzz.  For  numbers  that  are  multiples  of  both  three  and  five  print   FizzBuzz. 
"""


def fizzbuzz(number):
    if number%3 ==0 and number %5 ==0:
        return 'Fizz Buzz'
    elif number%3 ==0:
        return 'Fizz'
    elif number%5 ==0:
        return 'Buzz'
    return str(number)


def loop():
    # add time measure and compare lambda and
    for number in range(1,101):
        #('no: ',number)
        print(fizzbuzz(number))
        #print(fizzbuzz(number))

# checkio=lambda n:("Fizz "(1-n%3)+"Buzz "(1-n%5))[:-1]or str(n)


if __name__ == "__main__":
    loop()
    #print(fizzbuzz(21))
    #print(fizzbuzz(14))
    #print(fizzbuzz(10))
   # print(fizzbuzz(15))