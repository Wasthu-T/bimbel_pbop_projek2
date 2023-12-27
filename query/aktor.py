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
        Id_paket_belajar = None

        Nama = str(input("Masukan Nama\t: "))
        Password = self.confirm_password()
        Email = self.check_email()
        Nomor = "0" + str(int(input("Masukan Nomor\t: ")))
        Jenis_kelamin = self.jenis_kelamin()
        Alamat = str(input("Masukkan Alamat\t: "))
        Tagihan = 0
        x = PrettyTable()
        print("=== Data diri : ")
        x.field_names = ["Nama", "Email", "Nomor", "Jenis_kelamin", "Alamat"]
        x.add_row([Nama, Email, Nomor, Jenis_kelamin, Alamat])
        print(x)
        yakin = str(input("Yakin ingin mendaftar y/n? "))
        if (yakin == 'y') :
            quary = """INSERT INTO Siswa(Id_paket_belajar, Nama, Password, Email, Nomor, Jenis_kelamin, Alamat, Tagihan) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            data = (Id_paket_belajar, Nama, Password, Email, Nomor, Jenis_kelamin, Alamat, Tagihan)

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
                Password = self.confirm_password()
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

    def update_siswa(self, Id_siswa):
        print("=== Update Siswa ===")
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

    def delete_siswa(self, Id_siswa):
        print("=== Delete Siswa ===")
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

    def tambah_paket(self, Id_siswa, Id_paket_belajar) :
        try :
            query = """SELECT * FROM siswa WHERE Id_siswa = %s"""
            data = (Id_siswa,)
            result = self.db.selectValue(query, data)
            if result[0][4] :
                raise ValueError("Anda telah memiliki paket belajar")
            
            querypb = """SELECT * FROM `paket_belajar` WHERE Id_paket_belajar=%s"""
            resultpb = self.db.selectValue(querypb, (Id_paket_belajar,))
            Tagihan = resultpb[0][3]

            query = """UPDATE siswa SET `Id_paket_belajar`= %s, Tagihan=%s WHERE `Id_siswa` = %s"""
            data = (Id_paket_belajar, Tagihan, Id_siswa)
            self.db.insertValue(query, data)

            print("Selamat Anda telah membeli paket belajar")

            
        except Exception as e :
            print(e)

    def read_siswa(self):
        print("===== Lihat Siswa =====")
        print("== 1. Lihat semua")
        print("== 2. Cari bedasarkan Id Paket Belajar")
        print("== 3. Cari bedasarkan Tagihan")
        pilih = int(input("Pilih menu : "))
        if pilih == 1 :
            query = """SELECT `Id_siswa`, `Nama`, `Id_paket_belajar`, `Email`, `Nomor`, `Kelas`, `Jenis_kelamin`, `Alamat`, `Tagihan` FROM `siswa`"""
            self.db.selectValuepretty(query, data=None)
        elif pilih == 2 :
            data = int(input("Masukan Id Paket Belajar : "))
            query = """SELECT `Id_siswa`, `Nama`, `Id_paket_belajar`, `Email`, `Nomor`, `Kelas`, `Jenis_kelamin`, `Alamat`, `Tagihan` FROM `siswa` WHERE Id_paket_belajar=%s"""
            self.db.selectValuepretty(query, (data,))
        elif pilih == 3 :
            query = """SELECT `Id_siswa`, `Nama`, `Id_paket_belajar`, `Email`, `Nomor`, `Kelas`, `Jenis_kelamin`, `Alamat`, `Tagihan` FROM `siswa` WHERE Tagihan > 0"""
            self.db.selectValuepretty(query, data= None)
        else :
            print("Pilihan tidak tersedia")

    def read_jadwal_siswa(self, Id_siswa) :
        try :
            query = """SELECT * FROM siswa WHERE Id_siswa = %s"""
            data = (Id_siswa,)
            result = self.db.selectValue(query, data)
            if not result[0][4] :
                raise ValueError("Anda belum membeli paket belajar")
            
            Id_paket_belajar = result[0][4]
            queryj = """SELECT * FROM `jadwal` WHERE Id_paket_belajar=%s"""
            self.db.selectValuepretty(queryj, (Id_paket_belajar, ))

        except Exception as e :
            print(e)

class Guru:
    def __init__(self, db):
        self.db = db

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
    
    def inp_tanggal(self) :
        date_str = input("Masukan Tanggal Lahir (format: YYYY-MM-DD)\t: ")
        date = datetime.strptime(date_str, "%Y-%m-%d")
        Tanggal = date.date() 
        return Tanggal

    def gaji(self) :
        x = int(input("Berapa kali pertemuan dalam 1 minggu? "))
        y = 20000
        gaji = x*y
        if x > 6 : 
            fgaji = 150000+gaji
            return fgaji
        else : 
            return gaji
    
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

    def instert_guru(self):
        print("===== Input Data Guru =====")
        Nama = str(input("Masukan Nama\t: "))
        Email = self.check_email()
        Password = self.confirm_password()
        Nomor = "0" + str(int(input("Masukkan Nomor\t: ")))
        Jenis_kelamin = self.jenis_kelamin()
        Tgl_lahir = self.inp_tanggal()
        Alamat = str(input("Masukan Alamat\t: "))
        Status_pekerja = self.Status_pekerja()
        Bidang_mapel = self.bidang_mapel()
        Gaji = self.gaji()
        # Gaji = 0 
        
        x = PrettyTable()
        print("=== Data diri : ")
        x.field_names = ["Nama", "Email", "Nomor", "Jenis_kelamin", "Tgl_lahir", "Alamat", "Status_pekerja", "Bidang_mapel"]
        x.add_row([Nama, Email, Nomor, Jenis_kelamin, Tgl_lahir, Alamat, Status_pekerja, Bidang_mapel])
        print(x)
        
        yakin = str(input("Yakin ingin menambah data guru y/n? "))
        if yakin == 'y':
            query = """INSERT INTO Guru(Nama, Email,Password, Nomor, Jenis_kelamin, Tgl_lahir, Alamat, Status_pekerja, Bidang_mapel, Gaji) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"""
            data = (Nama, Email, Password, Nomor, Jenis_kelamin, Tgl_lahir, Alamat, Status_pekerja, Bidang_mapel, Gaji)
            self.db.insertValue(query, data)
            print("=== Anda Berhasil Menambahkan Data Guru ===")
        else:
            print("=== Anda Gagal Menambahkan Data Guru ===")

    def edit_guru(self,result, Id_guru) : 
        Nama = result[0][1]
        Password= result[0][2]
        Email= result[0][3]
        Nomor=result[0][4]
        Alamat	=result[0][7]
        while True :
            print("=== Edit Value ===")
            print("1. Nama")
            print("2. Password")
            print("3. Email")
            print("4. Nomor")
            print("5. Alamat")
            pilih = int(input("Data yang ingin diubah : "))
            if pilih == 1 :
                Nama = str(input("Masukan Nama\t: "))
            elif pilih == 2 :
                Password = self.confirm_password()
            elif pilih == 3 :
                Email = self.check_email()
            elif pilih == 4 :
                Nomor = "0" + str(int(input("Masukkan Nomor\t: ")))
            elif pilih == 5 :
                Alamat = str(input("Masukan Alamat\t: "))
            else : 
                print("Pilihan tidak tersedia")
            lanjut = str(input("Ganti data lain (y/n)? "))
            if lanjut == 'y' :
                continue
            else :
                break
        query = """UPDATE `guru` SET 
                    `Nama`=%s,
                    `Password`=%s,
                    `Email`=%s,
                    `Nomor`=%s,
                    `Alamat`=%s, WHERE `Id_guru`=%s"""
        data = (Nama, Password, Email, Nomor, Alamat, Id_guru)
        self.db.insertValue(query, data)

    def update_guru(self, Id_guru):
        print("===== Update Guru =====")
        query = """SELECT * FROM Guru WHERE Id_guru = %s"""
        data = (Id_guru,)
        self.db.selectValuepretty(query, data)
        result = self.db.selectValue(query, data)


        test = str(input("Apa data ingin diupdate (y/n)? "))
        if test.lower() == 'y':
            self.edit_guru(result, Id_guru)
            print("=== Anda Berhasil Meng-update Data Guru ===")
        else:
            print("=== Anda Gagal Meng-update Data Guru ===")

    def delete_guru(self, Id_guru):
        print("===== Delete Guru =====")
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
        print("===== Lihat Guru =====")
        print("== 1. Lihat semua")
        print("== 2. Cari bedasarkan Bidang Mapel")
        pilih = int(input("Pilih menu : "))
        if pilih == 1 :
            query = """SELECT `Id_guru`, `Nama`, `Email`, `Nomor`, `Jenis_kelamin`, `Tgl_lahir`, `Alamat`, `Status_pekerja`, `Bidang_mapel`, `Gaji` FROM `guru`"""
            self.db.selectValuepretty(query, data=None)
        elif pilih == 2 :
            data = (self.bidang_mapel(), )
            query = """SELECT `Id_guru`, `Nama`, `Email`, `Nomor`, `Jenis_kelamin`, `Tgl_lahir`, `Alamat`, `Status_pekerja`, `Bidang_mapel`, `Gaji` FROM `guru` WHERE Bidang_mapel=%s"""
            self.db.selectValuepretty(query, data)


    def read_jadwal_guru(self, Id_guru) :
        query = """SELECT * FROM jadwal WHERE Id_guru = %s"""
        data = (Id_guru,)
        self.db.selectValuepretty(query, data)
                
    def read_jadwal_pelayanan_guru(self,Id_guru):
        query = """SELECT * FROM Jadwal_pelayanan WHERE Id_guru = %s"""
        data = (Id_guru,)
        self.db.selectValuepretty(query, data)

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
        date_str = input("Masukkan tanggal lahir (format: YYYY-MM-DD)\t: ")
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
            istri = str(input("Apa kamu sudah berkeluarga? (y/n) "))
            if istri.lower() == "y" :
                while True :
                    anak = int(input("Kamu memiliki berapa anak? : "))
                    ank = anak * 2/100
                    tun1 = gaji * ank
                    tun2 = gaji * 5/100
                    final = tun1 + tun2
                    return final      
            else :
                return 0 
        else :
            return 0
        
    def gaji(self,jabatan) :
        if jabatan == "Manager" :
            gaji = 5000000
        elif jabatan == "Admin" :
            gaji = 3000000
        elif jabatan == "OB" :
            gaji = 1000000
        return gaji

    def insert_pegawai(self): #done
        print("===== Input Pegawai =====")
        Nama = str(input("Masukan Nama\t: "))
        Email = self.check_email()
        password = self.confirm_password()
        Nomor = "0" + str(int(input("Masukan Nomor\t: ")))
        Jenis_kelamin = self.jenis_kelamin()
        tanggal = self.inp_tanggal()
        alamat = str(input("Masukan alamat\t:"))
        status = self.Status_pekerja()
        jabatan = self.Jabatan()
        gaji = self.gaji(jabatan)
        Tunjangan = self.Tunjangan(status, gaji)

        
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
            print("=== Anda Berhasil Mendaftar Sebagai Pegawai ===")

        else : 
            print("=== Anda Gagal Mendaftar Sebagai Pegawai ===")


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


    def delete_Pegawai(self, Id_pegawai):#done
        print("===== Delete Pegawai =====")
        test = str(input("Apa data ingin dihapus (y/n)? "))
        if test.lower() == 'y' :
            query = """DELETE FROM admin WHERE Id_pegawai = %s """
            self.db.insertValue(query, (Id_pegawai, ))
            print("=== Anda Berhasil Menghapus Data Admin ===")
            
        else :
            print("=== Anda Gagal Menghapus Data Admin ===")

    def read_Pegawai(self):
        print("===== Lihat Pegawai =====")
        print("== 1. Lihat semua")
        print("== 2. Cari bedasarkan jabatan")
        pilih = int(input("Pilih menu : "))
        if pilih == 1 :
            query = """SELECT `Id_pegawai`, `Nama`, `Email`, `Nomor`, `Jenis_kelamin`, `Tgl_lahir`, `Alamat`, `Status_pekerja`, `Jabatan`, `Tunjangan`, `Gaji` FROM `pegawai` """
            self.db.selectValuepretty(query, data=None)
        elif pilih == 2 :
            data = (self.Jabatan(), )
            query = """SELECT `Id_pegawai`, `Nama`, `Email`, `Nomor`, `Jenis_kelamin`, `Tgl_lahir`, `Alamat`, `Status_pekerja`, `Jabatan`, `Tunjangan`, `Gaji` FROM `pegawai` WHERE Jabatan=%s"""
            self.db.selectValuepretty(query, data)
