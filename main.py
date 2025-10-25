import sys
#menampilkan sudo
def fmenampilkan_sudo():
    for baris in sudo:
        for nilai in sudo[baris].values():
            print(nilai,"",end="")
        print()
# mencari nikai sebaris
def fbaris(titik):
    baris = titik[0]
    nilai_baris = set([])
    for nilai in sudo[baris].values():
        nilai_baris.add(nilai)
    return nilai_baris
# mencari nilai sekolom
def fkolom(titik):
    nilai_kolom = set([])
    kolom = titik[1]
    for baris in sudo:
        nilai = sudo[baris][kolom]
        nilai_kolom.add(nilai)
    return nilai_kolom

# mencari nilai seblok
def fblok(titik):
    nilai_blok = set([])
    baris = titik[0]
    kolom = titik[1]

    if baris <= 2:
        panjang_baris = (1,2)
        if kolom <= 2:
            panjang_kolom = (1,2)
        else:
            panjang_kolom = (3,4)
    elif baris > 2:
        panjang_baris = (3,4)
        if kolom <= 2:
            panjang_kolom = (1,2)
        else:
            panjang_kolom = (3,4)
        
    for baris in panjang_baris:
        for kolom in panjang_kolom:
            nilai = sudo[baris][kolom]
            nilai_blok.add(nilai)
    return nilai_blok

# mengumpulkan nilai sudo
def fnilai_sudo():
    nilai_sudo = set([])
    for i in sudo.values():
        for j in i.values():
            nilai_sudo.add(j)
    return nilai_sudo

# soal sudo
sudo = {1: {1: 3, 2: 0, 3: 1, 4: 2},
        2: {1: 0, 2: 0, 3: 0, 4: 0},
        3: {1: 2, 2: 0, 3: 0, 4: 0},
        4: {1: 0, 2: 0, 3: 0, 4: 4}
        }
        
print("soal sudo 4x4:")
#menampilkan soal sudo
fmenampilkan_sudo()

# program utama
nilai_lengkap = set([1, 2, 3, 4])

while True:
    # mengumpulkan nilai sudo
    nilai_sudo = fnilai_sudo()
    # dummy nikai kemungkinan terpendek (nilai kemungkinan utana) yang akan di update ke sudo
    nilai_kemungkinan_utama = [1, 2, 3, 4, 5]
    #memeriksa apakah nilai 0 ada di sudo
    if 0 not in nilai_sudo:
        # jika tidak ada nilai 0 program berakhir
        print("\nJawaban: ")
        #menampilkan sudo
        fmenampilkan_sudo()
        break
    else:
        # jika ada nilai 0, cari titik (baris, kolom) bernilai 0
        for baris in sudo:
            for kolom in sudo[baris]:
                if sudo[baris][kolom] == 0:
                    titik = (baris,kolom)
                    # nilai sebaris
                    nilai_baris = fbaris(titik)
                    # nilai sekolom
                    nilai_kolom = fkolom(titik)
                    # nilai seblok
                    nilai_blok = fblok(titik)
                    # menggabungkan (union) nilai_baris, nilai_kolom dan nilai_blok
                    nilai_titik = nilai_baris | nilai_kolom | nilai_blok
                    # mencari kemungkinan nilai untuk nilai 0
                    nilai_kemungkinan = nilai_lengkap - nilai_titik
                    # mengubah tipe data set menjadi list
                    nilai_kemungkinan = list(nilai_kemungkinan)
                    # mencari nilai kemungjinan terpendek
                    if len(nilai_kemungkinan) < len(nilai_kemungkinan_utama):
                        nilai_kemungkinan_utama = nilai_kemungkinan
                        BARIS = baris
                        KOLOM = kolom
    # untuk menunjukan soal salah, dalam satu baris, kolom atau blok terdapat angka yang sama
    if nilai_kemungkinan_utama == []:
        print("\nJawaban sementara:")
        sudo[BARIS][KOLOM] = "i"
        fmenampilkan_sudo()
        print(f"eror: angka imajiner di ({BARIS},{KOLOM})")
        sys.exit()
    # mengupdate sudo
    nilai = nilai_kemungkinan_utama[0]
    sudo[BARIS][KOLOM] = nilai
