"""
ASUDE MOR
morasude1@gmail.com
"""

system_username = "asudemor"
system_password = "123456"

durum = 1
while durum != "0":
    username = input("Lütfen Kullanıcı Adınızı Giriniz: ")
    password = input("Lütfen Şifrenizi Giriniz: ")

    if (username == system_username) and (password != system_password):
        print("Şifre yanlış..")
        durum = input("Girise devam etmek istiyor musunuz? (0/1)")
    
    elif (username != system_username) and (password == system_password):
        print("Kullanıcı adı yanlış..")
        durum = input("Girise devam etmek istiyor musunuz? (0/1)")
    
    elif (username != system_username) and (password != system_password):
        print("Kullanıcı adı ve şifre yanlış..")
        durum = input("Girise devam etmek istiyor musunuz? (0/1)")
    
    else:
        print("----- Hoşgeldin ",username," -----")
        durum = 0

"""----------------------------------------------------------------------------------"""

#with dictionary
users = {}      #girilen kullanicilari sozlukte saklar.
durum = ""

def Menu():
    durum =input("Lütfen yapacağınız işlemi seçin\nÜye Girişi (ug) - Yeni Kayıt (yk) - Çıkış (-1): ")
    if durum == "ug":
        eski_kullanici()
    elif durum == "yk":
        yeni_kullanıcı()
    elif durum == "-1":
        print(users)
        exit()
    else:print("Lütfen geçerli durumları giriniz")

def yeni_kullanıcı():
    uye_giris = input("Kullanıcı adını girin: ")
    if uye_giris in users:
        print ("Zaten sisteme kayıtlısınız!")
    else:
        password =input("Şifreyi girin: ")
        users[uye_giris] = password
        print("Kayıt başarılı")     

def eski_kullanici():
    login =input("Kullanıcı adını girin: ")
    Password =input("Şifreyi girin: ")

    if login in users and users[login] == Password:
        print("----- Hoşgeldin ",login," -----")
    elif login not in users :
        print("Kullanıcı bulunamadı.")
    elif users[login] != Password:
        print("Girilen şifre hatalı.")        

while durum !="-1":
    Menu()
