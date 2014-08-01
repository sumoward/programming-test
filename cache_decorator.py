"""
Implement  a  least  recently  used  (LRU)  cache  mechanism
  using  a   decorator  and  demonstrate  it  use
 in  a  small  script.  The  LRU  must  be  able
    to  admit  a  max_size  parameter  that  by  default  has  to  be  100.
    An LRU cache limits its size by flushing the least recently used keys.
"""
from functools import lru_cache
import collections
# implement a lru cache in Python 3 is straight forward use functools


@lru_cache(maxsize=100)
def fib1(n):
    if n < 2:
        return n
    return fib1(n - 1) + fib1(n - 2)
# i have also included my own implementation of a memoization decorator.


def lru(maxsize=100):
    # if there are decorator arguments, the function
    def helper1(passed_function):
        holder1 = {}
        buffer = collections.deque()

        # internal function that we pass the params to
        def caching(param):
            if param not in holder1:
                holder1[param] = passed_function(param)
                buffer.appendleft(param)
                if len(buffer) > maxsize:
                    # find the entry
                    old_key = buffer[maxsize]
                    del holder1[old_key]
                    buffer.pop()
            else:
                buffer.remove(param)
                buffer.appendleft(param)
            return holder1[param]
        return caching
    return helper1


@lru(maxsize=6)
def fib2(n):
    if n < 2:
        return n
    return fib2(n - 1) + fib2(n - 2)

if __name__ == '__main__':
    print(fib1(12))
    print(fib1.cache_info())
    [fib1(n) for n in range(16)]
    print(fib1.cache_info())
    print('*'*60)
    print(fib2(12))
    print('*'*60)
    print(fib2(9))
    print('*'*60)
    print(fib2(10))
#     print ('*'*60)
#     print(fib1(5))
    print('-'*60)
    print(fib2(5))
