from database import pasahitza_gehitu, pasahitza_berreskuratu, pasahitza_ezabatu
from encryption import gakoa_sortu

def menua():
    while True:
        print("\n--- Pasahitz Kudeatzailea ---")
        print("1. Pasahitza gehitu")
        print("2. Pasahitza berreskuratu")
        print("3. Pasahitza ezabatu")
        print("4. Irten")
        aukera = input("Aukeratu ezazu: ")

        if aukera == "1":
            zerbitzua = input("Zerbitzua: ")
            erabiltzailea = input("Erabiltzailea: ")
            pasahitza = input("Pasahitza: ")
            pasahitza_gehitu(zerbitzua, erabiltzailea, pasahitza)
            print("Pasahitza ondo gorde da.")
        elif aukera == "2":
            zerbitzua = input("Zerbitzua: ")
            erabiltzailea, pasahitza = pasahitza_berreskuratu(zerbitzua)
            if erabiltzailea:
                print(f"Erabiltzailea: {erabiltzailea}")
                print(f"Pasahitza: {pasahitza}")
            else:
                print("Ez da zerbitzua aurkitu.")
        elif aukera == "3":
            zerbitzua = input("Zerbitzua: ")
            pasahitza_ezabatu(zerbitzua)
            print("Pasahitza ondo ezabatu da.")
        elif aukera == "4":
            break
        else:
            print("Aukera okerra.")

if __name__ == "__main__":
    gakoa_sortu()  # Enkriptazio gakoa sortu ez badago
    menua()