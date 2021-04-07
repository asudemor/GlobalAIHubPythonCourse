my_list = [0,1,2,3,4,5,6,7,8,9]
uzunluk = len(my_list)
for i in range(uzunluk-1):
    my_list[i], my_list[(uzunluk//2)+i] = my_list[(uzunluk//2)+i],my_list[i]
    if i == ((uzunluk//2)-1):break
	
print(my_list)

"""----------------------------------------------------"""
my_list = [0,1,2,3,4,5,6,7,8,9]
for i in range(uzunluk-1):
    my_list[i], my_list[uzunluk-i-1] = my_list[uzunluk-i-1],my_list[i]
    if i == uzunluk//2:break

print(my_list)

"""----------------------------------------------------"""
n = int(input("Lütfen tek basamaklı bir sayı giriniz: "))
if n < 0:
	raise Exception("Lutfen pozitif bir sayı girin.")
else:
    print("Çift sayılar: ")
    for i in range(0,n+1,2):
        print(i,end=" ")
        
