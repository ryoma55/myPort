#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import util
from operation_db import OperationDB
from html import Html

h = Html()
operation_db = OperationDB()

#時間割表を出力
def print_tbody(arg):
    def sch_week(time,arg):
        for day in range(0,6):
            for sch in arg:
                if  sch[time-1]:
                    print("<td class=\"ari\"></td>")
                else:
                    print("<td></td>")
    
    print('<tbody>')
    for time in range(1,6):
        print('<tr><th scope="row">{}限目</th>'.format(time))
        sch_week(time,arg)
        print("</tr>")
    print("</tbody>")

form = h.get_form(['number','quarter','newquarter']+util.period_array())
number = form['number']
quarter = form['quarter']
newquarter = form['newquarter']
newSchedule = {key:form[key] for key in util.period_array()}

if not quarter:
    quarter = util.now_quarter()
user = operation_db.select_user(int(1))
if newSchedule['Mon1'] != None:
    print("OK")
    operation_db.save_sch(number,newquarter,newSchedule)
a,schedule = operation_db.select_sch(int(1),quarter)

#htmlを出力
h.char_encode()
h.print_header("個人スケージュール")
h.print_menu()
print(h.form_tag_head('./schedule.py'))
print(h.make_selector('quarter',h.quarters))
print(h.make_button("number",number,"選択"))
print(h.make_table_head(f"{user[1]}　{quarter}"))
print(h.form_tag_head('./hensyu.py'))
print(h.make_input("hidden","quarter", quarter))
print(h.make_button("number",number,"時間割編集"))
print(h.make_thead(h.week,True))
print_tbody(schedule)
print(h.make_table_tail())
h.print_tail()