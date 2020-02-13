def toplama (a,b):
    return a + b
def cikartma (a,b):
    return a - b
def carpma (a,b):
    return a * b
def bolme (a,b):
    return a / b
print("Bir işlem seçiniz...")
print("Toplama işlemi için 1'e basınız.")
print("Çıkarma işlemi için 2'ye basınız.")
print("Çarpma işlemi için 3'e basınız.")
print("Bölme işlemi için 4'e basınız.")
secim = input("Hangi işlemi yapmak istersiniz (1 - 2 - 3 - 4):")
sayi1 = int(input("Birinci sayıyı giriniz = "))
sayi2 = int(input("İkinci sayıyı giriniz = "))
if secim == '1':
    print(sayi1,"+",sayi2,"=", toplama(sayi1,sayi2))
elif secim == '2':
    print(sayi1,"-",sayi2,"=", cikarma(sayi1,sayi2))
elif secim == '3':
    print(sayi1,"*",sayi2,"=", carpma(sayi1,sayi2))
elif secim == '4':
    print(sayi1,"/",sayi2,"=", bolme(sayi1,sayi2))
