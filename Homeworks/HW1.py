"""
ASUDE MOR
morasude1@gmail.com
"""
"""
1. Bir Liste oluşturun ve listenin ikinci yarısını listenin ilk yarısıyla değiştirin ve bunu ekrana yazdırın.
2. Kullanıcıdan n değişkenine tek basamaklı bir tam sayı girmesini isteyin. Ardından, 0'dan n'ye (n dahil) tüm çift sayıları yazdırın.
"""

#my_list = [0,1,2,3,4,5,6,7,8,9]
#my_list = [15,3,2,9,4,8,2]
my_list = [0,1,2,3,4,5,6,7,8,9,10]
print("Listenin ilk hali:\t ",my_list)
uzunluk = len(my_list)
for i in range(uzunluk-1):
    if (uzunluk%2 == 0):    #eger uzunluk cift ise ortada eleman kalmadan ikiye bolunebilir.
        my_list[i], my_list[(uzunluk//2)+i] = my_list[(uzunluk//2)+i],my_list[i]
    elif (uzunluk %2 == 1):    #eger uzunluk tek ise ortada eleman kalir. Bu yuzden ortada kalan eleman sabit olarak yerinde kalmalidir.
        my_list[i], my_list[(uzunluk//2)+i+1] = my_list[(uzunluk//2)+i+1],my_list[i]
    if i == ((uzunluk//2)-1):break
	
print("Listenin swap olmuş hali:",my_list)

"""----------------------------------------------------"""
"""
#istenilenden tam olarak emin olamadigim icin listedeki elemanları swap etme islemini boyle de yaptim. Aslinda asagida yazdigim kodda listeyi tersten yaziyor.
#my_list = [0,1,2,3,4,5,6,7,8,9,10]
my_list = [0,1,2,3,4,5,6,7,8,9,10,11]
uzunluk = len(my_list)
for i in range(uzunluk-1):
    my_list[i], my_list[uzunluk-i-1] = my_list[uzunluk-i-1],my_list[i]
    if i == uzunluk//2:break

print(my_list)
"""
"""----------------------------------------------------"""
try:
    n = int(input("\nLütfen pozitif bir sayı giriniz: "))
    if n >= 0:
        print("\nÇift sayılar ")
        for i in range(0,n+1,2):    #girilen degerinde dahil olunmasini istedigimiz icin n+1. Ve cift sayilari istedigimiz icin artis miktarini 2.
            print(i,end=" ")        #arada bosluk birakarak cift sayilari yan yana yazar.
    else:
        print("\nLütfen pozitif bir sayı girin.")
  
except ValueError:
  print("\nLütfen pozitif bir sayı girin.")
