from cryptography.fernet import Fernet
import os

def gakoa_sortu():
    # data direktorioa ez da existitzen
    if not os.path.exists('data'):
        os.makedirs('data')

    # gakoa.key fitxategia ez da existitzen
    if not os.path.exists('data/gakoa.key'):
        gakoa = Fernet.generate_key()
        with open("data/gakoa.key", "wb") as gako_fitxategia:
            gako_fitxategia.write(gakoa)

# gakoa.key fitxategia irakujrri
def gakoa_kargatu():
    return open("data/gakoa.key", "rb").read()

# Pasahitza enkriptatu
def enkriptatu(pasahitza):
    gakoa = gakoa_kargatu()
    f = Fernet(gakoa)
    return f.encrypt(pasahitza.encode())

# Pasahitza hasierara bueltatu
def desenkriptatu(pasahitz_enkriptatua):
    gakoa = gakoa_kargatu()
    f = Fernet(gakoa)
    return f.decrypt(pasahitz_enkriptatua).decode()