#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import common
from html import Html
from operation_db import OperationDB

operation_db = OperationDB()
home = Html()    

#時間割表を出力
def print_tbody(arg):
    result = ""
    def sch_week(time,arg,result):
        for day in range(0,6):
            a = sch_time(day,time)
            if(a[0]==0):
                result += f'<td>授業あり:{a[0]}人</td>'
            else:
                names = operation_db.get_name(a[1])
                result += f'<td class="ari">授業あり:{a[0]}人<span class="tooltiptext">'
                for name in names:
                    result += f'{name} '
                result += '</span></td>'
        return result

    def sch_time(day,time):
        names = []
        count = 0
        for person in arg:
            if person[1][day][time-1]:
                count += 1
                names.append(person[0])
        return (count, names)
    
    for time in range(1,6):
        result += f'<tr><th scope="row">{time}限目</th>'
        result = sch_week(time,arg, result)
        result += "</tr>"
    print(home.make_tbody(result))


#フォームから値を取得
form = home.get_form(['select','quarter'])
quarter = form['quarter']
if not quarter:
    quarter = common.now_quarter()
select = form['select']
if not select:
    select = home.grade

#htmlを出力設定
home.char_encode()
home.print_header("Home")
home.print_menu()
print(home.form_tag_head(action="./home.py"))
result = home.make_selector("quarter",home.quarters)

#selectに含まれていればチェックボックスに論理属性を追加
for grade in home.grade:
    if grade in select:
        result += home.make_checkbox(grade, True)
    else:
        result += home.make_checkbox(grade)
        
print(result)
print(home.form_tag_tail("選択"))
print(home.make_table_head(caption=f"全体スケジュール {quarter}"))
schedule = operation_db.get_db(quarter, select)
print(home.make_thead(home.week, True))
print_tbody(schedule)
print(home.make_table_tail())
home.print_tail()