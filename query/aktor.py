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

    def insert_siswa(self):
        print("===== Input Siswa =====")
        Id_paket_belajar = int(input("Masukan ID Paket Belajar\t: "))

        Nama = str(input("Masukan Nama\t: "))
        Password = str(input("Masukan Password\t: "))
        Email = self.check_email()
        Nomor = "0" + str(int(input("Masukan Nomor\t: ")))
        Kelas = self.kelas()
        Jenis_kelamin = self.jenis_kelamin()
        Alamat = str(input("Masukkan Alamat\t: "))
        Tagihan = str(input("Masukan Jumlah Tagihan\t: "))
        x = PrettyTable()
        x.field_names = ["Id_paket_belajar","Nama", "Password", "Email", "Nomor", "Kelas", "Jenis_kelamin", "Alamat", "Tagihan"]
        x.add_row([Id_paket_belajar, Nama, Password, Email, Nomor, Kelas, Jenis_kelamin, Alamat, Tagihan])
        print(x)
        yakin = str(input("Yakin ingin mendaftar y/n? "))
        if (yakin == 'y') :
            quary = """INSERT INTO pelajar(Id_paket_belajar, Nama, Password, Email, Nomor, Kelas, Jenis_kelamin, Alamat, Tagihan) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            data = (Id_paket_belajar, Nama, Password, Email, Nomor, Kelas, Jenis_kelamin, Alamat, Tagihan)

            self.db.insertValue(quary,data)
            print("=== Anda Berhasil Mendaftar Sebagai Siswa ===")
        else : 
            print("=== Anda Gagal Mendaftar Sebagai Siswa ===")

    def edit_siswa(self, result, Id_siswa) :
        Nama = result[0][1]
        Password = result[0][2]
        Email = result[0][3]
        Nomor = result[0][4]
        Alamat = result[0][5]
        while True :
            print("=== Edit Value ===")
            print("1. Nama")
            print("2. Password")
            print("3. Email")
            print("4. Nomor")
            print("5. Alamat")
            pilih = int(input("Data yang ingin diubah : "))
            if pilih == 1:
                Nama = str(input("Masukan Nama\t: "))
            elif pilih == 2:
                Password = str(input("Masukan Password\t: "))
            elif pilih == 3:
                Email = self.check_email()
            elif pilih == 4:
                Nomor = "0" + str(int(input("Masukan Nomor\t: ")))
            elif pilih == 5:
                Alamat = str(input("Masukkan Alamat\t: "))
            else : 
                print("Pilihan tidak tersedia")
            lanjut = str(input("Ganti data lain (y/n)? "))
            if lanjut == 'y' :
                continue
            else :
                break
        query = """UPDATE siswa SET `Nama`= %s, `Password`= %s , `Email`= %s, `Nomor`= %s, `Alamat`= %s WHERE `Id_siswa` = %s"""
        data = (Nama, Email, Nomor, Password, Alamat, Id_siswa)
        self.db.insertValue(query, data)

    def update_siswa(self):
        print("=== Update Siswa ===")
        Id_siswa = int(input("Masukkan ID Siswa yang akan diupdate: "))
        query = """SELECT * FROM siswa WHERE Id_siswa = %s"""
        data = (Id_siswa,)
        self.db.selectValuepretty(query, data)
        result = self.db.selectValue(query, data)


        test = str(input("Apa data ingin diupdate (y/n)? "))
        if test.lower() == 'y' :
            self.edit_siswa(result, Id_siswa)
            print("=== Anda Berhasil Meng-update Data Siswa ===")
        else :
            print("=== Anda Gagal Meng-update Data Siswa ===")

    def delete_siswa(self):
        print("=== Delete Siswa ===")
        Id_siswa = int(input("Masukkan ID Siswa yang akan dihapus: "))
        query = """SELECT * FROM siswa WHERE Id_siswa = %s"""
        data = (Id_siswa,)
        self.db.selectValuepretty(query, data)
        test = str(input("Apa data ingin dihapus (y/n)? "))
        if test.lower() == 'y' :
            query = """DELETE FROM siswa WHERE Id_siswa = %s """
            data = (Id_siswa,)
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Menghapus Data Siswa ===")
            
        else :
            print("=== Anda Gagal Menghapus Data Siswa ===")

    def read_siswa(self):
        print("=== Read Siswa ===")
        query = """SELECT * FROM siswa"""
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


    def instert_guru(self):
        print("===== Input Data Guru =====")
        Nama = str(input("Masukan Nama\t: "))
        Email = self.check_email()
        Nomor = "0" + str(int(input("Masukkan Nomor\t: ")))
        Jenis_kelamin = self.jenis_kelamin()
        Tgl_lahir = str(input("Masukan Tanggal Lahir (format: YYYY-MM-DD)\t: "))
        Alamat = str(input("Masukan Alamat\t: "))
        Status_pekerja = str(input("Masukkan Status Pekerja (Kontrak/Tetap)\t: "))
        Bidang_mapel = self.bidang_mapel()
        Gaji = str(input("Masukkan Gaji\t: "))
        
        x = PrettyTable()
        x.field_names = ["Nama", "Email", "Nomor", "Jenis_kelamin", "Tgl_lahir", "Alamat", "Status_pekerja", "Bidang_mapel", "Gaji"]
        x.add_row([Nama, Email, Nomor, Jenis_kelamin, Tgl_lahir, Alamat, Status_pekerja, Bidang_mapel, Gaji])
        print(x)
        
        yakin = str(input("Yakin ingin menambah data guru y/n? "))
        if yakin == 'y':
            query = """INSERT INTO Guru(Nama, Email, Nomor, Jenis_kelamin, Tgl_lahir, Alamat, Status_pekerja, Bidang_mapel, Gaji) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            data = (Nama, Email, Nomor, Jenis_kelamin, Tgl_lahir, Alamat, Status_pekerja, Bidang_mapel, Gaji)
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Menambahkan Data Guru ===")
        else:
            print("=== Anda Gagal Menambahkan Data Guru ===")

    def update_guru(self):
        print("===== Update Guru =====")
        Id_guru = int(input("Masukkan ID Guru yang akan diupdate: "))
        query = """SELECT * FROM Guru WHERE Id_guru = %s"""
        data = (Id_guru,)
        self.db.selectValuepretty(query, data)
        result = self.db.selectValue(query, data)


        test = str(input("Apa data ingin diupdate (y/n)? "))
        if test.lower() == 'y':
            self.edit(result, Id_guru)
            print("=== Anda Berhasil Meng-update Data Guru ===")
        else:
            print("=== Anda Gagal Meng-update Data Guru ===")

    def delete_guru(self):
        print("===== Delete Guru =====")
        Id_guru = int(input("Masukkan ID Guru yang akan dihapus: "))
        query = """SELECT * FROM Guru WHERE Id_guru = %s"""
        data = (Id_guru,)
        self.db.selectValuepretty(query, data)
        test = str(input("Apa data ingin dihapus (y/n)? "))
        if test.lower() == 'y':
            query = """DELETE FROM Guru WHERE Id_guru = %s """
            data = (Id_guru,)
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Menghapus Data Guru ===")
        else:
            print("=== Anda Gagal Menghapus Data Guru ===")
            
    def read_guru(self):
        print("===== Read Guru =====")
        query = """SELECT * FROM Guru"""
        self.db.selectValuepretty(query, data=None)

    def read_jadwal_guru(self):
        while True:
            try:
                Id_guru = int(input("Masukkan ID Pengajar Anda: "))
                query_check = """SELECT * FROM guru WHERE Id_guru = %s """
                data_check = (Id_guru,)
                result = self.db.selectValue(query_check, data_check)
                
                if result:
                    query = """SELECT * FROM jadwal WHERE Id_guru = %s"""
                    data = (Id_guru,)
                    self.db.selectValuepretty(query, data)
                    break
                else:
                    print("ID Guru tidak ditemukan. Coba lagi!")
            except ValueError:
                print("Masukkan ID Guru dalam bentuk angka")
                
    def read_jadwal_pelayanan_guru(self):
        while True:
            try:
                Id_guru = int(input("Masukkan ID Pengajar Anda: "))
                query_check = """SELECT * FROM Guru WHERE Id_guru = %s"""
                data_check = (Id_guru,)
                result = self.db.selectValue(query_check, data_check)

                if result:
                    query = """SELECT * FROM Jadwal_pelayanan WHERE Id_guru = %s"""
                    data = (Id_guru,)
                    self.db.selectValuepretty(query, data)
                    break
                else:
                    print("ID Guru tidak ditemukan. Coba lagi!")
            except ValueError:
                print("Masukkan ID Guru dalam bentuk angka")

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

    def confirm_password(self) :
        while True :
            try :
                password = str(input("Masukan Password\t:"))
                conf_pass = str(input("Masukan Password sekali lagi\t:"))
                if password != conf_pass :
                    raise ValueError("Masukan password yang benar")
                return conf_pass
            except Exception as e :
                print(e)

    def inp_tanggal(self) :
        date_str = input("Masukkan tanggal tayang (format: YYYY-MM-DD)\t: ")
        date = datetime.strptime(date_str, "%Y-%m-%d")
        Tanggal = date.date() 
        return Tanggal
    
    def Status_pekerja(self):
        while True :
            print("\n=== Status Pekerjaan ===")
            print("1. Tetap")
            print("2. Kontrak")
            pilih = int(input("Pilih status : "))
            if pilih == 1 :
                return "Tetap"
            elif pilih == 2 :
                return "Kontrak"
            else :
                print("Pilihan tidak tersedia")
    
    def Jabatan(self) :
        while True :
            print("\n=== Jabatan Pekerjaan ===")
            print("1. Manager")
            print("2. Admin")
            print("3. OB")
            pilih = int(input("Pilih Jabatan : "))
            if pilih == 1 :
                return "Manager"
            elif pilih == 2 :
                return "Admin"
            elif pilih == 3 :
                return "OB"
            else :
                print("Pilihan tidak tersedia")

    def Tunjangan(self, status, gaji) :
        if status == "Tetap" :
            istri = str(input("Apa kamu memiliki istri? (y/n) "))
            if istri.lower() == "y" :
                while True :
                    anak = int(input("Kamu memiliki berapa anak? : "))
                    ank = anak * 2/100
                    tun1 = gaji * ank
                    tun2 = gaji * 1/100
                    final = tun1 + tun2
                    return final      
            else :
                return 0 
        else :
            return 0
        
    def gaji(self,jabatan, tunjangan) :
        if jabatan == "Manager" :
            x = 5000000
        elif jabatan == "Admin" :
            x = 3000000
        elif jabatan == "OB" :
            x = 1000000

        gaji = x + tunjangan
        return gaji

    def insert_pegawai(self): #done
        print("===== Input Admin =====")
        Nama = str(input("Masukan Nama\t: "))
        Email = self.check_email()
        password = self.confirm_password()
        Nomor = "0" + str(int(input("Masukan Nomor\t: ")))
        Jenis_kelamin = self.jenis_kelamin()
        tanggal = self.inp_tanggal()
        alamat = str(input("Masukan alamat\t:"))
        status = self.Status_pekerja()
        jabatan = self.Jabatan()
        Tunjangan = self.Tunjangan(status)
        gaji = self.gaji(jabatan,Tunjangan)

        
        x = PrettyTable()
        print("=== Data diri ===")
        x.field_names = ["Nama", "Email", "Nomor", "Jenis_kelamin", "tanggal_lahir", "alamat"]
        x.add_row([Nama, Email, Nomor,Jenis_kelamin,tanggal,alamat])
        print(x)
        yakin = str(input("Data anda sudah benar (y/n) ?"))
        if Nama and Email and Jenis_kelamin and tanggal and alamat and yakin.lower() == "y" :
            quary = """INSERT INTO `pegawai`(`Nama`, `Password`, `Email`, `Nomor`, `Jenis_kelamin`, `Tgl_lahir`, `Alamat`, `Status_pekerja`, `Jabatan`, `Tunjangan`, `Gaji`) 
            VALUES 
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            data = (Nama, password, Email, Nomor, Jenis_kelamin, tanggal,alamat,status,jabatan,Tunjangan,gaji)
            self.db.insertValue(quary,data)
            print("=== Anda Berhasil Mendaftar Sebagai Siswa ===")

        else : 
            print("=== Anda Gagal Mendaftar Sebagai Siswa ===")





    def edit_pegawai(self, result, Id_pegawai) : #done
        Nama = result[0][1]
        Password = result[0][2]
        Email = result[0][3]
        Nomor = result[0][4]
        Alamat = result[0][7]
        Status_pekerja = result[0][8]
        Jabatan = result[0][9]
        Tunjangan = result[0][10]
        while True : 
            print("=== Edit value ===")
            print("1. Nama")
            print("2. Password")
            print("3. Email")
            print("4. Nomor")
            print("5. Alamat")
            print("6. Status_pekerja")
            print("7. Jabatan")
            print("8. Tunjangan")
            pilih = int(input("Data yang ingin diubah : "))
            if pilih == 1 :
                Nama = str(input("Masukan Nama\t: "))
            elif pilih == 2 :
                Password = self.confirm_password()
            elif pilih == 3 :
                Email = self.check_email()
            elif pilih == 4 :
                Nomor = "0" + str(int(input("Masukan Nomor\t: ")))
            elif pilih == 5 :
                Alamat = str(input("Masukan alamat\t:"))
            elif pilih == 6 :
                Status_pekerja = self.Status_pekerja()
            elif pilih == 7 :
                Jabatan = self.Jabatan()
            elif pilih == 8 : 
                Tunjangan = self.Tunjangan(Status_pekerja)

            else : 
                print("Pilihan tidak tersedia")
            lanjut = str(input("Ganti data lain (y/n)? "))
            if lanjut == 'y' :
                continue
            else :
                break

        gaji = self.gaji(Jabatan,Tunjangan)
        query = """UPDATE `pegawai` SET 
        `Nama`=%s,
        `Password`=%s,
        `Email`=%s,
        `Nomor`=%s,
        `Alamat`=%s,
        `Status_pekerja`=%s,
        `Jabatan`=%s,
        `Tunjangan`=%s,
        `Gaji`=%s 
        WHERE `Id_pegawai`='%s'"""
        data = (Nama, Password,Email, Nomor, Alamat,Status_pekerja,Jabatan,Tunjangan,gaji,Id_pegawai)
        self.db.insertValue(query, data)

    def update_pegawai(self, Id_pegawai): #done not yet testing
        print("===== Update pegawai =====")
        # Id_admin = int(input("Masukkan ID Admin yang akan diupdate: "))
        query = """SELECT `Id_pegawai`, `Nama`, `Email`, `Nomor`, `Jenis_kelamin`, `Tgl_lahir`, `Alamat`, `Status_pekerja`, `Jabatan`, `Tunjangan`, `Gaji` FROM pegawai WHERE Id_pegawai = %s"""
        data = (Id_pegawai,)
        self.db.selectValuepretty(query, data)
        result = self.db.selectValue(query, data)


        test = str(input("Apa data ingin diupdate (y/n)? "))
        if test.lower() == 'y' :
            self.edit_pegawai(result, Id_pegawai)
            print("=== Anda Berhasil Meng-update Data Admin ===")
        else :
            print("=== Anda Gagal Meng-update Data Admin ===")


    def delete_admin(self, Id_pegawai):#done
        print("===== Delete Pegawai =====")
        query = """SELECT `Id_pegawai`, `Nama`, `Email`, `Nomor`, `Jenis_kelamin`, `Tgl_lahir`, `Alamat`, `Status_pekerja`, `Jabatan`, `Tunjangan`, `Gaji` FROM pegawai WHERE Id_pegawai = %s"""
        data = (Id_pegawai,)
        self.db.selectValuepretty(query, data)
        test = str(input("Apa data ingin dihapus (y/n)? "))
        if test.lower() == 'y' :
            query = """DELETE FROM admin WHERE Id_pegawai = %s """
            data = (Id_pegawai,)
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Menghapus Data Admin ===")
            
        else :
            print("=== Anda Gagal Menghapus Data Admin ===")


    def read_admin(self):
        print("===== Read Admin =====")
        query = """SELECT * FROM admin"""
        self.db.selectValuepretty(query, data=None)
