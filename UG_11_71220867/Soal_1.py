def penjumlahan(bil1, bil2):
    jumlah=(bil1 + bil2)
    return jumlah
def pengurangan(bil1, bil2):
    kurang=(bil1 - bil2)
    return kurang
def perkalian(bil1, bil2):
    kali= (bil1 * bil2)
    return kali
def pembagian(bil1, bil2):
    bagi=(bil1 / bil2)
    return bagi


print("=========================")
print("Operasi Matematika")
print(" 1. Jumlah [+]")
print (" 2. Kurang [-]")
print (" 3. Kali [*]")
print (" 4. Bagi [/]")
print("=========================")
operasi= int(input("Pilih operasi (1/2/3/4): "))
print("=========================")
bil1= int(input("Masukkan bilangan pertama: "))
bil2= int(input("Masukkan bilangan kedua: "))
if operasi==1:
    print ("Hasil operasi dari",bil1,"+",bil2,"=",penjumlahan(bil1, bil2))
elif operasi==2:
    print ("Hasil operasi dari",bil1,"-",bil2,"=",pengurangan(bil1, bil2))
elif operasi==3:
    print ("Hasil operasi dari",bil1,"*",bil2,"=",perkalian(bil1, bil2))
elif operasi==4:
    print ("Hasil operasi dari",bil1,"/",bil2,"=",pembagian(bil1, bil2))
           
     
