# ARITHMETICS OPERATORS # buat versi ASSINGMENT NYAAAAA1!!!
x = 5
y = 10
hasil =( x * y )
print (hasil)
hasil2 = ( y / x )
print (hasil2)
hasil3 = ( y // x )
print (hasil3)
hasil4 = ( x ** y )
print (hasil4)
X = 100
Y = 50
hasil5 = ( Y % X )
print (hasil5)

# STRUKTUR KENDALI IF DLL
# (\n) berfungsi untuk membuat baris baru di hasil
pelanggan = "MC.HARRY"
TotalBelanja = 250000
if (TotalBelanja > 150000) : 
    keterangan = "SELAMAT ANDA MENDAPATKAN HADIAH \n TERIMAKASIH SUDAH BERBELANJA"
    
else :
    keterangan = "TERIMAKASIH SUDAH BERBELANJA"
print("pelanggan",pelanggan,"\nTotal Belanja Anda Rp.",TotalBelanja,"\n",keterangan)

#SISWA DINYATAKAN LULUS MINIMAL NILAINYA 60

NAMA = "BUDI SANTOSO"
MATPEL = "MATEMATIKA"
NILAI = 99.99

#TENARY INI ADALAH VERSI SINGKATNYA DARI APLIKASI KETERANGAN JENIS SOAL SEBELUMNYA
KETERANGAN = " LULUS " if NILAI >= 60 else "GAGAL"

#CETAK DATA
print ("Nama Siswa \t:",NAMA,"\nMata Pelajaran \t:",MATPEL,"\nNilai \t\t:",NILAI,"\nKeterangan \t:",KETERANGAN)

#(IF)MULTI KONDISI 

NAMA = "BUDI SANTOSO"
MATPEL = "MATEMATIKA"
NILAI = 99.99

#UJI GRADE MULTI KONDISI
if(NILAI >= 85 and NILAI <= 100):
    GRADE = "A"
elif(NILAI >= 75 and NILAI < 100):
    GRADE = "B"
elif(NILAI >= 60 and NILAI < 100):
    GRADE = "C"
elif(NILAI >= 30 and NILAI < 100):
    GRADE = "D"
else :
    GRADE = "E"

print ("Nama Siswa \t:",NAMA,"\nMata Pelajaran \t:",MATPEL,"\nNilai \t\t:",NILAI,"\nGRADE \t\t:",GRADE)

#TUGAS ASDOS 
NAMA = "BUDI SANTOSO"
USIA = 25

#UJI GRADE MULTI KONDISI SOAL NO 1
print ("ini soal no 1")
if( USIA < 18 ):
    keterangan = "Anak-anak"
elif( USIA >= 18 and USIA < 65):
    keterangan = "Dewasa"
else :
    keterangan = "Lanjut Usia"

print ("Nama \t\t:",NAMA,"\nUsia \t\t:",USIA,"\nKeterangan \t:",keterangan)

#UJI GRADE MULTI KONDISI SOAL NO 2
print ("ini soal no 2")
X = 34
Y = 24

if ( X > Y ):
    keterangan = "X lebih besar dari Y"
else :
    keterangan = "X tidak lebih besar dari Y"
print ("NILAI X \t:",X,"\nNILAI Y\t\t:",Y,"\nKeterangan \t:",keterangan)
    



    