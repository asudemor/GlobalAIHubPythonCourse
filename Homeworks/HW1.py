"""
ASUDE MOR
morasude1@gmail.com
"""
#my_list = [0,1,2,3,4,5,6,7,8,9]
my_list = [0,1,2,3,4,5,6,7,8,9,10]
uzunluk = len(my_list)
for i in range(uzunluk-1):
    if (uzunluk%2 == 0):    #eger uzunluk cift ise ortada eleman kalmadan ikiye bolunebilir.
        my_list[i], my_list[(uzunluk//2)+i] = my_list[(uzunluk//2)+i],my_list[i]
    elif (uzunluk %2 == 1):    #eger uzunluk tek ise ortada eleman kalir. Bu yuzden ortada kalan eleman sabit olarak yerinde kalmalidir.
        my_list[i], my_list[(uzunluk//2)+i+1] = my_list[(uzunluk//2)+i+1],my_list[i]
    if i == ((uzunluk//2)-1):break
	
print(my_list)

"""----------------------------------------------------"""
#istenilenden tam olarak emin olamadigim icin listedeki elemanları swap etme islemini boyle de yaptim. Aslinda asagida yazdigim kodda listeyi tersten yaziyor.
#my_list = [0,1,2,3,4,5,6,7,8,9,10]
my_list = [0,1,2,3,4,5,6,7,8,9,10,11]
uzunluk = len(my_list)
for i in range(uzunluk-1):
    my_list[i], my_list[uzunluk-i-1] = my_list[uzunluk-i-1],my_list[i]
    if i == uzunluk//2:break

print(my_list)

"""----------------------------------------------------"""
n = int(input("Lütfen tek basamaklı bir sayı giriniz: "))
if n < 0:   #eger girilen sayi negatifse hata bildiriyor. try blogu ile de yapilabilirdi.
	raise Exception("Lutfen pozitif bir sayı girin.")
else:
    print("Çift sayılar: ")
    for i in range(0,n+1,2):    #girilen degerinde dahil olunmasini istedigimiz icin n+1. Ve cift sayilari istedigimiz icin artis miktarini 2.
        print(i,end=" ")        #arada bosluk birakarak cift sayilari yan yana yazar.

