"""
ASUDE MOR
morasude1@gmail.com
"""
"""
Kullanıcı oturum açma uygulaması:
. Kullanıcıdan kullanıcı adı ve şifre değerlerini alın.
. Bir if ifadesindeki değerleri kontrol edin ve kullanıcıya başarılı olup olmadıklarını söyleyin.

Ekstra:
. Aynı kullanıcı oturum açma uygulamasını oluşturmayı deneyin, ancak bu sefer bir sözlük kullanın!
"""

print("----------------------- SORU 1 -----------------------")
system_username = "asudemor"
system_password = "123456"

durum = 1
while durum != "0":
    username = input("\nLütfen Kullanıcı Adınızı Giriniz: ")
    password = input("\nLütfen Şifrenizi Giriniz: ")

    if (username == system_username) and (password != system_password):
        print("\nŞifre yanlış..")
        durum = input("\nGirise devam etmek istiyor musunuz? (0/1)")
    
    elif (username != system_username) and (password == system_password):
        print("\nKullanıcı adı yanlış..")
        durum = input("\nGirise devam etmek istiyor musunuz? (0/1)")
    
    elif (username != system_username) and (password != system_password):
        print("\nKullanıcı adı ve şifre yanlış..")
        durum = input("\nGirise devam etmek istiyor musunuz? (0/1)")
    
    else:
        print("\n----- Hoşgeldin ",username," -----\n")
        durum = 0
        break


print("----------------------- SORU 2 -----------------------")
#with dictionary
users = {}      #girilen kullanicilari sozlukte saklar.
durum = ""

def Menu():
    durum =input("\nLütfen yapacağınız işlemi seçin\nÜye Girişi (ug) - Yeni Kayıt (yk) - Çıkış (-1): ")
    if durum == "ug":
        eski_kullanici()
    elif durum == "yk":
        yeni_kullanıcı()
    elif durum == "-1":
        print("\nSisteme kayıtlı üyelerimiz: ",users)
        exit()
    else:print("\nLütfen geçerli durumları giriniz")

def yeni_kullanıcı():
    uye_giris =input("\nKullanıcı adını girin: ")
    if uye_giris in users:
        print ("\nZaten sisteme kayıtlısınız!")
    else:
        password =input("\nŞifreyi girin: ")
        users[uye_giris] = password
        print("\nKayıt başarılı")     

def eski_kullanici():
    login =input("\nKullanıcı adını girin: ")
    Password =input("\nŞifreyi girin: ")

    if login in users and users[login] == Password:
        print("\n----- Hoşgeldin ",login," -----")
    elif login not in users :
        print("\nKullanıcı bulunamadı.")
    elif users[login] != Password:
        print("\nGirilen şifre hatalı.")        

while durum !="-1":
    Menu()
