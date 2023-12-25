from prettytable import PrettyTable
from email_validator import validate_email, EmailNotValidError
from datetime import datetime
import locale
# set bahasa waktu lokal indonesia
locale.setlocale(locale.LC_TIME, 'id_ID')

class Siswa:
    def __init__(self, db):
        self.db = db
    
    def check_email(self):
        run = True
        while run :
            try:
                Email = str(input("Masukan Email\t\t: "))
                validate_email(Email)
                return Email
            except EmailNotValidError as e:
                print(str(e))

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

    def jenis_kelamin(self) :
        while True :
            print("\n=== Jenis Kelamin ===")
            print("1. Laki-laki")
            print("2. Perempuan")
            pilih = int(input("Pilih Jenis Kelamin\t: "))
            if pilih == 1 :
                return "Laki-laki"
            elif pilih == 2 :
                return "Perempuan"
            else :
                print("pilihan tidak tersedia harap pilih yang benar")

    def insert_pelajar(self):
        print("===== Input Pelajar =====")
        Nama = str(input("Masukan Nama\t: "))
        Email = self.check_email()
        Nomor = "0" + str(int(input("Masukan Nomor\t: ")))

        Jenjang_pendidikan = self.kelas()
        Jenis_kelamin = self.jenis_kelamin()
        Password = str(input("Masukan Password: "))
        x = PrettyTable()
        x.field_names = ["Nama", "Email", "Nomor", "Jenjang_pendidikan", "Jenis_kelamin", "Password"]
        x.add_row([Nama, Email, Nomor, Jenjang_pendidikan, Jenis_kelamin, Password])
        print(x)
        yakin = str(input("Yakin ingin mendaftar y/n? "))
        if (yakin == 'y') :
            quary = """INSERT INTO pelajar(Nama, Email, Nomor, Jenjang_pendidikan, Jenis_kelamin, Password) VALUES (%s, %s, %s, %s, %s, %s)"""
            data = (Nama, Email, Nomor, Jenjang_pendidikan, Jenis_kelamin, Password)

            self.db.insertValue(quary,data)
            print("=== Anda Berhasil Mendaftar Sebagai Pelajar ===")
        else : 
            print("=== Anda Gagal Mendaftar Sebagai Pelajar ===")

    def update_pelajar(self):
        print("=== Update Pelajar ===")
        Id_pelajar = int(input("Masukkan ID Pelajar yang akan diupdate: "))
        query = """SELECT * FROM pelajar WHERE Id_pelajar = %s"""
        data = (Id_pelajar,)
        self.db.selectValuepretty(query, data)
        result = self.db.selectValue(query, data)


        test = str(input("Apa data ingin diupdate (y/n)? "))
        if test.lower() == 'y' :
            self.edit(result, Id_pelajar)
            print("=== Anda Berhasil Meng-update Data Pelajar ===")
        else :
            print("=== Anda Gagal Meng-update Data Pelajar ===")

    def delete_pelajar(self):
        print("=== Delete Pelajar ===")
        Id_pelajar = int(input("Masukkan ID Pelajar yang akan dihapus: "))
        query = """SELECT * FROM pelajar WHERE Id_pelajar = %s"""
        data = (Id_pelajar,)
        self.db.selectValuepretty(query, data)
        test = str(input("Apa data ingin dihapus (y/n)? "))
        if test.lower() == 'y' :
            query = """DELETE FROM pelajar WHERE Id_pelajar = %s """
            data = (Id_pelajar,)
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Menghapus Data Pelajar ===")
            
        else :
            print("=== Anda Gagal Menghapus Data Pelajar ===")

    def read_pelajar(self):
        print("=== Read Pelajar ===")
        query = """SELECT * FROM pelajar"""
        self.db.selectValuepretty(query, data=None)

class Guru:
    def __init__(self, db):
        self.db = db

    def check_email(self):
        run = True
        while run :
            try:
                Email = str(input("Masukan Email\t\t: "))
                validate_email(Email)
                return Email
            except EmailNotValidError as e:
                print(str(e))

    def umur(self) :
        umur = int(input("Masukan Usia\t\t: "))
        if umur >= 18 :
            return umur
        else :
            print("Usia anda dibawah umur maka dilarang mengajar di bimbel ini")
            return None
        
    def jenis_kelamin(self) :
        while True :
            print("\n=== Jenis Kelamin ===")
            print("1. Laki-laki")
            print("2. Perempuan")
            pilih = int(input("Pilih Jenis Kelamin\t: "))
            if pilih == 1 :
                return "Laki-laki"
            elif pilih == 2 :
                return "Perempuan"
            else :
                print("pilihan tidak tersedia harap pilih yang benar")

    def bidang_mapel(self):
        while True :
            print("\n=== Bidang Mapel ===")
            print("1. Matematika")
            print("2. Bahasa Indonesia")
            print("3. Bahasa Inggris")
            print("4. Ilmu Pengetahuan Alam")
            print("5. Fisika")
            print("6. Kimia")
            print("7. Biologi")
            print("8. Geografi")
            print("9. Ekonomi")
            print("10. Sosiologi")
            print("11. Sejarah")
            print("12. Tes Potensi Skolastik")
            pilih = int(input("Pilih Bidang Mapel\t: "))
            if pilih == 1 :
                return "Matematika"
            elif pilih == 2 :
                return "Bahasa Indonesia"
            elif pilih == 3 :
                return "Bahasa Inggris"
            elif pilih == 4 :
                return "Ilmu Pengetahuan Alam"
            elif pilih == 5 :
                return "Fisika"
            elif pilih == 6 :
                return "Kimia"
            elif pilih == 7 :
                return "Biologi"
            elif pilih == 8 :
                return "Geografi"
            elif pilih == 9 :
                return "Ekonomi"
            elif pilih == 10 :
                return "Sosiologi"
            elif pilih == 11 :
                return "Sejarah"
            elif pilih == 12 :
                return "Tes Potensi Skolastik"
            else :
                print("pilihan tidak tersedia harap pilih yang benar")


    def insert_pengajar(self):
        print("===== Input Pengajar =====")
        Nama = str(input("Masukan Nama\t: "))
        Email = self.check_email()
        Nomor = "0" + str(int(input("Masukan Nomor\t: ")))

        Usia = self.umur()
        Jenis_kelamin = self.jenis_kelamin()
        Password = str(input("Masukan Password: "))
        x = PrettyTable()
        x.field_names = ["Nama", "Email", "Nomor", "Usia", "Jenis_kelamin", "Password"]
        x.add_row([Nama, Email, Nomor, Usia, Jenis_kelamin, Password])
        print(x)
        yakin = str(input("Yakin ingin mendaftar y/n? "))
        if (yakin == 'y') and (Usia is not None):
            quary = """INSERT INTO pengajar(Nama, Email, Nomor, Usia, Jenis_kelamin, Password) VALUES (%s, %s, %s, %s, %s, %s)"""
            data = (Nama, Email, Nomor, Usia, Jenis_kelamin, Password)

            self.db.insertValue(quary,data)
            print("=== Anda Berhasil Mendaftar Sebagai Pengajar ===")
        else : 
            print("=== Anda Gagal Mendaftar Sebagai Pengajar ===")

    def update_pengajar(self):
        print("===== Update Pengajar =====")
        Id_pengajar = int(input("Masukkan ID Pengajar yang akan diupdate: "))
        query = """SELECT * FROM pengajar WHERE Id_pengajar = %s"""
        data = (Id_pengajar,)
        self.db.selectValuepretty(query, data)
        result = self.db.selectValue(query, data)


        test = str(input("Apa data ingin diupdate (y/n)? "))
        if test.lower() == 'y' :
            self.edit(result, Id_pengajar)
            print("=== Anda Berhasil Meng-update Data Pengajar ===")
        else :
            print("=== Anda Gagal Meng-update Data Pengajar ===")

    def delete_pengajar(self):
        print("===== Delete Pengajar =====")
        Id_pengajar = int(input("Masukkan ID Pengajar yang akan dihapus: "))
        query = """SELECT * FROM pengajar WHERE Id_pengajar = %s"""
        data = (Id_pengajar,)
        self.db.selectValuepretty(query, data)
        test = str(input("Apa data ingin dihapus (y/n)? "))
        if test.lower() == 'y' :
            query = """DELETE FROM pengajar WHERE Id_pengajar = %s """
            data = (Id_pengajar,)
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Menghapus Data Pengajar ===")
            
        else :
            print("=== Anda Gagal Menghapus Data Pengajar ===")

    def read_pengajar(self):
        print("===== Read Pengajar =====")
        query = """SELECT * FROM pengajar"""
        self.db.selectValuepretty(query, data=None)

class Pegawai:
    def __init__(self, db):
        self.db = db

    def jenis_kelamin(self) :
        while True :
            print("\n=== Jenis Kelamin ===")
            print("1. Laki-laki")
            print("2. Perempuan")
            pilih = int(input("Pilih Jenis Kelamin\t: "))
            if pilih == 1 :
                return "Laki-laki"
            elif pilih == 2 :
                return "Perempuan"
            else :
                print("pilihan tidak tersedia harap pilih yang benar")

    def umur(self) :
        umur = int(input("Masukan Usia\t\t: "))
        if umur >= 18 :
            return umur
        else :
            print("Usia anda dibawah umur")
            return None
        
    def check_email(self):
        run = True
        while run :
            try:
                Email = str(input("Masukan Email\t: "))
                validate_email(Email)
                return Email
            except EmailNotValidError as e:
                print(str(e)) 

    def insert_admin(self):
        print("===== Input Admin =====")
        Nama = str(input("Masukan Nama\t: "))
        Email = self.check_email()
        Nomor = "0" + str(int(input("Masukan Nomor\t: ")))

        Jenis_kelamin = self.jenis_kelamin()
        Usia = self.umur()
        x = PrettyTable()
        x.field_names = ["Nama", "Email", "Nomor", "Usia", "Jenis_kelamin"]
        x.add_row([Nama, Email, Nomor, Usia, Jenis_kelamin])
        print(x)
        yakin = str(input("Yakin ingin menambah data y/n? "))
        if (yakin == 'y') and (Usia is not None) :
            quary = """INSERT INTO admin(Nama, Email, Nomor, Usia, Jenis_kelamin) VALUES (%s, %s, %s, %s, %s)"""
            data = (Nama, Email, Nomor, Usia, Jenis_kelamin)

            self.db.insertValue(quary,data)
            print("=== Anda Berhasil Menambahkan Data Admin ===")
        else : 
            print("=== Anda Gagal Menambahkan Data Admin ===")

    def edit(self, result, Id_admin) :
        Nama = result[0][1]
        Email = result[0][2]
        Nomor = result[0][3]
        Usia = result[0][4]
        while True : 
            print("=== Edit value ===")
            print("1. Nama")
            print("2. Email")
            print("3. Nomor")
            print("4. Usia")
            pilih = int(input("Data yang ingin diubah : "))
            if pilih == 1 :
                Nama = str(input("Masukan Nama\t: "))
            elif pilih == 2 :
                Email = self.check_email()
            elif pilih == 3 :
                Nomor = "0" + str(int(input("Masukan Nomor\t: ")))
            elif pilih == 4 :
                Usia = self.umur()
                if int(Usia) <= int(result[0][4]) :
                    print("Usia kamu turun?")
                    Usia = result[0][4]
                if Usia is None :
                    Usia = result[0][4]
            else : 
                print("Pilihan tidak tersedia")
            lanjut = str(input("Ganti data lain (y/n)? "))
            if lanjut == 'y' :
                continue
            else :
                break
        query = """UPDATE admin SET `Nama`= %s, `Email`= %s, `Nomor`= %s, `Usia`= %s  WHERE Id_admin = %s"""
        data = (Nama, Email, Nomor, Usia, Id_admin)
        self.db.insertValue(query, data)

    def update_admin(self):
        print("===== Update Admin =====")
        Id_admin = int(input("Masukkan ID Admin yang akan diupdate: "))
        query = """SELECT * FROM admin WHERE Id_admin = %s"""
        data = (Id_admin,)
        self.db.selectValuepretty(query, data)
        result = self.db.selectValue(query, data)


        test = str(input("Apa data ingin diupdate (y/n)? "))
        if test.lower() == 'y' :
            self.edit(result, Id_admin)
            print("=== Anda Berhasil Meng-update Data Admin ===")
        else :
            print("=== Anda Gagal Meng-update Data Admin ===")


    def delete_admin(self):
        print("===== Delete Admin =====")
        Id_admin = int(input("Masukkan ID Admin yang akan dihapus: "))
        query = """SELECT * FROM admin WHERE Id_admin = %s"""
        data = (Id_admin,)
        self.db.selectValuepretty(query, data)
        test = str(input("Apa data ingin dihapus (y/n)? "))
        if test.lower() == 'y' :
            query = """DELETE FROM admin WHERE Id_admin = %s """
            data = (Id_admin,)
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Menghapus Data Admin ===")
            
        else :
            print("=== Anda Gagal Menghapus Data Admin ===")


    def read_admin(self):
        print("===== Read Admin =====")
        query = """SELECT * FROM admin"""
        self.db.selectValuepretty(query, data=None)