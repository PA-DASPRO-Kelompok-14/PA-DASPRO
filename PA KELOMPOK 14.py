import json
import pwinput
import os
from prettytable import PrettyTable 
os.system("cls")


# dictionary utuk akun admin supermarket AHA
akun_admin = {"Username" : ["admin1"],
            "Password" : ["123"]} 

# prettytable
etalase_produk = PrettyTable()      #untuk memanggil prettytable menampilkan daftar produk
etalase_produk.field_names = ["ID Produk","Nama Produk","Harga Produk", "Stok Produk"]

# json login
json_path_login = "C:\\Users\\ASUS\\Desktop\\project akhir\\tesPA\\data_user.json"
with open(json_path_login, "r") as baca_user:
    user = json.load(baca_user)

def datacust():
    with open(json_path_login, "w") as tambah_user:
        json.dump(user, tambah_user, indent=4)

nm = user.get("Usernames")
pw = user.get("Passwords")
em = user.get("e-Money")

# json produk
json_path_produk = "C:\\Users\\ASUS\\Desktop\\project akhir\\tesPA\\produk.json"#untuk membuka file json yang menyimpan
with open(json_path_produk, "r") as baca_produk:
    produk = json.load(baca_produk)

def penyimpanan():
    with open(json_path_produk, "w") as tambah_produk:
        json.dump(produk, tambah_produk, indent=4)

ip = produk.get("ID Produk")
np = produk.get("Nama Produk")
hp = produk.get("Harga Produk")
sp = produk.get("Stok Produk")

# function login admin
def login_admin():
    print("""
    ==============================
    |        LOGIN ADMIN         |
    ==============================
        """)

    while True : 
        try :
            input_username = input("Masukkan username : ")
            input_password = pwinput.pwinput("Masukkan Password : ")
            iusername = input_username.lower()

            user_admin = akun_admin.get("Username").index(input_username)
            password_admin = akun_admin.get("Password").index(input_password)

            if iusername == akun_admin.get("Username")[user_admin] and input_password == akun_admin.get("Password")[password_admin]:

                os.system("cls")
                print("")
                print("        --- LOGIN BERHASIL ---\n")
                print("Selamat datang,", iusername)
                return menuHomeAdmin()
            
        except ValueError:
            print("\n> TERJADI KESALAHAN")
            print("> SILAHKAN COBA LAGI\n")

# function registrasi akun baru
def regis():
    print("""
    ==============================
    |    REGISTRASI AKUN BARU    |
    ==============================
        """)
    while True:
        try :
            uname = input("Masukkan username: ")
            if all(x.isspace () for x in uname):
                print("> INPUT TIDAK BOLEH KOSONG")
                print("> Coba lagi\n")

            elif all(x.isalpha() for x in uname):
                if uname in user["Usernames"]:
                    print("> USERNAME TELAH TERDAFTAR\n")
                    while True :
                        login_pembeli()
                        break
                else:
                    password = pwinput.pwinput("Masukkan password: ")
                    if all(x.isspace () for x in password):
                        print("> INPUT TIDAK BOLEH KOSONG, COBA ULANG\n")
                        
                    elif all(x.isnumeric() for x in password):
                        Saldo = 0
                        nm.append(uname)
                        pw.append(password)
                        em.append(Saldo)
                        datacust()

                        os.system('cls')
                        print("\n     ---- AKUN BERHASIL DIBUAT ----")
                        menu_pembeli()
                        break
                    else :
                        print("> PASSWORD HARUS BERNILAI ANGKA")
            else:
                print("> USERNAME YANG DIMASUKAN HARUS ALPHABET")
        except ValueError:
            print("> INVALID INPUT\n")

def login_pembeli ():
    print("""
    ==============================
    |        LOGIN PEMBELI       |
    ==============================
        """)
    while True :
            global cari
            uname = input("Masukkan username: ")
            password = pwinput.pwinput("Masukkan password: ")
            cari = nm.index(uname)

            if uname == nm[cari] and password == pw[cari]:
                print("\n          ---LOGIN BERHASIL---")
                print("          Selamat Datang", uname)
                return menuHomepembeli()

def tampilan_awal():
    print("""
    +---------------------------+
    |        LOGIN SEBAGAI      |
    +---------------------------+
    |1.|         ADMIN          |
    |2.|        PEMBELI         |
    |3.|        KELUAR          |
    +---------------------------+ 
        """)
    
def tampilan_pembeli() :
    print("""
    +----------------------------+
    |         OPSI LOGIN         |
    +----------------------------+
    |1.|     REGISTRASI AKUN     |
    |2.|      LOGIN AKUN         |
    |3.|        KELUAR           |
    +----------------------------+
    """)

def tampilan_admin():
    print("""
    +----------------------------+
    |         MENU ADMIN         |
    +----------------------------+
    |1.|     TAMBAH BARANG       |
    |2.|    TAMPILKAN BARANG     |
    |3.|      UBAH BARANG        |
    |4.|     HAPUS BARANG        |
    |5.|        KELUAR           |
    +----------------------------+
        """)
    
def menu_belanja_pembeli():
        print("""
    +----------------------------+
    |        MENU PEMBELI        |
    +----------------------------+
    |1.|      BELI BARANG        |
    |2.|   CEK SALDO E-MONEY     |
    |3.|    TOP UP E-MONEY       |
    |4.|        KELUAR           |
    +----------------------------+
        """)

def metode_beli():
    print(
        """
        +-------------------------------+
        |       METODE PEMBAYARAN       |
        +-------------------------------+
        |1.| Cash                       |
        |2.| e-Money                    |
        +-------------------------------+
            """
    )

def top_up () :
        print("""
    +----------------------------+
    |        TOP UP E-MONEY      |
    +----------------------------+
    |1.|       Rp 50.000         |
    |2.|       Rp 100.000        |
    |3.|       Rp 300.000        |
    |4.|       Rp 500.000        |
    |5.|        KELUAR           |
    +----------------------------+
        """)

def menuHomepembeli():
    try :
        while True:
            menu_belanja_pembeli()
            pilihan = int(input("Masukkan nomor menu yang Anda inginkan (1/2/3/4): "))

            if pilihan == 1:
                beli_barang()
            elif pilihan == 2:
                cek_saldo()
            elif pilihan == 3:
                emoney()
            elif pilihan == 4:
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
    except ValueError :
        print("> PERHATIKAN INPUT")

#function menu pembeli
def menu_pembeli() :
    try :
        while True :
            tampilan_pembeli()
            awal = input("Pilih opsi (1/2/3): ")
            if awal == "1":
                os.system('cls')
                regis()
            elif awal == "2":
                os.system("cls")
                login_pembeli()
            elif awal == "3":
                os.system("cls")
                break
            else:
                print("Invalid")
                break
    except ValueError :
        print("> PERHATIKAN INPUT")


def create():
    read()
    print("\n+--------TAMBAHKAN PRODUK BARU--------+")
    while True:
        try:
            id_produk = int(input("Masukan ID Produk : "))
            id_produk_str = str(id_produk)

            if id_produk <= 0:
                print("> INPUT HARUS LEBIH DARI 0")
            elif id_produk in produk["ID Produk"]:
                print("> ID PRODUK SUDAH ADA, MASUKIN LAINNYA")
            elif id_produk_str.isspace():
                print("> INPUT TIDAK BOLEH KOSONG")
            elif len(id_produk_str) > 3:
                print("> ID PRODUK TIDAK BOLEH LEBIH DARI 3 ANGKA\n")
            else:
                break
                
        except ValueError:
            print("> PERHATIKAN INPUT")


    while True:
        try :
            nama = input("Masukan Nama Produk : ").strip()
            if nama in produk["Nama Produk"]:
                cari_produk = produk.get("Nama Produk").index(nama)
                produk["Stok Produk"][cari_produk] = produk.get("Stok Produk")[cari_produk] +1
                read()
            elif all(x.isspace () for x in nama):
                print("> INPUT TIDAK BOLEH KOSONG")
            elif all(x.isalpha() for x in nama) and len(nama) <= 20:
                break
            elif len(nama) > 20:
                print("> NAMA PRODUK TIDAK BOLEH LEBIH DARI 20\n")
            elif all(x.isnumeric() for x in nama):
                print("> INPUT TIDAK BOLEH ANGKA\n")
            else:
                break
        except ValueError:
            print("> PERHATIKAN INPUT")
            
    while True:
        try:
            harga = int(input("Masukan Harga Produk : Rp "))

            if harga < 0:
                print("HARGA TIDAK BOLEH KURANG DARI 0")
            elif harga == 0:
                print("HARGA HARUS LEBIH DARI 0")
            elif harga < 100000000 :
                break
            elif harga > 100000000 :
                print("> Harga Produk tidak boleh lebih dari 100000000\n")
            else:
                print("> TOLONG MASUKAN INPUT YANG BENAR")
                print("> SILAHKAN COBA LAGI\n")
        except ValueError:
            print("> MASUKAN ANGKA")

    while True:
        try:
            stok = int(input("Masukan Stok Produk : "))
            if stok < 0:
                print("> STOK PRODUK TIDAK BOLEH KURANG DARI 0 0")
            elif stok > 0 and stok <= 1000 :
                break
            elif stok > 50 :
                print("> STOK PRODUK TIDAK BOLEH MELEBIHI 1000 PRODUK\n")
            else :
                print("> INPUT YANG DIMASUKAN SALAH, COBA LAGI")
        except ValueError:
            print("> MASUKAN ANGKA")
        
    ip.append(id_produk)
    np.append(nama)
    hp.append(harga)
    sp.append(stok)
    os.system("cls")
    penyimpanan()
    
    print("--- PRODUK BERHASIL DITAMBAHKAN ---\n")
    read()

def read():
    # Mengurutkan produk berdasarkan "ID Produk"
    sorted_produk = sorted(zip(produk["ID Produk"], produk["Nama Produk"], produk["Harga Produk"], produk["Stok Produk"]), key=lambda x: x[0])

    etalase_produk.clear_rows()
    for item in sorted_produk:
        etalase_produk.add_row([
            item[0],
            item[1],
            "Rp." + str(item[2]),
            item[3]
        ])
    
    print(etalase_produk)

def update():
    read()
    print("\n+--------UBAH PRODUK--------+")
    while True:
        try :
            nama_produk = int(input("Masukkan ID Produk yang ingin diubah: "))
            pilih_update = produk.get("ID Produk").index(nama_produk)
            break
        except : 
            print("NAMA PRODUK TIDAK DITEMUKAN")
            print("SILAHKAN COBA LAGI")

    while True :
        pilih= input("\n>> Anda mau mengubah produk? (y/t) : ")
        if pilih == "y":
            nama_produk_baru= input(" Masukan nama produk baru : ")
            if nama_produk_baru in produk["Nama Produk"] :
                print("> NAMA YG DIMASUKAN SUDAH ADA")
                print("> MASUKAN NAMA PRODUK YG BERBEDA\n")
            elif all(x.isalpha() for x in nama_produk_baru) and len(nama_produk_baru) <= 20:
                produk.get("Nama Produk")[pilih_update] = nama_produk_baru
                print("--- Nama Produk berhasil diubah ---\n")
                penyimpanan()
                break
            else :
                print("> NAMA PRODUK HANYA BOLEH ALPHABET")
                print("> NAMA TIDAK BOLEH LEBIH DARI 20 HURUF")

        elif pilih == "t":
            break
        else :
            print("> PILIHAN TIDAK TERSEDIA")

    while True:
        pilih1 = input("\n>> Apakah anda ingin mengubah harga produk? (y/t) : ")
        if pilih1 == "y":
            while True :
                try :
                    harga_produk_baru = int(input("~ Masukkan harga produk baru : Rp. "))
                    if harga_produk_baru < 0:
                        print("HARGA TIDAK BOLEH KURANG DARI 0")
                    elif harga_produk_baru == 0:
                        print("HARGA HARUS LEBIH DARI 0")
                    elif harga_produk_baru > 0 and harga_produk_baru < 100000000:
                        produk.get("Harga Produk")[pilih_update] = harga_produk_baru
                        print("--- Harga Produk berhasil diubah ---\n")
                        penyimpanan()
                        break
                    else :
                        print("HARGA PRODUK TIDAK BISA LEBIH DARI 100000000")
                except :
                    print("PERHATIKAN INPUTAN")
            break
        elif pilih1 == "t":
            break
        else :
            print("PILIHAN TIDAK TERSEDIA")

    while True:
        sm = input("\n>> Apakah anda ingin mengubah stok produk? (y/t) : ")
        if sm == "y":
            while True :
                try:
                    sp_b = int(input("~ Masukkan stok produk baru : "))
                    if sp_b < 0 :
                        print("STOK TIDAK BOLEH KURANG DARI 0")
                    elif sp_b <= 1000:
                        produk.get("Stok Produk")[pilih_update] = sp_b
                        print("--- Stok Produk berhasil diubah ---\n")
                        penyimpanan()
                        break
                    else:
                        print("[] STOK TIDAK BOLEH LEBIH DARI 1000")
            
                except ValueError :
                    print("\n[] TOLONG MASUKAN ANGKA")
                    print("[] SILAHKAN COBA LAGI")
            break
        elif sm == "t":
            break
        else :
            print("[] PILIHAN TIDAK TERSEDIA")


def delete():
    read()
    print("\n+--------HAPUS PRODUK--------+")
    
    while True:
        try:
            hapus = int(input("Masukkan ID produk yang ingin dihapus: "))
            
            if hapus in produk["ID Produk"]:
                hapus_produk = produk["ID Produk"].index(hapus)
                produk["ID Produk"].pop(hapus_produk)
                produk["Nama Produk"].pop(hapus_produk)
                produk["Harga Produk"].pop(hapus_produk)
                produk["Stok Produk"].pop(hapus_produk)
                
                # Mengatur ulang ID Produk secara otomatis
                for i in range(hapus_produk, len(produk["ID Produk"])):
                    produk["ID Produk"][i] = i + 1  # ID Produk diatur ulang sesuai urutan
                
                penyimpanan()
                read()
                break
            else:
                print("PRODUK TIDAK DITEMUKAN")
        except ValueError:
            print("Masukkan ID Produk yang valid.")

def menuHomeAdmin ():
    while True :
        try :
            tampilan_admin ()
            pilihan = str(input("Masukkan pilihan (1/2/3/4/5) : "))
            
            if pilihan == "1":
                os.system("cls")
                while True:
                    create()
                    lanjut = input("Mau nambah data lagi? (y/t) : ")
                    lanjut_lagi = lanjut.lower()
                    if lanjut_lagi == "y":
                        print("Silahkan tambahkan produk baru")
                    elif lanjut_lagi == "t":
                        os.system('cls')
                        break
                    else :
                        print("> INPUT HARUS BERUPA (y/t)")
            elif pilihan == "2":
                os.system("cls")
                while True :
                    read()
                    lanjut = input("Mau kembali ke menu? (y/t) : ")
                    lanjut_lagi = lanjut.lower()
                    if lanjut_lagi == "y":
                        os.system('cls')
                        break
                    elif lanjut_lagi == "t":
                        read()
                    else :
                        print("> INPUT HARUS BERUPA (y/t)")
            elif pilihan == "3":
                os.system("cls")
                while True:
                    update()
                    lanjut = input("Mau mengubah data lagi? (y/t) :")
                    lanjut_lagi = lanjut.lower()
                    if lanjut_lagi == "y":
                        print("Silahkan lanjut Ubah data ")
                    elif lanjut_lagi == "t":
                        os.system('cls')
                        break
                    else :
                        print("> INPUT HARUS BERUPA (y/t)")
                            
            elif pilihan == "4":
                os.system("cls")
                while True:
                    delete()
                    lanjut = input("Mau menghapus data lagi? (y/t) :")
                    lanjut_lagi = lanjut.lower()
                    if lanjut_lagi == "y":
                        print("Silahkan lanjut hapus data")
                    elif lanjut_lagi == "t":
                        os.system('cls')
                        break
                    else :
                        print("> INPUT HARUS BERUPA (y/t)")
                
            elif pilihan == "5":
                os.system("cls")
                break
            else:
                print("> PILIHAN HARUS DARI 1-5, COBA LAGI")
                menuHomeAdmin()
                break

        except Exception as e:
            print(f"> TERJADI KESALAHAN: {str(e)}")

def emoney():

    while True :
        print(f"\n    <<<  Saldo : {user['e-Money'][cari]}  >>>")
        top_up()
        topup = int(input("Pilih nominal Top Up : "))

        if topup == 1 :
            user["e-Money"][cari] = user["e-Money"][cari] + 50000
            with open("emoney.txt", "a") as c:
                print("\n================================================",file=c,)
                print("Saldo e-Money berhasil ditambah Rp", 50000, file=c)
                print("------------------------------------------------",file=c)
                print("Saldo e-Money anda sekarang Rp",user['e-Money'][cari], file=c)
                print("================================================",file=c,)

            print("\n<<< Pengisian saldo e-Money Berhasil >>>")
            print("      Saldo e-Money : Rp", user['e-Money'][cari])
            datacust()
            break

        if topup == 2 :
            user["e-Money"][cari] = user["e-Money"][cari] + 100000
            with open("emoney.txt", "a") as c:
                print("\n================================================",file=c,)
                print("Saldo e-Money berhasil ditambah Rp", 100000, file=c)
                print("------------------------------------------------",file=c)
                print("Saldo e-Money anda sekarang Rp",user['e-Money'][cari], file=c)
                print("================================================",file=c,)

            print("\n<<< Pengisian saldo e-Money Berhasil >>>")
            print("      Saldo e-Money : Rp", user['e-Money'][cari])
            datacust()
            break

        if topup == 3 :
            user["e-Money"][cari] = user["e-Money"][cari] + 300000
            with open("emoney.txt", "a") as c:
                print("\n================================================",file=c,)
                print("Saldo e-Money berhasil ditambah Rp", 300000, file=c)
                print("------------------------------------------------",file=c)
                print("Saldo e-Money anda sekarang Rp",user['e-Money'][cari], file=c)
                print("================================================",file=c,)

            print("\n<<< Pengisian saldo e-Money Berhasil >>>")
            print("      Saldo e-Money : Rp", user['e-Money'][cari])
            datacust()
            break

        if topup == 4 :
            user["e-Money"][cari] = user["e-Money"][cari] + 500000
            with open("emoney.txt", "a") as c:
                print("\n================================================",file=c,)
                print("Saldo e-Money berhasil ditambah Rp", 500000, file=c)
                print("------------------------------------------------",file=c)
                print("Saldo e-Money anda sekarang Rp",user['e-Money'][cari], file=c)
                print("================================================",file=c,)

            print("\n<<< Pengisian saldo e-Money Berhasil >>>")
            print("      Saldo e-Money : Rp", user['e-Money'][cari])
            datacust()
            break
        break


def beli_barang() :
    while True :
        read()
        beli = int(input("Masukkan Nama produk yang ingin anda beli : "))
        if beli in produk["ID Produk"]:
            cari_produk = produk.get("ID Produk").index(beli)

            if produk["Stok Produk"][cari_produk] >= 0 :
                jumlah_produk = int(input("jumlah produk : "))
                if jumlah_produk > 0 :
                    if jumlah_produk < produk["Stok Produk"][cari_produk] or jumlah_produk == produk["Stok Produk"][cari_produk]:
                            global cari_nama
                            cari_harga = produk.get("ID Produk").index(beli)
                            cari_nama = produk.get("ID Produk").index(beli)
                            nama_barang = produk.get("Nama Produk")[cari_nama]
                            total_harga = produk.get("Harga Produk")[cari_harga]
                            totalan = jumlah_produk * total_harga
                            pilih_bayar(beli,jumlah_produk,totalan,cari_produk,nama_barang)
                            break
                    else :
                        print ("> STOK PRODUK TIDAK CUKUP")
                        print("> SILAHKAN COBA LAGI\n")
                else :
                    print("> JUMLAH TIDAK BOLEH KURANG DARI 0")   
            else : 
                print("--- STOK PRODUK TELAH HABIS ---")
                break
        else:
            print("> PRODUK TIDAK DITEMUKAN")
                    
        while True:
            try:
                Lanjut = input(">> Apakah anda ingin belanja lagi? (y/t) : ")
                if Lanjut == "y":
                    os.system('cls')
                    break
                    
                elif Lanjut == "t":
                    os.system('cls')
                    return
                    
                else:
                    print("> INPUT SALAH\n")
            except:
                print("> MOHON PERHATIKAN INPUTAN\n")
            

def pilih_bayar(beli,jumlah_produk,totalan,cari_produk,nama_barang) :
    print("\n    <<< Silahkan pilih metode pembayaran anda >>>")

    while True:
        metode_beli ()
        pilbayar = int(input("Pilih metode pembayaran : "))
        if pilbayar == 1:
            uang = int(input("Masukkan nominal uang anda : "))
            if uang > totalan:
                kembalian = uang - totalan

                with open("transaksi.txt", "a") as a:
                    print("\n----------TRANSAKSI BERHASIL-----------")

                    print("\n===================================", file=a)
                    print("              AHA MART             ", file=a)
                    print("===================================", file=a)
                    print("  Barang    :", nama_barang, file=a)
                    print("  Jumlah    :", jumlah_produk, file=a)
                    print("-----------------------------------", file=a)
                    print("  Total     : Rp", totalan, file=a)
                    print("-----------------------------------", file=a)
                    print("  Uang      : Rp", uang, file=a) 
                    print("  Kembalian : Rp", kembalian, file=a)
                    print("===================================", file=a)
                produk["Stok Produk"][cari_produk] = produk.get("Stok Produk")[cari_produk] - jumlah_produk

            elif uang < totalan:
                total_kurang = totalan - uang
                print("\n----------TRANSAKSI GAGAL-----------\n")
                print("-------------------------------------")
                print("Uang anda kurang sebesar Rp.", total_kurang)
                print("-------------------------------------")
                
            
            elif uang == totalan:
                print("")
            
                kembalian = uang - totalan
                with open("transaksi.txt", "a") as a:
                    print("\n----------TRANSAKSI ANDA BERHASIL-----------")

                    print("\n===================================", file=a)
                    print("              AHA MART             ", file=a)
                    print("===================================", file=a)
                    print("  Barang    :", nama_barang, file=a)
                    print("  Jumlah    :", jumlah_produk, file=a)
                    print("------------------------------------", file=a)
                    print("  Total     : Rp", totalan, file=a)
                    print("------------------------------------", file=a)
                    print("  Uang      : Rp", uang, file=a) 
                    print("  Kembalian : Rp", kembalian, file=a)
                    print("===================================", file=a)
                produk["Stok Produk"][cari_produk] = produk.get("Stok Produk")[cari_produk] - jumlah_produk
    

        elif pilbayar == 2:
            if user['e-Money'][cari] > totalan:
                produk.get("Stok Produk")[cari_produk] = produk["Stok Produk"][cari_produk] - jumlah_produk
                user.get("e-Money")[cari] = user["e-Money"][cari]- totalan
                penyimpanan()
                datacust()
                with open("transaksi.txt", "a") as a:
                    print("\n----------TRANSAKSI ANDA BERHASIL-----------")

                    print("\n===================================", file=a)
                    print("              AHA MART             ", file=a)
                    print("===================================", file=a)
                    print("  Barang     :", nama_barang, file=a)
                    print("  Jumlah     :", jumlah_produk, file=a)
                    print("------------------------------------", file=a)
                    print("  Total      : Rp", totalan, file=a)
                    print("------------------------------------", file=a)
                    print("  Sisa Saldo : Rp", user['e-Money'][cari], file=a) 
                    print("===================================", file=a)
            
            elif user['e-Money'][cari] < totalan:
                print("Saldo e-Money anda kurang")
                while True :
                    tny = input("Apakah anda ingin top up saldo e-Money? (y/t) : ")
                    if tny == "y":
                        emoney()
                        break

                    elif tny == "t":
                        print("---------------------------------------------")
                        print("          SALDO ANDA TIDAK MENCUKUPI ")
                        print("---------------------------------------------\n")
                        print("------------- TRANSAKSI GAGAL --------------")
                        break
                    else :
                        print("\n> INPUT TIDAK SESUAI")
            
            elif user["e-Money"][cari] == totalan :
                produk.get("Stok Produk")[cari_produk] = produk["Stok Produk"][cari_produk] - jumlah_produk
                user.get("e-Money")[cari] = user["e-Money"][cari]- totalan
                penyimpanan()
                datacust()
                with open("transaksi.txt", "a") as a:
                    print("\n----------TRANSAKSI ANDA BERHASIL-----------")

                    print("\n===================================", file=a)
                    print("              AHA MART             ", file=a)
                    print("===================================", file=a)
                    print("  Barang     :", nama_barang, file=a)
                    print("  Jumlah     :", jumlah_produk, file=a)
                    print("------------------------------------", file=a)
                    print("  Total      : Rp", totalan, file=a)
                    print("------------------------------------", file=a)
                    print("  Sisa Saldo : Rp", user['e-Money'][cari], file=a) 
                    print("===================================", file=a)

        while True : 
            lagi = input(">> Apakah anda ingin kembali ke menu home (y/t) : ")
            if lagi == "y" :
                os.system("cls")
                return
                
            elif lagi == "t":
                print("BELI LAGI: ")
                
            else :
                print("> TOLONG PERHATIKAN INPUT")
                

def cek_saldo():
    while True :
        print("\n-----------------------------------------")
        print("            CEK SALDO E-MONEY            ")
        print("-----------------------------------------")
        print( f'   Saldo e-Money anda adalah Rp.{user.get("e-Money")[cari]}   ')
        print("-----------------------------------------\n")
        kembali = input(">> Apakah anda ingin kembali ke menu sebelumnya? (y/t) : ")
        if kembali == "y":
            os.system("cls")
            return
            
        elif kembali == "t":
            print("SALDO ANDA: ")
            
        else :
            print("> PILIHAN TIDAK TERSEDIA")
            

    
#main program
def main():
    while True:
        try :
            print("""
=====================================
          SELAMAT DATANG DI 
              AHA MART
=====================================""")
            tampilan_awal()
            pilihan = input("Masukkan pilihan (1/2/3): ")
            os.system("cls")
            
            if pilihan == "1":
                login_admin()
                
            elif pilihan == "2" :
                menu_pembeli()
                
            elif pilihan == "3":
                
                print("""
    =======================================
            PROGRAM TELAH SELESAI
        Terima kasih! dan sampai jumpa :)
    =======================================
        """)
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")
    
        except KeyboardInterrupt :
                print("INPUT INVALID")

main()