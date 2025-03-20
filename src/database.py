import sqlite3

def konexioa_sortu():
    return sqlite3.connect('data/pasahitzak.db')

def taula_sortu():
    konexioa = konexioa_sortu()
    kurtsorea = konexioa.cursor()
    kurtsorea.execute('''
        CREATE TABLE IF NOT EXISTS pasahitzak (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            zerbitzua TEXT NOT NULL,
            erabiltzailea TEXT NOT NULL,
            pasahitza TEXT NOT NULL
        )
    ''')
    konexioa.commit()
    konexioa.close()

def pasahitza_gehitu(zerbitzua, erabiltzailea, pasahitza):
    konexioa = konexioa_sortu()
    kurtsorea = konexioa.cursor()
    kurtsorea.execute('''
        INSERT INTO pasahitzak (zerbitzua, erabiltzailea, pasahitza)
        VALUES (?, ?, ?)
    ''', (zerbitzua, erabiltzailea, pasahitza))
    konexioa.commit()
    konexioa.close()

def pasahitza_berreskuratu(zerbitzua):
    konexioa = konexioa_sortu()
    kurtsorea = konexioa.cursor()
    kurtsorea.execute('SELECT erabiltzailea, pasahitza FROM pasahitzak WHERE zerbitzua = ?', (zerbitzua,))
    emaitza = kurtsorea.fetchone()
    konexioa.close()
    return emaitza

def pasahitza_ezabatu(zerbitzua):
    konexioa = konexioa_sortu()
    kurtsorea = konexioa.cursor()
    kurtsorea.execute('DELETE FROM pasahitzak WHERE zerbitzua = ?', (zerbitzua,))
    konexioa.commit()
    konexioa.close()

# Taula sortu programa abiaraztean
taula_sortu()