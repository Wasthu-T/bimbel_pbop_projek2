from prettytable import PrettyTable
from email_validator import validate_email, EmailNotValidError
from datetime import datetime
from query.aktor import Siswa, Guru, Pegawai
import locale


# set bahasa waktu lokal indonesia
locale.setlocale(locale.LC_TIME, 'id_ID')

class transaksi :
    pass

class jadwal : 
    pass

class jadwal_pelayanan :
    pass

class ruangan :
    pass

class paket_belajar :
    def __init__(self, db):
        self.db = db

    def kelas(self) :
        while True :
            print("\n=== Jenjang Pendidikan ===")
            print("1. SD")
            print("2. SMP")
            print("3. SMA")
            pilih = int(input("Pilih Jenjang Pendidikan\t: "))
            if pilih == 1 :
                return "SD"
            elif pilih == 2 :
                return "SMP"
            elif pilih == 3 :
                return "SMA"
            else :
                print("pilihan tidak tersedia harap pilih yang benar")

    def kategori(self) :
        while True :
            print("\n=== Kategori Paket Belajar ===")
            print("1. Reguler")
            print("2. Premium")
            pilih = int(input("Pilih Kategori Paket Belajar\t: "))
            if pilih == 1 :
                return "Reguler"
            elif pilih == 2 :
                return "Premium"
            else :
                print("pilihan tidak tersedia harap pilih yang benar")

    def insert_paket_belajar(self):
        print("===== Input Paket Belajar =====")
        Kategori = self.kategori()
        Kelas = self.kelas()
        Biaya = int(input("Masukan Biaya Paket Belajar\t:"))
        x = PrettyTable()
        x.field_names = ["Kategori", "Kelas", "Biaya"]
        x.add_row([Kategori, Kelas, Biaya])
        print(x)
        yakin = str(input("Yakin ingin mendaftar y/n? "))
        if (yakin == 'y') :
            quary = """INSERT INTO paket_belajar(Kategori, Kelas, Biaya) VALUES (%s, %s, %s)"""
            data = (Kategori, Kelas, Biaya)

            self.db.insertValue(quary,data)
            print("=== Anda Berhasil Meng-input Data Paket Belajar ===")
        else : 
            print("=== Anda Gagal Meng-input Data Paket Belajar===")

    def edit_paket_belajar(self, result, Id_paket_belajar) :
        Kategori = result[0][1]
        Kelas = result[0][2]
        Biaya = result[0][3]
        while True :
            print("=== Edit Value ===")
            print("1. Kategori")
            print("2. Kelas")
            print("3. Biaya")
            pilih = int(input("Data yang ingin diubah : "))
            if pilih == 1:
                Kategori = self.kategori()
            elif pilih == 2:
                Kelas = self.kelas()
            elif pilih == 3:
                Biaya = int(input("Masukan Biaya Paket Belajar\t:"))
            else : 
                print("Pilihan tidak tersedia")
            lanjut = str(input("Ganti data lain (y/n)? "))
            if lanjut == 'y' :
                continue
            else :
                break
        query = """UPDATE paket_belajar SET `Kategori`= %s, `Kelas`= %s , `Biaya`= %s WHERE `Id_paket_belajar` = %s"""
        data = (Kategori, Kelas, Biaya, Id_paket_belajar)
        self.db.insertValue(query, data)

    def update_paket_belajar(self):
        print("=== Update Paket Belajar ===")
        Id_paket_belajar = int(input("Masukkan ID Paket Belajar yang akan diupdate: "))
        query = """SELECT * FROM paket_belajar WHERE Id_paket_belajar = %s"""
        data = (Id_paket_belajar,)
        self.db.selectValuepretty(query, data)
        result = self.db.selectValue(query, data)


        test = str(input("Apa data ingin diupdate (y/n)? "))
        if test.lower() == 'y' :
            self.edit_paket_belajar(result, Id_paket_belajar)
            print("=== Anda Berhasil Meng-update Data Paket Belajar ===")
        else :
            print("=== Anda Gagal Meng-update Data Paket Belajar ===")

    def delete_paket_belajar(self):
        print("=== Delete Paket Belajar ===")
        Id_paket_belajar = int(input("Masukkan ID Paket Belajar yang akan dihapus: "))
        query = """SELECT * FROM paket_belajar WHERE Id_paket_belajar = %s"""
        data = (Id_paket_belajar,)
        self.db.selectValuepretty(query, data)
        test = str(input("Apa data ingin dihapus (y/n)? "))
        if test.lower() == 'y' :
            query = """DELETE FROM paket_belajar WHERE Id_paket_belajar = %s """
            data = (Id_paket_belajar,)
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Menghapus Data Paket Belajar ===")
            
        else :
            print("=== Anda Gagal Menghapus Data Paket Belajar ===")

    def read_paket_belajar(self):
        print("=== Read Paket Belajar ===")
        query = """SELECT * FROM paket_belajar"""
        self.db.selectValuepretty(query, data=None)
