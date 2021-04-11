"""
ASUDE MOR
morasude1@gmail.com
"""
"""
Ders Notu Başvurusu
. 5 öğrenci oluşturun. Kullanıcıdan bu öğrencilere sorun.
. Bu öğrencilerin her birinin bir ara notu, proje notu ve final notu olması gerekir.
. Her öğrencinin bir ders geçme notu olacaktır.
. passingGrade = midterm * (0.3) + project * (0.3) + final * (0.4) geçme notu bu şekilde belirlenmelidir.
. Bu öğrencilerin bilgilerini tutan bir sözlük oluşturun.
. Öğrencilerin notlarını hesaplayın ve indeksleme yardımı ile listeye aktarın.
. Son olarak, notu en yüksek olan öğrenciyi ilk dizinde ve en düşük notu olan öğrenciyi listenin son dizininde olacak şekilde ayarlayın.
"""
#Listeyiye aktarım ile olan kısmı Community kısmından sordum ama cevap alamadım o yüzden sözlük kullanarak yaptım.

def calc_average(passingGrade):
    if (0.0 <= midterm <= 100.0 and 0.0 <= project <= 100.0 and 0.0 <= final <= 100.0):
        passingGrade = midterm * (0.3) + project * (0.3) + final * (0.4)
        return passingGrade
    else:
        print("Hatalı giriş yaptınız. Lütfen girilen notları kontrol edip tekrar deneyin, çıkış yapılıyor.")
        exit()

users = {}
passingGrade = 0.0

for i in range(5):
    try:
        #her ogrencinin ismi alınır. Isimlerin karismamasi icin okul numarası da alınabilirdi
        isim = str(input("\nÖğrencilerin isimlerini giriniz: "))
        #her ogrencinin notlari alinir.
        midterm = float(input('{0} isimli öğrencinin ara sınavı notu: '.format(isim)))
        project = float(input('{0} isimli öğrencinin proje notu: '.format(isim)))
        final   = float(input('{0} isimli öğrencinin final notu: '.format(isim)))
        
        print (isim, "isimli öğrencinin geçme notu:", calc_average(passingGrade))
        users[isim] = calc_average(passingGrade)
        
    except ValueError:
        print("Hatalı giriş yaptınız. Lütfen girdiklerinizi kontrol edip tekrar deneyin, çıkış yapılıyor.")
        exit()
    
users = dict(sorted(users.items(), key=lambda item: item[1]))
#print(users)

print("\nEn yüksek notu alan\nÖğrencinin Adı:",list(users.keys())[-1], "\nNotu:", list(users.values())[-1])
print("\nEn düşük notu alan\nÖğrencinin Adı :",list(users.keys())[0], "\nNotu:", list(users.values())[0])
