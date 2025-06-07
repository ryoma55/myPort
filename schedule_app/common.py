def now_quarter():
    import datetime
    now = datetime.datetime.now()
    if 4 <= now.month and now.month <= 5:
        quarter = 'Q1'
    elif 6 <= now.month and now.month <= 7:
        quarter = 'Q2'
    elif 9 <= now.month and now.month or (now.month == 11 and now.day <= 15):
        quarter = 'Q3'
    else:
        quarter = 'Q4'
    return quarter


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