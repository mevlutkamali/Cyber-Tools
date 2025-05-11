import os

def figlet():
    # Gereken araçları yükle
    os.system("sudo apt-get install figlet lolcat -y")
    os.system("clear")

    # Figlet + lolcat (renkli başlık)
    os.system("figlet mr.Dark | lolcat")

    # Kuru kafa ASCII sanatını renkli yazdırmak
    skull = r'''
     ______
  .-'      `-.
 /            \
|              |
|,  .-.  .-.  ,|
| )(_o/  \o_)( |
|/     /\     \|
(_     ^^     _)
 \__|IIIIII|__/
  | \IIIIII/ |
  \          /
   `--------`
    '''
    # ASCII'yi geçici bir dosyaya yazıp lolcat ile gösteriyoruz
    with open("skull.txt", "w") as f:
        f.write(skull)
    os.system("cat skull.txt | lolcat")
    os.remove("skull.txt")  # temizlik

figlet()