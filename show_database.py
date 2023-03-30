#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('H.db')

c = conn.cursor()

#c.execute('''CREATE TABLE Zdarzenia(AId integer primary key autoincrement,'data','text','aktywny')''')

#c.execute('''INSERT INTO Zdarzenia VALUES(1, '29.05.2019 12:10', 'task1', 'nie')''')
#c.execute('''INSERT INTO Zdarzenia VALUES(2, '15.03.2023 16:55', 'task2', 'tak')''')

for row in c.execute('''SELECT * FROM Zdarzenia'''):
    print(row)

conn.commit()

input()
