import sqlite3
import os

def konexioa_sortu():
    # Datuak basea 'data' karpetan gordetzen da
    if not os.path.exists('data'):
        os.makedirs('data')
    return sqlite3.connect('data/pasahitzak.db')

# Datuak gordetzeko taulak
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


# Pasahitza gorde
def pasahitza_gehitu(zerbitzua, erabiltzailea, pasahitza):
    konexioa = konexioa_sortu()
    kurtsorea = konexioa.cursor()
    kurtsorea.execute('''
        INSERT INTO pasahitzak (zerbitzua, erabiltzailea, pasahitza)
        VALUES (?, ?, ?)
    ''', (zerbitzua, erabiltzailea, pasahitza))
    konexioa.commit()
    konexioa.close()

# Pasahitza erakutsi
def pasahitza_berreskuratu(zerbitzua):
    konexioa = konexioa_sortu()
    kurtsorea = konexioa.cursor()
    kurtsorea.execute('SELECT erabiltzailea, pasahitza FROM pasahitzak WHERE zerbitzua = ?', (zerbitzua,))
    emaitza = kurtsorea.fetchone()
    konexioa.close()
    return emaitza

# Pasahitza ezabatu
def pasahitza_ezabatu(zerbitzua):
    konexioa = konexioa_sortu()
    kurtsorea = konexioa.cursor()
    kurtsorea.execute('DELETE FROM pasahitzak WHERE zerbitzua = ?', (zerbitzua,))
    konexioa.commit()
    konexioa.close()

taula_sortu()