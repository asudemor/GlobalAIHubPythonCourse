"""
ASUDE MOR
morasude1@gmail.com
"""
"""
Bilgi yarışması
. Bir bilgi yarışması programı yazın.
. Toplamda 10 sorudan oluşmalıdır.
. Her sorunun yalnızca bir cevabı olacaktır.
. Soruların yanıtlarını büyük / küçük harf duyarlılığına göre ayarlayın.
. Her soru 10 puan değerinde olmalıdır.
. Kullanıcı 5 veya daha az soruyu yanıtlarsa, başarısız sayılacaktır.
. Kullanıcı 5'ten fazla soruyu doğru cevaplarsa başarılı sayılacaktır.
"""

class Question:
     def __init__(self, prompt, yarismaci_cevap):
          self.prompt = prompt
          self.yarismaci_cevap = yarismaci_cevap

sorular = [
     "Türkiye'nin başkenti ?\n-->",
     "Covid 19 vakası ilk olarak hangi şehirde görülmüştür ?\n-->",
     "Türkiye'nin pidesi ile ünlü olan şehri ?\n-->",
     "İstanbul kaç yılında fethedilmiştir ?\n-->",
     "Bu kodlar hangi dilde yazılmıştır ?\n-->",
     "İzmir şehri hangi bölgededir ?\n-->",
     "İstanbul'un plaka kodu ?\n-->",
     "Fatih'in posta kodu ?\n-->",
     "Bir yılda kaç hafta vardır ?\n-->",
     "TC numarasında kaç tane rakam vardır ?\n-->"
]

cevaplar = [
     Question(sorular[0], "ankara"),
     Question(sorular[1], "wuhan"),
     Question(sorular[2], "konya"),
     Question(sorular[3], "1453"),
     Question(sorular[4], "python"),
     Question(sorular[5], "ege"),
     Question(sorular[6], "34"),
     Question(sorular[7], "34093"),
     Question(sorular[8], "52"),
     Question(sorular[9], "11")
]

def quiz(cevaplar):
     puan = 0 #yarismacinin puanini tutar
     for dogru_cevap in cevaplar:
          yarismaci_cevap = input(dogru_cevap.prompt)
          if yarismaci_cevap.lower() == dogru_cevap.yarismaci_cevap.lower():        #dogru cevabi ve yarismacinin cevabini kucuk harfe donusturur.
              puan += 1                                                             #eger ikiside ayni ise puan 1 artar.

     print("Puanınız: ", puan, "/", len(cevaplar)". Tebrikler.")

quiz(cevaplar)

