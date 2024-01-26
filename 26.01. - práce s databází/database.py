"""
    Práce s databází v mysql
    
    1) stáhněte si do svého PC xampp z verejne_vsichni
    2) extrahujte, spusťte setup_xampp.bat, poté spusťte xampp-control.exe
    3) zapněte Apache a MySQL server
    
    Práce v Pythonu
    
    1) importujeme mysql.connector na první řádek
    2) nainstalujeme connector pomocí pip. Příkaz do terminálu: py -m pip install mysql-connector-python
    3) vytvoříme připojení do databáze s potřebnými údaji (MySQL server v xamppu má vždy jméno root a heslo prázdné)
    4) vytvoříme cursor pro vykonání příkazu
    5) pomocí dané konkrétní funkce vykonáme příkaz (execute, fetchall)    
    
"""

import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library"
)

mycursor = mydatabase.cursor()
mycursor.execute("SELECT * FROM books")

results = mycursor.fetchall()

for x in results:
    print(x)
    

insertCursor = mydatabase.cursor()
sql = "INSERT INTO books (name, pages, author, release_date, genre, language) VALUES (%s, %s, %s, %s, %s, %s)"
val = ("Minecraft", 9, "Vojta Věchetů", "2023-05-08", "sci-fi", "cesky")
insertCursor.execute(sql, val)

mydatabase.commit()