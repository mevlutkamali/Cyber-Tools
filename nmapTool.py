import os

def nmap_tool():
    while True:
        print('''
        --------------------------------------------
                        NMAP TOOL
        --------------------------------------------
            0 - Sade nmap taraması
            1 - Servis ve script taraması (-sC -sV)
            2 - Tüm portları tara (-p-)
            3 - İşletim sistemi tespiti (-O)
            4 - Çıkış
        --------------------------------------------
        ''')

        ip = input("IP adresini giriniz: ")
        choice = input("İşlem numarasını seçiniz: ")

        if choice == "0":
            os.system(f"nmap {ip}")
        elif choice == "1":
            os.system(f"nmap -sC -sV {ip}")
        elif choice == "2":
            os.system(f"nmap -p- {ip}")
        elif choice == "3":
            os.system(f"nmap -O {ip}")
        elif choice == "4":
            print("Çıkış yapılıyor... 👋")
            break
        else:
            print("❌ Geçersiz seçim yaptınız!")

if __name__ == "__main__":
    nmap_tool()
