
print("Bu örnek kullanıcı tarafıdan virgül ile girilen sayıların ortalamasını hesaplar")

numaralar = input("Virgül ile sayıları giriniz.: ")

print("Girdiğiniz Sayılar: {0}".format(numaralar))

numaralarArr=numaralar.split(",")
toplam = 0
for n in numaralarArr:
   toplam = toplam + int(n)

print("GİRDİĞİNİZ SAYILARIN ORTALMASI:{0:.2f} ".format(toplam / len(numaralarArr)))
