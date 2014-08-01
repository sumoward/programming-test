"""
    The  Irish  lottery  draw  takes  place  twice  weekly  on  a  Wednesday
     and  a   Saturday  at  8pm.  Write  a  function  that  calculates
      and  returns  the  next   valid  draw
      date  based  on  the  current  date
      and  time  and  also  on  an   optional  supplied  date.

"""
from datetime import datetime
from datetime import timedelta
from datetime import time

default_day = datetime.today().date()

def lotto_day(chosen_day = default_day):

    print('chosen_day :',chosen_day)
    # print('time :', check_time)
    day_date = datetime.today().date()
    print(day_date)

    if isinstance(chosen_day, str):
        chosen_day = datetime.strptime(chosen_day, '%Y-%m-%d')
        print('chosen_day :',chosen_day)
    day = chosen_day.weekday()
    print('todayday', day)
    #the key is the day, the value is the number of days to next draw 0 = mon, 1 - tues etc
    lotto_day = {0: 2, 1: 1, 2: 0, 3: 2, 4: 1, 5: 0, 6: 3}
    print ('diff', lotto_day[day])

    if lotto_day[day] == 0:
        #if it is a lotto day then check the time
        check_time = datetime.today().time()
        if check_time < time(20, 0, 0):
            next_date = day_date + timedelta(days=lotto_day[day] + 1)
            print('next day', next_date)
    else:
        next_date = day_date + timedelta(days=lotto_day[day])

    print('The next lotto is on the ', next_date)

if __name__ == '__main__':
    #lotto_day()
    lotto_day('2014-07-18')
