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


def lotto_day(chosen_day=datetime.today().date()):

    if isinstance(chosen_day, str):
        chosen_day = datetime.strptime(chosen_day, '%Y-%m-%d').date()
    day = chosen_day.weekday()
    # the key is the day, the value is the number of days
    # to next draw 0 = mon, 1 - tues etc
    lotto_day = {0: 2, 1: 1, 2: 0, 3: 2, 4: 1, 5: 0, 6: 3}

    if lotto_day[day] == 0:
        #  it is a lotto day then check the time
        check_time = datetime.today().time()
        if check_time < time(20, 0, 0):
            next_date = chosen_day + timedelta(days=lotto_day[day] + 1)
    else:
        next_date = chosen_day + timedelta(days=lotto_day[day])

    return next_date

if __name__ == '__main__':
    lotto_day()
    lotto_day('2014-07-18')
