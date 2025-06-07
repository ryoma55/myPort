#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import sqlite3
from contextlib import closing
from common import array_make


class OperationDB:
    def __init__(self,dbname = '/var/www/db/schedule.db'):
        self.dbname = dbname
        self.create_user()
        self.create_quarter()

    
    #データベース操作
    def excute_sql(self, sql, returns = False, args = False):
        with closing(sqlite3.connect(self.dbname)) as conn:
            result = None
            c = conn.cursor()
            #c.execute('PRAGMA foreign_keys = ON')
            if returns:
                    c.execute(sql)
                    result = c.fetchall()
                    conn.commit()
                    return result   
            else:
                if isinstance(sql, list):
                    for s in sql:

                        if args:
                            c.execute(s[0], s[1])
                        else:
                            c.execute(s)
                else:
                    if args:
                        c.execute(sql[0], sql[1])
                    else:
                        c.execute(sql)
            conn.commit()
                    
        
    #データベースの作成
    def create_db(self):
        create_table = '''create table if not exists user(id integer primary key, name varchar(8), grade varchar(3))\
            Mon1 integer default 0,
            Mon2 integer default 0,
            Mon3 integer default 0,
            Mon4 integer default 0,
            Mon5 integer default 0,
            Tue1 integer default 0,
            Tue2 integer default 0,
            Tue3 integer default 0,
            Tue4 integer default 0,
            Tue5 integer default 0,
            Wen1 integer default 0,
            Wen2 integer default 0,
            Wen3 integer default 0,
            Wen4 integer default 0,
            Wen5 integer default 0,
            Thu1 integer default 0,
            Thu2 integer default 0,
            Thu3 integer default 0,
            Thu4 integer default 0,
            Thu5 integer default 0,
            Fri1 integer default 0,
            Fri2 integer default 0,
            Fri3 integer default 0,
            Fri4 integer default 0,
            Fri5 integer default 0,
            Sat1 integer default 0,
            Sat2 integer default 0,
            Sat3 integer default 0,
            Sat4 integer default 0,
            Sat5 integer default 0)'''
        self.excute_sql(create_table)


    #ユーザデータベース作成 home.py
    def create_user(self):
            create_table = '''create table if not exists user(id integer primary key, name varchar(8), grade varchar(3))\
                '''
            self.excute_sql(create_table)
    

    #各クォータのデータベース作成 homo.py
    def create_quarter(self):
        sql_list = []
        for q in range(1,5):
            sql = '''create table if not exists Q{} 
            (id integer primary key references user(id), 
            Mon1 integer default 0,
            Mon2 integer default 0,
            Mon3 integer default 0,
            Mon4 integer default 0,
            Mon5 integer default 0,
            Tue1 integer default 0, 
            Tue2 integer default 0,
            Tue3 integer default 0, 
            Tue4 integer default 0,
            Tue5 integer default 0,
            Wen1 integer default 0, 
            Wen2 integer default 0, 
            Wen3 integer default 0,
            Wen4 integer default 0, 
            Wen5 integer default 0,
            Thu1 integer default 0,
            Thu2 integer default 0,
            Thu3 integer default 0,
            Thu4 integer default 0,
            Thu5 integer default 0,
            Fri1 integer default 0,
            Fri2 integer default 0,
            Fri3 integer default 0,
            Fri4 integer default 0,
            Fri5 integer default 0,
            Sat1 integer default 0,
            Sat2 integer default 0,
            Sat3 integer default 0,
            Sat4 integer default 0,
            Sat5 integer default 0)'''.format(q)
            sql_list.append(sql)
        self.excute_sql(sql_list)
        

    #ユーザ登録 user.py
    def save_user(self,name,grade): 
        sql_list = []
        init = (0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0)
        sql = f'INSERT INTO user (name, grade) VALUES(?,?)'
        sql_list.append((sql, (name, grade)))
        for i in range(1,5):
            sql = f'INSERT INTO Q{i} (Mon1, Mon2, Mon3, Mon4, Mon5, Tue1, Tue2, Tue3, Tue4, Tue5, Wen1, Wen2, Wen3, Wen4,\
Wen5, Thu1, Thu2, Thu3, Thu4, Thu5, Fri1, Fri2, Fri3, Fri4, Fri5, Sat1, Sat2, Sat3, Sat4, Sat5) \
    VALUES(?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,? ,?,?,?,?,? ,?,?,?,?,?, ?,?,?,?,?)'
            sql_list.append((sql, init))
        try:  
            self.excute_sql(sql_list, args=True) 
        except Exception as e:
            print(e)
                        

    #ユーザ削除 user.py
    def delete_user(self, number): 
        sql = 'DELETE FROM user WHERE id = {}'.format(number)
        sql2 = 'DELETE FROM Q1 WHERE id = {}'.format(number)
        sql3 = 'DELETE FROM Q2 WHERE id = {}'.format(number)
        sql4 = 'DELETE FROM Q3 WHERE id = {}'.format(number)
        sql5 = 'DELETE FROM Q4 WHERE id = {}'.format(number)
        self.excute_sql([sql,sql2,sql3,sql4,sql5])


    # ユーザ一覧を取得 usr.py
    def get_user(self):
        row2 = []
        num = []
        name = []
        grade = []

        select_sql = 'SELECT * FROM user'
        for row in self.excute_sql(select_sql, True):
            row2.append(row)
        for user in row2:
            num.append(user[0])
            name.append(user[1])
            grade.append(user[2])
        return num,name,grade


    #データベースから指定された学年の時間割を取得
    def get_db(self, quarter, select = None):
        if select == None:
            select = ['3','4','M1','M2','その他']
        row2=[]
        select_sql = 'SELECT * FROM {}'.format(quarter)
        #引数selectがリストであるかどうか
        if not isinstance(select, list):
            select_sql += " WHERE id IN (SELECT id FROM user WHERE grade = \"{}\")".format(select)
        else:    
            select_sql += " WHERE id IN (SELECT id FROM user WHERE grade = \"{}\")".format(select[0])
            for i in range(1,len(select)):
                select_sql += " OR id IN (SELECT id FROM user WHERE grade = \"{}\")".format(select[i]) 
        for row in self.excute_sql(select_sql, True):
            row2.append((row[0], array_make(row[1:])))
        return row2


    #時間割を保存
    def save_sch(self,num,quarter,schedule):

        week = ['Mon','Tue','Wen','Thu','Fri','Sat']
        sql_list = []
        for key in schedule:
                sql = f'UPDATE {quarter} SET {key}={schedule[key]} WHERE id = {num}'
                sql_list.append(sql)
        self.excute_sql(sql_list)


    #編集しているユーザの時間割情報を取得
    def select_sch(self, num,quarter):

        select_sql = 'SELECT * FROM {} WHERE id = {}'.format(quarter, num)

        for row in self.excute_sql(select_sql, True):
            pass
        row2 = array_make(row[1:])
        return row[0],row2


    #選択されたユーザの情報を取得
    def select_user(self, user_id):
        select_sql = 'SELECT * FROM user WHERE id = {}'.format(user_id)
        for row in self.excute_sql(select_sql, True):
            pass
        user = row
        return user


    def get_name(self,user_id):
        select_sql = 'SELECT name FROM user WHERE id = {}'.format(user_id[0])
        for i in range(1,len(user_id)):
            select_sql += " OR id = {}".format(user_id[i])
        name = []
        for row in self.excute_sql(select_sql, True):
            name.append(row[0])
        return name


