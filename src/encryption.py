from cryptography.fernet import Fernet

def gakoa_sortu():
    gakoa = Fernet.generate_key()
    with open("data/gakoa.key", "wb") as gako_fitxategia:
        gako_fitxategia.write(gakoa)

def gakoa_kargatu():
    return open("data/gakoa.key", "rb").read()

def enkriptatu(pasahitza):
    gakoa = gakoa_kargatu()
    f = Fernet(gakoa)
    return f.encrypt(pasahitza.encode())

def desenkriptatu(pasahitz_enkriptatua):
    gakoa = gakoa_kargatu()
    f = Fernet(gakoa)
    return f.decrypt(pasahitz_enkriptatua).decode()