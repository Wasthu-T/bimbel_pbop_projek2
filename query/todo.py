from prettytable import PrettyTable
from email_validator import validate_email, EmailNotValidError
from datetime import datetime
from query.aktor import Siswa, Guru, Pegawai
import locale


# set bahasa waktu lokal indonesia
locale.setlocale(locale.LC_TIME, 'id_ID')

class transaksi :
    def __init__(self, db):
        self.db = db

    def jenis_pembayaran(self):
        while True :
            print("\n=== Jenis Pembayaran ===")
            print("1. Cash")
            print("2. Transfer")
            pilih = int(input("Pilih Jenis Pembayaran\t: "))
            if pilih == 1 :
                return "Cash"
            elif pilih == 2 :
                return "Transfer"
            else :
                print("pilihan tidak tersedia harap pilih yang benar")

    def insert_transaksi(self):
        print("===== Input Transaksi =====")
        Id_pegawai = int(input("Masukan ID Pegawai\t: "))
        Id_siswa = int(input("Masukan ID Siswa\t: "))
        Id_paket_belajar = int(input("Masukan ID Paket Belajar\t: "))

        Jenis_pembayaran = self.jenis_pembayaran()
        Bayar = int(input("Masukan Nominal Bayar\t: "))
        Kembalian = int(input("Masukan Jumlah Kembalian\t: "))
        date_str = input("Masukkan tanggal transaksi (format: YYYY-MM-DD)\t: ") 
        date = datetime.strptime(date_str, "%Y-%m-%d") 
        Tgl_transaksi = date.date()
        x = PrettyTable()
        x.field_names = ["Id_pegawai", "Id_siswa","Id_paket_belajar", "Jenis_pembayaran", "Bayar", "Kembalian", "Tgl_transaksi"]
        x.add_row([Id_pegawai, Id_siswa, Id_paket_belajar, Jenis_pembayaran, Bayar, Kembalian, Tgl_transaksi])
        print(x)
        yakin = str(input("Yakin ingin meng-input y/n? "))
        if (yakin == 'y') :
            quary = """INSERT INTO transaksi(Id_pegawai, Id_siswa, Id_paket_belajar, Jenis_pembayaran, Bayar, Kembalian, Tgl_transaksi) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            data = (Id_pegawai, Id_siswa, Id_paket_belajar, Jenis_pembayaran, Bayar, Kembalian, Tgl_transaksi)

            self.db.insertValue(quary,data)
            print("=== Anda Berhasil Meng-input transaksi ===")
        else : 
            print("=== Anda Gagal Meng-input transaksi ===")

    def read_transaksi(self):
        print("=== Read Transaksi ===")
        query = """SELECT * FROM transaksi"""
        self.db.selectValuepretty(query, data=None)

class jadwal : 
    pass

class jadwal_pelayanan :
    pass

class ruangan :
    def __init__(self, db):
        self.db = db

    def kondisi_ruangan(self):
        while True :
            print("\n=== Kondisi Ruangan ===")
            print("1. Layak")
            print("2. Tidak layak")
            pilih = int(input("Pilih Kondisi Ruangan\t: "))
            if pilih == 1 :
                return "Layak"
            elif pilih == 2 :
                return "Tidak Layak"
            else :
                print("pilihan tidak tersedia harap pilih yang benar")

    def insert_ruangan(self):
        print("===== Input Ruangan =====")
        Kondisi_ruangan = self.kondisi_ruangan()
        Kapasitas_kursi = int(input("Masukan Kapasitas Kursi\t: "))
        x = PrettyTable()
        x.field_names = ["Kondisi_ruangan", "Kapasitas_kursi"]
        x.add_row([Kondisi_ruangan, Kapasitas_kursi])
        print(x)
        yakin = str(input("Yakin ingin meng-input y/n? "))
        if (yakin == 'y') :
            quary = """INSERT INTO ruangan(Kondisi_ruangan, Kapasitas_kursi) VALUES (%s, %s)"""
            data = (Kondisi_ruangan. Kapasitas_kursi)

            self.db.insertValue(quary,data)
            print("=== Anda Berhasil Meng-input Data Ruangan ===")
        else : 
            print("=== Anda Gagal Meng-input Data Ruangan ===")

    def edit_ruangan(self, result, Id_ruangan) :
        Kondisi_ruangan = result[0][1]
        Kapasitas_kursi = result[0][2]
        while True :
            print("=== Edit Value ===")
            print("1. Kondisi Ruangan")
            print("2. Kapasitas Kursi")
            pilih = int(input("Data yang ingin diubah : "))
            if pilih == 1:
                Kondisi_ruangan = self.kondisi_ruangan()
            elif pilih == 2:
                Kapasitas_kursi = int(input("Masukan Kapasitas Kursi\t: "))
            else : 
                print("Pilihan tidak tersedia")
            lanjut = str(input("Ganti data lain (y/n)? "))
            if lanjut == 'y' :
                continue
            else :
                break
        query = """UPDATE ruangan SET `Kondisi_ruangan`= %s, `Kapasitas_kursi`=%s WHERE `Id_ruangan` = %s"""
        data = (Kondisi_ruangan, Kapasitas_kursi)
        self.db.insertValue(query, data)

    def update_ruangan(self) :
        print("=== Update Ruangan ===")
        Id_ruangan = int(input("Masukkan ID Ruangan yang akan diupdate: "))
        query = """SELECT * FROM ruangan WHERE Id_ruangan = %s"""
        data = (Id_ruangan,)
        self.db.selectValuepretty(query, data)
        result = self.db.selectValue(query, data)
        test = str(input("Apa data ingin diupdate (y/n)? "))
        if test.lower() == 'y' :
            self.edit_ruangan(result, Id_ruangan)
            print("=== Anda Berhasil Meng-update Data Ruangan ===")
        else :
            print("=== Anda Gagal Meng-update Data Ruangan ===")

    def delete_ruangan(self):
        print("=== Delete Ruangan ===")
        Id_ruangan = int(input("Masukkan ID Ruangan yang akan dihapus: "))
        query = """SELECT * FROM ruangan WHERE Id_ruangan = %s"""
        data = (Id_ruangan,)
        self.db.selectValuepretty(query, data)
        test = str(input("Apa data ingin dihapus (y/n)? "))
        if test.lower() == 'y' :
            query = """DELETE FROM ruangan WHERE Id_ruangan = %s """
            data = (Id_ruangan,)
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Menghapus Data Ruangan ===")
            
        else :
            print("=== Anda Gagal Menghapus Data Ruangan ===")

    def read_ruangan(self) :
        print("=== Read Ruangan ===")
        query = """SELECT * FROM ruangan"""
        self.db.selectValuepretty(query, data=None)
        print("=== Anda Berhasil Menampilkan Data Ruangan ===")

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
