from prettytable import PrettyTable
from email_validator import validate_email, EmailNotValidError
from datetime import datetime
from query.aktor import Siswa, Guru, Pegawai
import locale

# set bahasa waktu lokal indonesia
locale.setlocale(locale.LC_TIME, 'id_ID')

class absen_pegawai :
    def __init__(self, db):
        self.db = db

    def absen_datang(self, Id_pegawai) :
        tanggal = datetime.now().date()
        jam_datang = datetime.now().time()
        Jam_selesai = None
        Absen = "Alpha"
        query = """INSERT INTO `absen_pegawai`(`Id_pegawai`, `Tanggal`, `Jam_datang`, `Jam_selesai`, `Absen`) 
                VALUES 
                (%s,%s,%s,%s,%s)"""
        data = (Id_pegawai, tanggal, jam_datang, Jam_selesai, Absen)
        self.db.insertValue(query,data)
    

    def absen_pulang(self, Id_pegawai) :
        tanggal = datetime.now().date()
        Jam_selesai = datetime.now().time()
        Absen = "Hadir"
        query = """
            UPDATE `absen_pegawai` 
            SET
            `Jam_selesai` = %s,
            `Absen` = %s 
            WHERE `Tanggal` = %s AND `Id_pegawai` = %s
        """
        data = (Jam_selesai, Absen, tanggal, Id_pegawai)
        self.db.insertValue(query, data)
    
    def absen(self) :
        while True:
            print("\n=== Izin ===")
            print("1. Sakit")
            print("2. Izin")
            pilih = int(input("Pilih Absensi\t: "))
            if pilih == 1:
                return "Sakit"
            elif pilih == 2:
                return "Izin"
            else:
                print("pilihan tidak tersedia harap pilih yang benar")
    
    def izin(self,Id_pegawai) :
        tanggal = datetime.now().date()
        jam_datang = None
        Jam_selesai = None
        Absen = self.absen()
        query = """INSERT INTO `absen_pegawai`(`Id_pegawai`, `Tanggal`, `Jam_datang`, `Jam_selesai`, `Absen`) 
                VALUES 
                (%s,%s,%s,%s,%s)"""
        data = (Id_pegawai, tanggal, jam_datang, Jam_selesai, Absen)
        self.db.insertValue(query,data)

class absen_guru:
    def absen(self):
        while True:
            print("\n=== Absensi Guru ===")
            print("1. Hadir")
            print("2. Sakit")
            print("3. Izin")
            print("4. Alpha")
            pilih = int(input("Pilih Absensi\t: "))
            if pilih == 1:
                return "Hadir"
            elif pilih == 2:
                return "Sakit"
            elif pilih == 3:
                return "Izin"
            elif pilih == 4:
                return "Alpha"
            else:
                print("pilihan tidak tersedia harap pilih yang benar")

    def insert_absen_guru(self, db):
        print("=== Input Absen Guru ===")
        Id_guru = int(input("Masukkan ID Guru\t: "))
        date_str = input("Masukkan tanggal absensi (format: YYYY-MM-DD)\t: ")
        date = datetime.strptime(date_str, "%Y-%m-%d")
        Tanggal = date.date()
        Jam_datang = input("Masukkan Jam Datang (format: HH:MM:SS)\t: ")
        Jam_selesai = input("Masukkan Jam Selesai (format: HH:MM:SS)\t: ")
        
        Absen = self.absen()

        x = PrettyTable()
        x.field_names = ["Id_guru", "Tanggal", "Jam_datang", "Jam_selesai", "Absen"]
        x.add_row([Id_guru, Tanggal, Jam_datang, Jam_selesai, Absen])
        print(x)
        
        yakin = str(input("Yakin ingin meng-input y/n? "))
        
        if yakin == 'y':
            query = """INSERT INTO absen_guru(Id_guru, Tanggal, Jam_datang, Jam_selesai, Absen) 
                       VALUES (%s, %s, %s, %s, %s)"""
            data = (Id_guru, Tanggal, Jam_datang, Jam_selesai, Absen)
            self.db.insertValue(query,data)
            print("=== Anda Berhasil Meng-input Absen Guru ===")
        else:
            print("=== Anda Gagal Meng-input Absen Guru ===")

    def update_absen_guru(self):
        print("=== Update Absen Guru ===")
        Id_absen_guru = int(input("Masukkan ID Absen Guru yang akan diupdate: "))
        Absen = self.absen()
        Tanggal = input("Masukkan tanggal (format: YYYY-MM-DD): ")
        Jam_datang = input("Masukkan jam datang (format: HH:MM:SS): ")
        Jam_selesai = input("Masukkan jam selesai (format: HH:MM:SS): ")
        
        yakin = str(input("Yakin ingin meng-input y/n? "))
        
        if yakin == 'y':
            query = """UPDATE absen_guru SET `Absen` = %s, `Tanggal` = %s, `Jam_datang` = %s, `Jam_selesai` = %s WHERE `Id_absen_guru` = %s"""
            data = (Absen, Tanggal, Jam_datang, Jam_selesai, Id_absen_guru)
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Meng-update Absensi Guru ===")
        else:
            print("=== Gagal update data ===")

    def read_absen_guru(self):
        print("=== Read Absen Guru ===")
        query = """SELECT * FROM absen_guru"""
        self.db.selectValuepretty(query, data=None)
        print("=== Anda Berhasil Menampilkan Data Absensi Guru ===")

    def delete_absen_guru(self):
        print("=== Delete Absen Guru ===")
        Id_guru = int(input("Masukkan ID Guru yang akan dihapus: "))
        query = """SELECT * FROM absen_guru WHERE Id_guru = %s"""
        data = (Id_guru,)
        self.db.selectValuepretty(query, data)
        
        test = str(input("Apa data ingin dihapus (y/n)? "))
        if test.lower() == 'y':
            query = """DELETE FROM absen_guru WHERE Id_guru = %s"""
            data = (Id_guru,)
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Menghapus Absensi Guru ===")
        else:
            print("=== Anda Gagal Menghapus Absensi Guru ===")

class absen_siswa :
    def absen(self):
        while True :
            print("\n=== Absensi ===")
            print("1. Hadir")
            print("2. Sakit")
            print("3. Izin")
            print("4. Alpha")
            pilih = int(input("Pilih Absensi\t: "))
            if pilih == 1 :
                return "Hadir"
            elif pilih == 2 :
                return "Sakit"
            elif pilih == 3 :
                return "Izin"
            elif pilih == 4 :
                return "Alpha"
            else :
                print("pilihan tidak tersedia harap pilih yang benar")

    def insert_absen_siswa(self):
        print("=== Input Absen Siswa ===")
        Id_guru = int(input("Masukan ID Guru\t: "))

        Id_siswa = int(input("Masukkan ID Siswa\t: "))
        Id_jadwal = int(input("Masukkan ID Jadwal\t: "))
        date_str = input("Masukkan tanggal absensi (format: YYYY-MM-DD)\t: ") 
        date = datetime.strptime(date_str, "%Y-%m-%d") 
        Tanggal = date.date()
        Absen = self.absen()
        x = PrettyTable()
        x.field_names = ["Id_guru", "Id_siswa", "Id_jadwal", "Tanggal", "Absen"]
        x.add_row([Id_guru, Id_siswa, Id_jadwal, Tanggal, Absen])
        print(x)
        yakin = str(input("Yakin ingin meng-input y/n? "))
        if (yakin == 'y') :
            quary = """INSERT INTO absen_siswa(Id_guru, Id_siswa, Id_jadwal, Tanggal, Absen) VALUES (%s, %s, %s, %s, %s)"""
            data = (Id_guru, Id_siswa, Id_jadwal, Tanggal, Absen)

            self.db.insertValue(quary,data)
            print("=== Anda Berhasil Meng-input Absen Siswa ===")
        else : 
            print("=== Anda Gagal Meng-input Absen Siswa ===")

    def edit_absen_siswa(self, result, Id_absen_siswa) :
        Absen = result[0][1]
        while True :
            print("=== Edit Value ===")
            print("1. Absen")
            pilih = int(input("Data yang ingin diubah : "))
            if pilih == 1:
                Absen = self.absen()
            else : 
                print("Pilihan tidak tersedia")
            lanjut = str(input("Ganti data lain (y/n)? "))
            if lanjut == 'y' :
                continue
            else :
                break
        query = """UPDATE absen_siswa SET `Absen`= %s WHERE `Id_absen_siswa` = %s"""
        data = (Absen)
        self.db.insertValue(query, data)

    def update_absen_siswa(self) :
        print("=== Update Absen Siswa ===")
        Id_absen_siswa = int(input("Masukkan ID Absen Siswa yang akan diupdate: "))
        query = """SELECT * FROM absen_siswa WHERE Id_absen_siswa = %s"""
        data = (Id_absen_siswa,)
        self.db.selectValuepretty(query, data)
        result = self.db.selectValue(query, data)
        test = str(input("Apa data ingin diupdate (y/n)? "))
        if test.lower() == 'y' :
            self.edit_absen_siswa(result, Id_absen_siswa)
            print("=== Anda Berhasil Meng-update Absensi Siswa ===")
        else :
            print("=== Anda Gagal Meng-update Absensi Siswa ===")

    def delete_absen_siswa(self):
        print("=== Delete Absen Siswa ===")
        Id_absen_siswa = int(input("Masukkan ID Absen Siswa yang akan dihapus: "))
        query = """SELECT * FROM absen_siswa WHERE Id_absen_siswa = %s"""
        data = (Id_absen_siswa,)
        self.db.selectValuepretty(query, data)
        test = str(input("Apa data ingin dihapus (y/n)? "))
        if test.lower() == 'y' :
            query = """DELETE FROM absen_siswa WHERE Id_absen_siswa = %s """
            data = (Id_absen_siswa,)
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Menghapus Absensi Siswa ===")
            
        else :
            print("=== Anda Gagal Menghapus Absensi Siswa ===")

    def read_absen_siswa(self) :
        print("=== Read Absen Siswa ===")
        query = """SELECT * FROM absen_siswa"""
        self.db.selectValuepretty(query, data=None)
        print("=== Anda Berhasil Menampilkan Data Absensi Siswa ===")
