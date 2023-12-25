from prettytable import PrettyTable
from email_validator import validate_email, EmailNotValidError
from datetime import datetime
from query.aktor import Siswa, Guru, Pegawai
import locale

# set bahasa waktu lokal indonesia
locale.setlocale(locale.LC_TIME, 'id_ID')

class absen_pegawai :
    pass

class absen_guru :
    pass

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
