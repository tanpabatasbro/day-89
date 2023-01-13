print("""Buatlah program yang dapat menerima 2 input angka dengan ketentuan sebagai 
-Jika penjumlahan kedua nilai adalah genap, maka tambahkan angka 1
-Jika penjumlahan kedua adalah ganjil, maka jumlah ditambah 2""")

a = int(input("Masukkan Angka : "))
b = int(input("Masukkan Angka : "))

if a %2 == 0 and b %2 ==0:
    c = a + b + 1
    print(f"{a} + {b} + 1 = {c} ")
elif a %2 != 0 and b %2 != 0:
    c = a + b + 2
    print(f"{a} + {b} + 2 = {c}")
else:
    c = a + b
    print(f"{a} + {b} = {c}")