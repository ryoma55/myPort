#!/usr/bin/python3
# -*- coding:UTF-8 -*-

from operation_db import OperationDB
from html import Html

ht = Html()
operation_db = OperationDB()

def print_tbody(num,name,grade):
    print("<tbody>")
    for user in range(0,len(num)):
        print(f'''<tr class=\"user\">
        <th>{num[user]}</th>
        <th>{name[user]}</th>
        <th>{grade[user]}</th>
        <th>''')
        print(ht.form_tag_head(action="./schedule.py"))
        print(ht.make_button("number",num[user],"時間割"))
        print('</th><th>')
        print(ht.form_tag_head(action="./user.py"))
        print(ht.make_button("delete",num[user],"削除"))
        print('</th></tr>')
    print("</tbody>")
    
    
form = ht.get_form(['name','grade','delete','namelog'])
if form['name'] and form['grade']:
    #ブラウザ再読み込み対策
    if form['name'] != form['namelog']:
        operation_db.save_user(form['name'],form['grade'])
        
if form['delete']:
    operation_db.delete_user(int(form['delete']))

num,name,grade = operation_db.get_user()

#htmlを出力
ht.char_encode()
ht.print_header("ユーザ一覧")
ht.print_menu()
print(ht.make_table_head("ユーザ一覧"))
print(ht.make_thead(['ID','名前','学年','ユーザー時間割','ユーザー削除']))
print(ht.form_tag_head(action="user.py"))
print(ht.make_input("hidden","namelog", form['name']))
print(ht.make_input("text","name", option ="required"))
print(ht.make_selector("grade",ht.grade))
print(ht.form_tag_tail("登録"))
print_tbody(num,name,grade)
print(ht.make_table_tail())
ht.print_tail()