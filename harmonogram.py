#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import time

db = 'H.db'
data = time.asctime(time.localtime(time.time()))
id = 0
aktywny = 0

con = sqlite3.connect(db)
print("Polaczono z baza danych:", db)
print()
c = con.cursor()

'''
c.execute("DROP TABLE IF EXISTS zdarzenia;")
c.execute(
    CREATE TABLE zdarzenia (
        id INTEGER PRIMARY KEY,
        data TEXT,
        tresc TEXT,
        aktywny INTEGER ''
    ))'''

while True:

    print("HARMONOGRAM")
    print()
    print("1)dodaj zdarzenie")
    print("2)usuń zdarzenie")
    print("3)wyświetl zdarzenia")
    print("4)wykonaj zdarzenie")
    print("5)zamknij program")
    print()
    W = input("Wybierz opcję: ")
    print()
 
    if int(W) == 1:
        id += 1
        aktywny = 0
        tresc = input("Podaj tresc: ")
        c.execute("INSERT INTO zdarzenia (id, data, tresc, aktywny) VALUES (?, ?, ?, ?)",
                (id, data, tresc, aktywny))
        con.commit()
        print()
        print("Dodano zdarzenie.")
        print()
        print()
        continue
    elif int(W) == 2:
        U = int(input("Podaj numer zdarzenia do usunięcia: "))
        print()
        c.execute("DELETE FROM zdarzenia WHERE id=?", (U,))
        con.commit()        
        print("Usunięto zdarzenie.")
        print()
        print()
        continue
    elif int(W) == 3:
        print("Lista zdarzeń:")
        print()
        for row in c.execute('''SELECT * FROM zdarzenia'''):
            print("ID = ", row[0])
            print("DATA = ", row[1])
            print("TRESC = ", row[2])
            print("AKTYWNY = ", row[3])
            print()
        con.commit()        
        print()
        print()
        continue
    elif int(W) == 4:
        W = int(input("Podaj numer zdarzenia do wykonania: "))
        print()
        aktywny = 1        
        c.execute("UPDATE zdarzenia SET aktywny=? WHERE id=?", (aktywny, W,))		
        con.commit()        
        print("Aktywowano zdarzenie.")
        print()
        print()
        continue
    elif int(W) == 5:
        print("Koniec programu.")
        print()
        print()
        break
    else:
        print("Nie ma takiej opcji.")
        print()
        print()
        continue

input()
