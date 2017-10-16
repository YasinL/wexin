#!/usr/bin/env python
# -*- conding:utf-8 -*-
__Author__ = "Yasin Li"

import  pymysql

def db_con(inser_sql):
    db = pymysql.connect(host='', port=13307,user="", password="", database = "")
    cursor = db.cursor()
    cursor.execute('INSERT INTO link (link_value) VALUES( %s);', inser_sql)
    print(inser_sql)
    # cursor.execute('INSERT INTO link (link_value) VALUES(12)')
    db.commit()
    db.close()

# db_con(inser_sql='nihao')