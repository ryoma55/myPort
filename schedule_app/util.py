def now_quarter():
    import datetime
    now = datetime.datetime.now()
    quarter ={
    "Q1":({"month":4,"day":1}, {"month":5, "day":31}),
    "Q2":({"month":6,"day":1}, {"month":7, "day":31}),
    "Q3":({"month":9,"day":1}, {"month":11, "day":15}),
    "Q4":({"month":11,"day":16}, {"month":3, "day":31})
    }
    for key, value in quarter.items():    
        start, end = value
        if (start['month'] == now.month and start['day'] <= now.day) or \
           (end['month'] == now.month and now.day <= end['day']) or \
           (start['month'] < now.month < end['month']):
            return key
    return "Q1"  # Default to Q4 if no match found

def period_array():
    week = ['Mon','Tue','Wen','Thu','Fri','Sat']
    schedule = []
    for day in week:
        for date in range(1,6):
            schedule.append('{}{}'.format(day,date))
    return schedule


#時間割を格納する配列の作成
def array_make(array):
    day = []
    week = []

    for time in array:
        day.append(time)
        if len(day)%5 == 0:
            week.append(day)
            day = []
    return week

if __name__ == "__main__":
    print(now_quarter())