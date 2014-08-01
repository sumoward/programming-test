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


def lru(maxsize=100):
    #holder1 = {}

    # if there are decorator arguments, the function
    # to be decorated Y       it a single argument uou can give to it
    def helper1(passed_function):
        holder1 = {}
        buffer = collections.deque() 
        def caching(param):
            #holder1 = {}
            if param not in holder1:
                holder1[param] = passed_function(param)
                buffer.appendleft(param)
                if len(buffer) > maxsize:
                    #print('in cache')
                     # find the entry
                    old_key = buffer[maxsize]
                    print(old_key)
                    print('ok', old_key,holder1[old_key], len(holder1))
                    del holder1[old_key]
                    buffer.pop()
                    #print(holder1)
            else:
                # what do we do is the key is in our cache
                pass
                buffer.remove(param)
                buffer.appendleft(param)
                #print('in else', param, holder1)
                
                # what do we do if the key is not in our cache
                #del  holder1[param]
                #print('test', ans)
            print(param, holder1)
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
    print ('*'*60)
    print(fib2(12))
    print ('*'*60)
    print(fib2(9))
    print ('*'*60)
    print(fib2(10))
#     print ('*'*60)
#     print(fib1(5))
    print ('-'*60)
    print(fib2(5))
    #print(fib2.cache_info())
    #[fib2(n) for n in range(16)]
    #print(fib2.cache_info())


