#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import common
from html import Html
from operation_db import OperationDB

hensyu = Html()
operation_db = OperationDB()

#時間割表を出力
def print_tbody(arg):
    #時間割表の行を出力
    def sch_week(time,arg):
        week = ['Mon','Tue','Wen','Thu','Fri','Sat']
        for day in range(0,6):
            if arg[day][time-1]:
                print('<th>')
                print(hensyu.make_radio(week[day]+str(time), 1, "あり", True))
                print(hensyu.make_radio(week[day]+str(time), 0, "なし"))
                print('</th>')
            else:
                print('<th>')
                print(hensyu.make_radio(week[day]+str(time), 1, "あり"))
                print(hensyu.make_radio(week[day]+str(time), 0, "なし", True))
                print('</th>')

    print('<tbody>')
    for time in range(1,6):
        print('<tr><th scope="row">%d限目</th>' % time)
        sch_week(time,arg)
        print("</tr>")
    print("</tbody>")

form = hensyu.get_form(['number','quarter'])
number = form['number']
quarter = form['quarter']
if not quarter:
    quarter = common.now_quarter()
num,schedule = operation_db.select_sch(number,quarter)
print(num,schedule)
    
#htmlを出力
hensyu.char_encode()
hensyu.print_header("時間割編集")
hensyu.print_menu()
print(hensyu.make_table_head(f"時間割編集 {quarter}"))
print(hensyu.make_thead(hensyu.week,True))
print(hensyu.form_tag_head('./hensyu.py'))
print(hensyu.make_selector('quarter',hensyu.quarters))
print(hensyu.make_button("number",number,"選択"))
print("<div>")
print(hensyu.form_tag_head('./schedule.py'))
print_tbody(schedule)
print(hensyu.make_input("hidden","newquarter",quarter))
print(hensyu.make_input("hidden","quarter",quarter))
print(hensyu.make_button("number",num,"時間割登録"))
print(hensyu.form_tag_head('./schedule.py'))
print(hensyu.make_button("number",number,"戻る"))
print("</div>")
print(hensyu.make_table_tail())
hensyu.print_tail()



