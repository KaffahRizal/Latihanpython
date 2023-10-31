#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

listKendaraan =["Kawasaki_Ninja_H2R","Motor","998_CC","Metalic_Green","Roda_Dua"]
listKendaraan.append("750.000")
listKendaraan.append("BahanBakarBensin")
print(listKendaraan)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


lang = input (""">>>>>>>>>>>>>>PILIHLAH_Nomor_RUMUS_YANG_INGIN_DIGUNAKAN<<<<<<<<<<
       1.RUMUS_LUAS_PERSEGI
       2.RUMUS_LUAS_LINGKARAN
       3.RUMUS_LUAS_SEGITIGA
                 Answer=""")
match lang:
    case "1":
        s = int(input("masukkan sisi :"))
        persegi = s * s
        print("luas Persegi =",persegi)
    case "2":
        phi = 3.14
        r = int(input("masukkan jari-jari :"))
        lingkaran = phi*r*r
        print("luas lingkaran =",lingkaran)
    case "3":
        m = 1/2
        a = int(input("masukkan Alas :"))
        t = int(input("Masukkan Tinggi :"))
        Segitiga = a * t * m
        print("luas Segitiga =",Segitiga)
    case _:
        print("RUMUS TIDAK TERDETEKSI")
   
     
      
     
    






