from prettytable import PrettyTable
from email_validator import validate_email, EmailNotValidError
from datetime import datetime, timedelta
from query.aktor import Siswa, Guru, Pegawai
import os 
import locale


# set bahasa waktu lokal indonesia
locale.setlocale(locale.LC_TIME, 'id_ID')

class login :
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

    def cheking(self, tabel) :
        os.system('cls')
        run = True
        while run:
            try:
                query = ""f"SELECT * FROM {tabel} WHERE Email = %s"""
                data = self.check_email()
                result = self.db.selectValue(query, (data, ))

                if result and len(result) > 0:  
                    password = result[0][2]

                    inppass = str(input("Masukan Password\t: "))
                    if inppass == password:
                        print("="*35)
                        print("===\tLogin Berhasil!\t\t===")
                        print(f"== Selamat Datang {result[0][1]} ==")
                        print("="*35)
                        run = False 
                        os.system('pause')
                        id = result[0][0]
                        nama = result[0][1]
                        
                        return id, nama
                    else:
                        raise ValueError("Email atau password salah")
                else:
                    raise ValueError("Email atau password salah")
                    
            except Exception as e:
                print(e)

    def cheking_jabatan(self, tabel) :
        os.system('cls')
        run = True
        while run:
            try:
                query = ""f"SELECT * FROM {tabel} WHERE Email = %s"""
                data = self.check_email()
                result = self.db.selectValue(query, (data, ))

                if result and len(result) > 0:  
                    password = result[0][2]

                    inppass = str(input("Masukan Password\t: "))
                    if inppass == password:
                        print("="*35)
                        print("===\tLogin Berhasil!\t\t===")
                        print(f"== Selamat Datang {result[0][1]} ==")
                        print("="*35)
                        run = False 
                        os.system('pause')
                        id = result[0][0]
                        nama = result[0][1]
                        jabatan = result[0][9]
                        return id, nama, jabatan
                    else:
                        raise ValueError("Email atau password salah")
                else:
                    raise ValueError("Email atau password salah")
                    
            except Exception as e:
                print(e)

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

    def kembalian(self, tagihan, bayar) :
        sisa_tagihan = tagihan-bayar
        if sisa_tagihan < 0 :
            sisa_tagihan = 0

        kembalian = bayar-tagihan
        if kembalian < 0 :
            kembalian = 0

        return kembalian, sisa_tagihan
        
    def bayar_tagihan(self, Id_siswa) :
        try :
            query_siswa = """SELECT 
            `Id_siswa`, `Nama`, `Email`, `Id_paket_belajar`, `Nomor`, `Kelas`, `Jenis_kelamin`, `Alamat`, `Tagihan` 
            FROM `siswa` WHERE Id_siswa=%s"""

            resultsiswa = self.db.selectValue(query_siswa, (Id_siswa, ))
            Id_Paket_belajar = resultsiswa[0][3]
            Tagihan = resultsiswa[0][8]

            if Tagihan == 0 :
                raise ValueError("Anda Tidak Memiliki Tagihan")

            x = PrettyTable()
            x.field_names=["Id Paket Belajar", "Tagihan Anda"]
            x.add_row([Id_Paket_belajar,Tagihan])
            print(x)
            test = str(input("Ingin membayar tagihan (y/n) ? "))
            if test == "y" : 
                Jenis_pembayaran = "Transfer"
                Bayar = int(input("Masukan Nominal Bayar\t: "))
                if Bayar > Tagihan :
                    raise ValueError("Anda memasukkan jumlah lebih dari tagihan")
                Kembalian, tagihan_tersisa = self.kembalian(Tagihan, Bayar)
                Tgl_transaksi = datetime.now().date()

                quary = """INSERT INTO transaksi(Id_pegawai, Id_siswa, Id_paket_belajar, Jenis_pembayaran, Bayar, Kembalian, Tgl_transaksi) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                data = (None, Id_siswa, Id_Paket_belajar, Jenis_pembayaran, Bayar, Kembalian, Tgl_transaksi)
                self.db.insertValue(quary,data)

                query_tag = """UPDATE `siswa` SET `Tagihan`=%s WHERE Id_siswa=%s"""
                edit = (tagihan_tersisa, Id_siswa)
                self.db.insertValue(query_tag, edit)
                if tagihan_tersisa != 0 :
                    print(f"Tagihan anda masih : {tagihan_tersisa}")

                print("=== Anda Berhasil Membayar Paket Belajar ===")
            else : 
                print("=== Kembali ke menu utama ===")
                

        except Exception as e :
            print(e)

    def insert_transaksi(self, Id_pegawai):
        try :
            print("===== Input Transaksi =====")
            id_siswa, Id_Paket_belajar, Tagihan = self.get_siswa()
            if not (id_siswa and Id_Paket_belajar and Tagihan) :
                raise ValueError("Data kurang lengkap")
            
            if Tagihan == 0 :
                raise ValueError("Anda tidak memiliki tagihan")

            Jenis_pembayaran = self.jenis_pembayaran()
            Bayar = int(input("Masukan Nominal Bayar\t: "))
            Kembalian, tagihan_tersisa = self.kembalian(Tagihan, Bayar)
            Tgl_transaksi = datetime.now().date()

            x = PrettyTable()
            x.field_names = ["Id_pegawai", "Id_siswa","Id_paket_belajar", "Jenis_pembayaran", "Bayar", "Kembalian", "Tgl_transaksi"]
            x.add_row([Id_pegawai, id_siswa, Id_Paket_belajar, Jenis_pembayaran, Bayar, Kembalian, Tgl_transaksi])
            print(x)

            quary = """INSERT INTO transaksi(Id_pegawai, Id_siswa, Id_paket_belajar, Jenis_pembayaran, Bayar, Kembalian, Tgl_transaksi) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            data = (Id_pegawai, id_siswa, Id_Paket_belajar, Jenis_pembayaran, Bayar, Kembalian, Tgl_transaksi)
            self.db.insertValue(quary,data)

            query_tag = """UPDATE `siswa` SET `Tagihan`=%s WHERE Id_siswa=%s"""
            edit = (tagihan_tersisa, id_siswa)
            self.db.insertValue(query_tag, edit)
            if tagihan_tersisa != 0 :
                print(f"Tagihan anda masih : {tagihan_tersisa}")

            print("=== Anda Berhasil Membayar Paket Belajar ===")

        
        except Exception as e :
            print(e)

    def kelas(self) :
        while True :
            print("\n=== Jenjang Pendidikan ===")
            print("1. SD")
            print("2. SMP")
            print("3. SMA")
            pilih = int(input("Pilih Jenjang Pendidikan\t: "))
            if pilih == 1 :
                kelas = int(input("Kelas berapa? (4/5/6) \t: "))
                if kelas in [4,5,6] :
                    xkel = str(kelas)+"SD"
                    return xkel
                else : 
                    print("Pilihan tidak tersedia")
            elif pilih == 2 :
                kelas = int(input("Kelas berapa? (1/2/3) \t: "))
                if kelas in [1,2,3] :
                    xkel = str(kelas)+"SMP"
                    return xkel
                else : 
                    print("Pilihan tidak tersedia")
            elif pilih == 3 :
                kelas = int(input("Kelas berapa? (1/2/3) \t: "))
                if kelas in [1,2,3] :
                    jurusan = str(input("Jurusan apa? (IPA/IPS) :"))
                    if jurusan.upper() in ["IPA","IPS"] :
                        xkel = str(kelas)+"SMA "+ jurusan.upper()
                        return xkel
                    else : 
                        print("Pilihan tidak tersedia")
                else : 
                    print("Pilihan tidak tersedia")
            else :
                print("pilihan tidak tersedia harap pilih yang benar")
     
    def get_siswa(self) :
            try :
                print("=== Cari Siswa ===")
                print("1. Bedasarkan Kelas")
                print("2. Bedasarkan Id Siswa")
                print("3. Kembali")
                pilih = int(input("Pilih Menu : "))
                if pilih == 1 :
                    query_kelas = """SELECT Id_siswa, Nama,Kelas,Tagihan FROM siswa WHERE `Kelas`=%s"""
                    kelas = self.kelas()
                    self.db.selectValuepretty(query_kelas, (kelas, ))
                    result = self.db.selectValue(query_kelas, (kelas, ))

                    if not result :
                        raise ValueError("Data tidak tersedia")

                    a=0
                    list_id = []
                    for a in range(len(result)) :
                        check_id_siswa = result[a][0]
                        list_id.append(check_id_siswa)
                    
                    Id_siswa = int(input("Masukan Id siswa : "))

                    if Id_siswa not in list_id :
                        raise ValueError("Id siswa tidak ditemukan")
                    
                    query_siswa = """SELECT 
                    `Id_siswa`, `Nama`, `Email`, `Id_paket_belajar`, `Nomor`, `Kelas`, `Jenis_kelamin`, `Alamat`, `Tagihan` 
                    FROM `siswa` WHERE Id_siswa=%s"""

                    self.db.selectValuepretty(query_kelas, (kelas, ))
                    check = str(input("Data benar (y/n) ? "))
                    if check.lower() == 'y' :
                        resultsiswa = self.db.selectValue(query_siswa, (Id_siswa, ))
                        id_siswa = resultsiswa[0][0]
                        Id_Paket_belajar = resultsiswa[0][3]
                        Tagihan = resultsiswa[0][8]
                        return id_siswa, Id_Paket_belajar, Tagihan
                    else :
                        raise ValueError("Kembali ke menu cari siswa")


                elif pilih == 2 :
                    query_siswa = """SELECT 
                    `Id_siswa`, `Nama`, `Email`, `Id_paket_belajar`, `Nomor`, `Kelas`, `Jenis_kelamin`, `Alamat`, `Tagihan` 
                    FROM `siswa` WHERE Id_siswa=%s"""

                    self.db.selectValuepretty(query_kelas, (kelas, ))
                    resultsiswa = self.db.selectValue(query_siswa, (Id_siswa, ))
                    if not resultsiswa :
                        raise ValueError("Id siswa tidak tersedia")
                    
                    check = str(input("Data benar (y/n) ? "))
                    if check.lower() == 'y' :
                        id_siswa = resultsiswa[0][0]
                        Id_Paket_belajar = resultsiswa[0][3]
                        Tagihan = resultsiswa[0][8]
                        return id_siswa, Id_Paket_belajar, Tagihan
                    
                    else :
                        raise ValueError("Kembali ke menu cari siswa")
                elif pilih == 3 :
                    print("=== Kembali ke menu utama ===")
                    
                else :
                    print("=== Pilihan Tidak Tersedia ===")

            except Exception as e :
                print(e)
                os.system('pause')

    def read_transaksi(self):
        print("=== Lihat Transaksi ===")
        print("1. Lihat bedasarkan Siswa")
        print("2. Lihat bedasarkan Paket belajar")
        print("3. Lihat bedasarkan Jenis pembayaran")
        print("4. Lihat bedasarkan Tanggal Transaksi")
        print("5. Lihat semua")
        pilih = int(input("Pilih menu : ")) 
        if pilih == 1 :
            query = """SELECT * FROM transaksi WHERE Id_siswa=%s"""
            data = int(input("Masukan id siswa : "))
            self.db.selectValuepretty(query, (data, ))
        elif pilih == 2 :
            query = """SELECT * FROM transaksi WHERE Id_paket_belajar=%s"""
            data =int(input("Masukan id paket belajar : "))
            self.db.selectValuepretty(query, (data, ))
        elif pilih == 3 :
            query = """SELECT * FROM transaksi WHERE Jenis_pembayaran=%s"""
            data = self.jenis_pembayaran()
            self.db.selectValuepretty(query, (data,))
        elif pilih == 4 :
            query = """SELECT * FROM transaksi WHERE Tgl_transaksi=%s"""
            data = input("Masukkan Tanggal (format: YYYY-MM-DD)\t: ")
            self.db.selectValuepretty(query, (data, ))
        elif pilih == 5 :
            query = """SELECT * FROM transaksi"""
            self.db.selectValuepretty(query, data=None)
        else :
            print("Pilihan tidak tersedia")

class jadwal : 
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
                kelas = int(input("Kelas berapa? (4/5/6) :"))
                if kelas in [4,5,6] :
                    xkel = str(kelas)+"SD"
                    return xkel
                else : 
                    print("Pilihan tidak tersedia")
            elif pilih == 2 :
                kelas = int(input("Kelas berapa? (1/2/3) :"))
                if kelas in [1,2,3] :
                    xkel = str(kelas)+"SMP"
                    return xkel
                else : 
                    print("Pilihan tidak tersedia")
            elif pilih == 3 :
                kelas = int(input("Kelas berapa? (1/2/3) :"))
                if kelas in [1,2,3] :
                    jurusan = str(input("Jurusan apa? (IPA/IPS) :"))
                    if jurusan.upper() in ["IPA","IPS"] :
                        xkel = str(kelas)+"SMA "+ jurusan.upper()
                        return xkel
                    else : 
                        print("Pilihan tidak tersedia")
                else : 
                    print("Pilihan tidak tersedia")
            else :
                print("pilihan tidak tersedia harap pilih yang benar")
                
    def mapel(self):
        while True:
            print("\n=== Mata Pelajaran ===")
            mapel = [
                'Bahasa Inggris', 'Ilmu Pengetahuan Alam', 'Tes Potensi Skolastik', 'Matematika',
                'Bahasa Indonesia', 'Biologi', 'Kimia', 'Geografi', 'Ekonomi',
                'Sosiologi', 'Sejarah', 'Fisika'
            ]       
            for idx, pelajaran in enumerate(mapel, 1):
                print(f"{idx}. {pelajaran}")
            opsi = int(input("Pilih Mata Pelajaran\t:"))
            if 1 <= opsi <= len(mapel):
                return mapel[opsi - 1]
            else:
                print("Pilihan tidak tersedia")
    
    def check_jam(self) :
        try:
            jam_mulai = input("Mulai Jam (HH:MM:SS): ")
            waktu_mulai = datetime.strptime(jam_mulai, "%H:%M:%S")
            waktu_mulai_jadwal = datetime.strptime("15:00:00", "%H:%M:%S")
            if waktu_mulai < waktu_mulai_jadwal:
                raise ValueError(f"Waktu jam kerja 15:00:00")
            
            jam_selesai = input("Selesai Jam (HH:MM:SS): ")
            waktu_selesai = datetime.strptime(jam_selesai, "%H:%M:%S")
            waktu_selesai_jadwal = datetime.strptime("21:00:00", "%H:%M:%S")
            if waktu_selesai > waktu_selesai_jadwal:
                raise ValueError(f"Waktu selesai kerja 21:00:00")
            
            durasi_maksimal = timedelta(hours=1, minutes=30)
            batas_waktu = waktu_mulai + durasi_maksimal

            if waktu_selesai > batas_waktu:
                raise ValueError("Durasi pembelajaran tidak boleh lebih dari 1 jam 30 menit")

            return jam_mulai,jam_selesai

        except Exception as e:
            print(e)

    def get_data_paket(self, result) :
        kelas = result[0][1]
        kategori = result[0][2]
        return kelas, kategori


    def get_guru(self, result) :
        return result[0][1],result[0][9], result[0][10]

    def insert_jadwal(self):
        try :
            print("===== Input Jadwal =====")
            mapelku = self.mapel()
            quguru = """SELECT `Id_guru`, `Nama`, `Bidang_mapel` FROM `guru` WHERE Bidang_mapel=%s"""
            self.db.selectValuepretty(quguru, (mapelku, ))

            
            Id_guru = int(input("Masukkan ID Guru\t: "))
            qdata_guru = """SELECT * FROM `guru` WHERE Id_guru=%s"""
            resultg = self.db.selectValue(qdata_guru, (Id_guru, ))

            a = 0
            check_id = self.db.selectValue(quguru, (mapelku, ))
            list_id = []
            for a in range(len(check_id)) :
                check_id_guru = check_id[a][0]
                list_id.append(check_id_guru)

            if Id_guru not in list_id : 
                raise ValueError("=== Id Guru tidak ditemukan ===")
                
            if not resultg :
                raise ValueError("=== Id Guru tidak ditemukan ===")
            nama, mapel, gaji = self.get_guru(resultg)

            Kelas = self.kelas()
            Jam_mulai, Jam_selesai = self.check_jam()

            query = """SELECT * FROM paket_belajar WHERE Kelas=%s"""
            data = (Kelas, )
            self.db.selectValuepretty(query, data)

            Id_paket = int(input("Masukan Id Belajar : "))
            paket_query = """SELECT * FROM paket_belajar WHERE Id_paket_belajar=%s"""
            result = self.db.selectValue(paket_query, (Id_paket,))

            b= 0
            check_paket = self.db.selectValue(query, data)
            list_paket = []
            for b in range(len(check_paket)) :
                check_id_paket = check_paket[b][0]
                list_paket.append(check_id_paket)

            if Id_paket not in list_paket :
                raise ValueError("=== Id Paket Belajar tidak ditemukan ===")

            if not result:
                raise ValueError("=== Id Paket Belajar tidak ditemukan ===")

            kelas, kategori = self.get_data_paket(result)
            Tanggal_str = input("Masukkan Tanggal (format: YYYY-MM-DD)\t: ")
            Tanggal = datetime.strptime(Tanggal_str, "%Y-%m-%d").date()


            ruang_query ="""SELECT * FROM `ruangan`"""
            self.db.selectValuepretty(ruang_query, data=None)

            Id_ruangan = int(input("Masukkan ID Ruangan\t: "))
            select_query = """SELECT * FROM `ruangan` WHERE Id_ruangan=%s"""
            resultR = self.db.selectValue(select_query, (Id_ruangan,))
            if not resultR[0][0] :
                raise ValueError("=== Id Ruang tidak ditemukan ===")
            if resultR[0][1] == "Tidak layak" :
                raise ValueError("=== Ruang Tidak Layak ===")

            x = PrettyTable()
            x.field_names = ["Data", "Value"]
            x.add_row(["Id Guru", Id_guru])
            x.add_row(["Nama Guru", nama])
            x.add_row(["Mapel Guru", mapel])
            x.add_row(["Kelas", kelas])
            x.add_row(["Jam", f"{Jam_mulai}-{Jam_selesai}"])
            x.add_row(["Tanggal", Tanggal])
            x.add_row(["Id_ruangan", Id_ruangan])
            print(x)
            confirm = input("Apakah anda ingin melanjutkan tindakan ini (y/n): ")
            
            if confirm == 'y':
                query = """INSERT INTO `jadwal`(`Id_guru`, `Id_paket_belajar`, `Kelas`, `Mapel`, `Jam_mulai`, `Jam_selesai`, `Tanggal`, `Id_ruangan`, `Paket_belajar`) 
                VALUES 
                (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                data = (Id_guru, Id_paket, kelas, mapel, Jam_mulai, Jam_selesai, Tanggal, Id_ruangan, kategori)
                self.db.insertValue(query, data)

                queryguru = """UPDATE `guru` SET 
                    `Gaji`=%s
                    WHERE `Id_guru`=%s"""
                tambahgaji = gaji+20000
                dataguru =(tambahgaji, Id_guru)
                self.db.insertValue(queryguru, dataguru)
                print("=== Anda Berhasil Meng-input Data Jadwal ===")
            else:
                raise ValueError("=== Insert data anda gagal ===")
        except Exception as e :
            print(e)
    def update_jadwal(self):
        try : 
            print("=== Update Jadwal ===")
            self.read_jadwal()
            Id_jadwal = int(input("Masukkan ID Jadwal yang akan diupdate: "))
            
            query = """SELECT * FROM Jadwal WHERE Id_jadwal = %s"""
            querytes = """SELECT * FROM Jadwal"""
            data = (Id_jadwal,)
            a = 0
            check_id = self.db.selectValue(querytes, data=None)
            list_check = []
            for a in range(len(check_id)) :
                check_id_jadwal = check_id[a][0]
                list_check.append(check_id_jadwal)

            if Id_jadwal not in list_check: 
                raise ValueError("=== Id Jadwal tidak ditemukan ===")
                
            if not check_id :
                raise ValueError("=== Id Jadwal tidak ditemukan ===")
            
            self.db.selectValuepretty(query, data)
            result = self.db.selectValue(query, data)
            confirmation = input("Apakah Anda ingin melanjutkan proses update (y/n)? ").lower()
            
            if confirmation == 'y':
                self.edit_jadwal(result, Id_jadwal)
                print("=== Data Jadwal berhasil diupdate ===")
            else:
                print("=== Proses update dibatalkan ===")

        except Exception as e :
            print(e)
            os.system('pause')

    def edit_jadwal(self, result, Id_jadwal):
        Id_guru = result[0][1]
        Bidang_mapel = result[0][4]
        Id_ruangan = result[0][8]
        print(Bidang_mapel)
        while True:
            try :
                print("=== Edit Value ===")
                print("1. Id Guru")
                print("2. Id Ruangan")
                pilih = int(input("Data yang ingin diubah: "))

                if pilih == 1:
                    quguru = """SELECT `Id_guru`, `Nama`, `Bidang_mapel` FROM `guru` WHERE Bidang_mapel=%s"""
                    self.db.selectValuepretty(quguru, (Bidang_mapel, ))
                    data = self.db.selectValue(quguru,(Bidang_mapel, ))
                    if not data :
                        raise ValueError("Data tidak ditemukan")
                    
                    a = 0
                    Id_guru = int(input("Masukkan ID Guru baru\t: "))
                    for a in range(len(data)) :
                        check_id_guru = data[a][1]

                    if check_id_guru != Id_guru : 
                        raise ValueError("=== Id Guru tidak ditemukan ===")
                    
                    query = """UPDATE Jadwal SET Id_guru = %s WHERE Id_jadwal = %s"""
                    data = (Id_guru, Id_jadwal)
                    self.db.insertValue(query, data)


                elif pilih == 2:
                    ruang_query ="""SELECT * FROM `ruangan`"""
                    self.db.selectValuepretty(ruang_query, data=None)

                    Id_ruangan = int(input("Masukkan ID Ruangan baru\t: "))
                    select_query = """SELECT `Id_ruangan`, `Kondisi_ruangan`, `Kapasitas_kursi` FROM `ruangan` WHERE Id_ruangan=%s"""
                    resultR = self.db.selectValue(select_query, (Id_ruangan,))
                    if not resultR :
                        raise ValueError("=== Id Ruang tidak ditemukan ===")
                    if resultR[0][1] == "Tidak layak" :
                        raise ValueError("=== Ruang Tidak Layak ===")
                
                    query = """UPDATE Jadwal SET Id_ruangan = %s WHERE Id_jadwal = %s"""
                    data = (Id_ruangan, Id_jadwal)
                    self.db.insertValue(query, data)
                    
                else:
                    print("Pilihan tidak tersedia")

                lanjut = str(input("Ganti data lain (y/n)? "))
                if lanjut.lower() != 'y':
                    break
                print("=== Anda Berhasil Meng-update Data Jadwal ===")
            except Exception as e  :
                print(e)
                os.system('pause')
            
    def delete_jadwal(self):
        try :
            print("=== Delete Jadwal ===")
            self.read_jadwal()
            Id_jadwal = int(input("Masukkan ID Jadwal yang akan dihapus: "))

            query_select = """SELECT * FROM jadwal WHERE Id_jadwal = %s"""
            data_select = (Id_jadwal,)
            self.db.selectValuepretty(query_select, data_select)

            data = self.db.selectValue(query_select, data_select)

            if not data :
                raise ValueError("Data tidak ditemukan")
            
            a = 0
            Id_jadwal = int(input("Masukkan Id Jadwal \t: "))
            list_jadwal = []
            for a in range(len(data)) :
                check_Id_jadwal = data[a][1]
                list_jadwal.append(check_Id_jadwal)

            if Id_jadwal not in list_jadwal : 
                raise ValueError("=== Id Jadwal tidak ditemukan ===")

            test = str(input("Apakah Anda yakin ingin menghapus data ini (y/n)? "))
            
            if test.lower() == 'y':
                query_delete = """DELETE FROM jadwal WHERE Id_jadwal = %s"""
                data_delete = (Id_jadwal,)
                self.db.insertValue(query_delete, data_delete)
                print("=== Anda Berhasil Menghapus Data Jadwal ===")
            else:
                print("=== Pembatalan Penghapusan Data Jadwal ===")
        except Exception as e :
            print(e)
            os.system('pause')
    
    def read_jadwal(self):
        while True : 
            print("=== Lihat Jadwal ===")
            print("1. Lihat semua jadwal")
            print("2. Lihat bedasarkan mapel")
            pilih = int(input("Pilih menu : "))
            if pilih == 1 :
                query = """SELECT * FROM jadwal"""
                self.db.selectValuepretty(query, data=None)
                print("=== Anda Berhasil menampilkan Data Jadwal ===")
                break
            elif pilih == 2 :
                mapelku = self.mapel()
                quguru = """SELECT * FROM `jadwal` WHERE mapel=%s"""
                self.db.selectValuepretty(quguru, (mapelku, ))
                print("=== Anda Berhasil menampilkan Data Jadwal ===")
                break
            else :
                print("=== Pilihan tidak tersedia ===")

class jadwal_pelayanan :
    def __init__(self, db):
        self.db = db
            
    def mapel(self):
        while True:
            print("\n=== Mata Pelajaran ===")
            mapel = [
                'Bahasa Inggris', 'Ilmu Pengetahuan Alam', 'Tes Potensi Skolastik', 'Matematika',
                'Bahasa Indonesia', 'Biologi', 'Kimia', 'Geografi', 'Ekonomi',
                'Sosiologi', 'Sejarah', 'Fisika'
            ]       
            for idx, pelajaran in enumerate(mapel, 1):
                print(f"{idx}. {pelajaran}")
            opsi = int(input("Pilih Mata Pelajaran\t:"))
            if 1 <= opsi <= len(mapel):
                return mapel[opsi - 1]
            else:
                print("Pilihan tidak tersedia")
    
    def check_jam(self) :
        try:
            jam_mulai = input("Mulai Jam (HH:MM:SS): ")
            waktu_mulai = datetime.strptime(jam_mulai, "%H:%M:%S")
            waktu_mulai_jadwal = datetime.strptime("15:00:00", "%H:%M:%S")
            if waktu_mulai < waktu_mulai_jadwal:
                raise ValueError(f"Waktu jam kerja 15:00:00")
            
            jam_selesai = input("Selesai Jam (HH:MM:SS): ")
            waktu_selesai = datetime.strptime(jam_selesai, "%H:%M:%S")
            waktu_selesai_jadwal = datetime.strptime("21:00:00", "%H:%M:%S")
            if waktu_selesai > waktu_selesai_jadwal:
                raise ValueError(f"Waktu selesai kerja 21:00:00")
            
            durasi_maksimal = timedelta(hours=1, minutes=30)
            batas_waktu = waktu_mulai + durasi_maksimal

            if waktu_selesai > batas_waktu:
                raise ValueError("Durasi pembelajaran tidak boleh lebih dari 1 jam 30 menit")

            return jam_mulai,jam_selesai

        except Exception as e:
            print(e)

    def get_guru(self, result) :
        return result[0][1],result[0][9], result[0][10]

    def insert_jadwal_pelayanan(self):
        try :
            print("===== Input Jadwal =====")
            mapelku = self.mapel()
            quguru = """SELECT `Id_guru`, `Nama`, `Bidang_mapel` FROM `guru` WHERE Bidang_mapel=%s"""
            self.db.selectValuepretty(quguru, (mapelku, ))

            
            Id_guru = int(input("Masukkan ID Guru\t: "))
            qdata_guru = """SELECT * FROM `guru` WHERE Id_guru=%s"""
            resultg = self.db.selectValue(qdata_guru, (Id_guru, ))

            a = 0
            check_id = self.db.selectValue(quguru, (mapelku, ))
            list_id = []
            for a in range(len(check_id)) :
                check_id_guru = check_id[a][0]
                list_id.append(check_id_guru)

            if Id_guru not in list_id : 
                raise ValueError("=== Id Guru tidak ditemukan ===")
                
            if not resultg :
                raise ValueError("=== Id Guru tidak ditemukan ===")
            nama, mapel, gaji = self.get_guru(resultg)


            Jam_mulai, Jam_selesai = self.check_jam()


            ruang_query ="""SELECT * FROM `ruangan`"""
            self.db.selectValuepretty(ruang_query, data=None)

            Id_ruangan = int(input("Masukkan ID Ruangan\t: "))
            select_query = """SELECT * FROM `ruangan` WHERE Id_ruangan=%s"""
            resultR = self.db.selectValue(select_query, (Id_ruangan,))
            if not resultR :
                raise ValueError("=== Id Ruang tidak ditemukan ===")
            if resultR[0][1] == "Tidak layak" :
                raise ValueError("=== Ruang Tidak Layak ===")


            x = PrettyTable()
            x.field_names = ["Data", "Value"]
            x.add_row(["Id Guru", Id_guru])
            x.add_row(["Nama Guru", nama])
            x.add_row(["Mapel Guru", mapel])
            x.add_row(["Kelas", mapel])
            x.add_row(["Jam", f"{Jam_mulai}-{Jam_selesai}"])
            x.add_row(["Id_ruangan", Id_ruangan])
            print(x)
            confirm = input("Apakah anda ingin melanjutkan tindakan ini (y/n): ")
            
            if confirm == 'y':
                query = """INSERT INTO `jadwal_pelayanan`(`Id_guru`, `Mapel`, `Jam_mulai_pelayanan`, `Jam_selesai_pelayanan`, `Id_ruangan`) 
                VALUES 
                (%s,%s,%s,%s,%s)"""
                data = (Id_guru, mapel, Jam_mulai, Jam_selesai, Id_ruangan)
                self.db.insertValue(query, data)

                print("=== Anda Berhasil Meng-input Data Jadwal ===")
            else:
                raise ValueError("=== Insert data anda gagal ===")
        except Exception as e :
            print(e)
            
    def update_jadwal_pelayanan(self):
        try : 
            print("=== Update Jadwal ===")
            self.read_jadwal()
            Id_jadwal_pelayanan = int(input("Masukkan ID Jadwal yang akan diupdate: "))
            
            query = """SELECT * FROM jadwal_pelayanan WHERE Id_jadwal_pelayanan = %s"""
            querytes = """SELECT * FROM jadwal_pelayanan	"""
            data = (Id_jadwal_pelayanan,)
            a = 0
            check_id = self.db.selectValue(querytes, data=None)
            list_check = []
            for a in range(len(check_id)) :
                check_id_jadwal = check_id[a][0]
                list_check.append(check_id_jadwal)

            if Id_jadwal_pelayanan not in list_check: 
                raise ValueError("=== Id Jadwal tidak ditemukan ===")
                
            if not check_id :
                raise ValueError("=== Id Jadwal tidak ditemukan ===")
            
            self.db.selectValuepretty(query, data)
            result = self.db.selectValue(query, data)
            confirmation = input("Apakah Anda ingin melanjutkan proses update (y/n)? ").lower()
            
            if confirmation == 'y':
                self.edit_jadwal_pelayanan(result, Id_jadwal_pelayanan)
                print("=== Data Jadwal berhasil diupdate ===")
            else:
                print("=== Proses update dibatalkan ===")

        except Exception as e :
            print(e)
            os.system('pause')

    def edit_jadwal_pelayanan(self, result, Id_jadwal) :
        Id_guru = result[0][1]
        Bidang_mapel = result[0][2]
        Id_ruangan = result[0][5]
        while True:
            try :
                print("=== Edit Value ===")
                print("1. Id Guru")
                print("2. Id Ruangan")
                pilih = int(input("Data yang ingin diubah: "))

                if pilih == 1:
                    quguru = """SELECT `Id_guru`, `Nama`, `Bidang_mapel` FROM `guru` WHERE Bidang_mapel=%s"""
                    self.db.selectValuepretty(quguru, (Bidang_mapel, ))
                    data = self.db.selectValue(quguru,(Bidang_mapel, ))
                    if not data :
                        raise ValueError("Data tidak ditemukan")
                    
                    a = 0
                    Id_guru = int(input("Masukkan ID Guru baru\t: "))
                    for a in range(len(data)) :
                        check_id_guru = data[a][1]

                    if check_id_guru != Id_guru : 
                        raise ValueError("=== Id Guru tidak ditemukan ===")
                    
                    query = """UPDATE jadwal_pelayanan SET Id_guru = %s WHERE Id_jadwal_pelayanan = %s"""
                    data = (Id_guru, Id_jadwal)
                    self.db.insertValue(query, data)


                elif pilih == 2:
                    ruang_query ="""SELECT * FROM `ruangan`"""
                    self.db.selectValuepretty(ruang_query, data=None)

                    Id_ruangan = int(input("Masukkan ID Ruangan baru\t: "))
                    select_query = """SELECT `Id_ruangan`, `Kondisi_ruangan`, `Kapasitas_kursi` FROM `ruangan` WHERE Id_ruangan=%s"""
                    resultR = self.db.selectValue(select_query, (Id_ruangan,))
                    if not resultR :
                        raise ValueError("=== Id Ruang tidak ditemukan ===")
                    if resultR[0][1] == "Tidak layak" :
                        raise ValueError("=== Ruang Tidak Layak ===")
                
                    query = """UPDATE jadwal_pelayanan SET Id_ruangan = %s WHERE Id_jadwal_pelayanan = %s"""
                    data = (Id_ruangan, Id_jadwal)
                    self.db.insertValue(query, data)
                    
                else:
                    print("Pilihan tidak tersedia")

                lanjut = str(input("Ganti data lain (y/n)? "))
                if lanjut.lower() != 'y':
                    break
                print("=== Anda Berhasil Meng-update Data Jadwal ===")
            except Exception as e  :
                print(e)
                os.system('pause')
            
    def delete_jadwal(self):
        try :
            print("=== Delete jadwal_pelayanan ===")
            self.read_jadwal()
            Id_jadwal = int(input("Masukkan ID jadwal_pelayanan yang akan dihapus: "))

            query_select = """SELECT * FROM jadwal_pelayanan WHERE Id_jadwal = %s"""
            data_select = (Id_jadwal,)
            self.db.selectValuepretty(query_select, data_select)

            data = self.db.selectValue(query_select, data_select)

            if not data :
                raise ValueError("=== Id jadwal_pelayanan tidak ditemukan ===")
            
            a = 0
            Id_jadwal = int(input("Masukkan Id jadwal_pelayanan \t: "))
            list_jadwal = []
            for a in range(len(data)) :
                check_Id_jadwal = data[a][1]
                list_jadwal.append(check_Id_jadwal)

            if Id_jadwal not in list_jadwal : 
                raise ValueError("=== Id jadwal_pelayanan tidak ditemukan ===")

            test = str(input("Apakah Anda yakin ingin menghapus data ini (y/n)? "))
            
            if test.lower() == 'y':
                query_delete = """DELETE FROM jadwal_pelayanan WHERE Id_jadwal_pelayanan = %s"""
                data_delete = (Id_jadwal,)
                self.db.insertValue(query_delete, data_delete)
                print("=== Anda Berhasil Menghapus Data Jadwal ===")
            else:
                print("=== Pembatalan Penghapusan Data Jadwal ===")
        except Exception as e :
            print(e)
            os.system('pause')
    
    def read_jadwal(self):
        while True : 
            print("=== Lihat Jadwal ===")
            print("1. Lihat semua jadwal")
            print("2. Lihat bedasarkan mapel")
            pilih = int(input("Pilih menu : "))
            if pilih == 1 :
                query = """SELECT * FROM jadwal_pelayanan"""
                self.db.selectValuepretty(query, data=None)
                print("=== Anda Berhasil menampilkan Data Jadwal ===")
                break
            elif pilih == 2 :
                mapelku = self.mapel()
                quguru = """SELECT * FROM `jadwal_pelayanan` WHERE Mapel=%s"""
                self.db.selectValuepretty(quguru, (mapelku, ))
                print("=== Anda Berhasil menampilkan Data Jadwal ===")
                break
            else :
                print("=== Pilihan tidak tersedia ===")

# done
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
                return "Tidak layak"
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
            data = (Kondisi_ruangan, Kapasitas_kursi)

            self.db.insertValue(quary,data)
            print("=== Anda Berhasil Meng-input Data Ruangan ===")
        else : 
            print("=== Anda Gagal Meng-input Data Ruangan ===")

    def edit_ruangan(self, result, Id_ruangan) :
        while True :
            Kondisi_ruangan = result[0][1]
            Kapasitas_kursi = result[0][2]
            print("=== Edit Value ===")
            print("1. Kondisi Ruangan")
            print("2. Kapasitas Kursi")
            pilih = int(input("Data yang ingin diubah : "))
            if pilih == 1:
                Kondisi_ruangan = self.kondisi_ruangan()
                query = """UPDATE `ruangan` SET `Kondisi_ruangan`=%s WHERE `Id_ruangan`=%s"""
                data = (Kondisi_ruangan, Id_ruangan)
                self.db.insertValue(query, data)
            elif pilih == 2:
                Kapasitas_kursi = int(input("Masukan Kapasitas Kursi\t: "))
                query = """UPDATE `ruangan` SET `Kapasitas_kursi`=%s WHERE `Id_ruangan`=%s"""
                data = (Kapasitas_kursi, Id_ruangan)
                self.db.insertValue(query, data)
            else : 
                print("Pilihan tidak tersedia")
            lanjut = str(input("Ganti data lain (y/n)? "))
            if lanjut == 'y' :
                continue
            else :
                break

    def update_ruangan(self) :
        print("=== Update Ruangan ===")
        self.read_ruangan()
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
        self.read_ruangan()
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
        print("=== Lihat Ruangan ===")
        print("1. Lihat semua")
        print("2. Lihat Ruangan Layak")
        print("3. Lihat Ruangan Tidak layak")
        pilih = int(input("Pilih menu : "))
        if pilih == 1 :
            query = """SELECT * FROM ruangan"""
            self.db.selectValuepretty(query, data=None)
        elif pilih == 2 :
            query = """SELECT * FROM ruangan WHERE Kondisi_ruangan=%s"""
            self.db.selectValuepretty(query, ("Layak", ))
        elif pilih == 3 :
            query = """SELECT * FROM ruangan WHERE Kondisi_ruangan=%s"""
            self.db.selectValuepretty(query, ("Tidak layak", ))
        print("=== Anda Berhasil Menampilkan Data Ruangan ===")

# done
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
                kelas = int(input("Kelas berapa? (4/5/6) :"))
                if kelas in [4,5,6] :
                    xkel = str(kelas)+"SD"
                    return xkel
                else : 
                    print("Pilihan tidak tersedia")
            elif pilih == 2 :
                kelas = int(input("Kelas berapa? (1/2/3) :"))
                if kelas in [1,2,3] :
                    xkel = str(kelas)+"SMP"
                    return xkel
                else : 
                    print("Pilihan tidak tersedia")
            elif pilih == 3 :
                kelas = int(input("Kelas berapa? (1/2/3) :"))
                if kelas in [1,2,3] :
                    jurusan = str(input("Jurusan apa? (IPA/IPS) :"))
                    if jurusan.upper() in ["IPA","IPS"] :
                        xkel = str(kelas)+"SMA "+ jurusan.upper()
                        return xkel
                    else : 
                        print("Pilihan tidak tersedia")
                else : 
                    print("Pilihan tidak tersedia")
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
        Kelas = result[0][1]
        Kategori = result[0][2]
        Biaya = result[0][3]
        while True :
            print("=== Edit Value ===")
            print("1. Kategori")
            print("2. Kelas")
            print("3. Biaya")
            pilih = int(input("Data yang ingin diubah : "))
            if pilih == 1:
                Kategori = self.kategori()
                query = """UPDATE paket_belajar SET `Kategori`= %s WHERE `Id_paket_belajar` = %s"""
                data = (Kategori, Id_paket_belajar)
                self.db.insertValue(query, data)

            elif pilih == 2:
                Kelas = self.kelas()
                query = """UPDATE paket_belajar SET `Kelas`= %s WHERE `Id_paket_belajar` = %s"""
                data = (Kelas, Id_paket_belajar)
                self.db.insertValue(query, data)
            elif pilih == 3:
                Biaya = int(input("Masukan Biaya Paket Belajar\t:"))
                query = """UPDATE paket_belajar SET `Biaya`= %s WHERE `Id_paket_belajar` = %s"""
                data = (Biaya, Id_paket_belajar)
                self.db.insertValue(query, data)
            else : 
                print("Pilihan tidak tersedia")
            lanjut = str(input("Ganti data lain (y/n)? "))
            if lanjut == 'y' :
                continue
            else :
                break

    def update_paket_belajar(self):
        print("=== Update Paket Belajar ===")
        self.read_paket_belajar()
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
        self.read_paket_belajar()
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
        print("=== Lihat Paket Belajar ===")
        print("1. Lihat Bedasarkan Kelas")
        print("2. Lihat Bedasarkan Kategori")
        print("3. Lihat Semua")
        pilih = int(input("Pilih menu : "))
        if pilih == 1 :
            query = """SELECT * FROM `paket_belajar` WHERE `Kelas`=%s"""
            data = self.kelas()
            self.db.selectValuepretty(query, (data, ))

        elif pilih == 2 :
            query = """SELECT * FROM `paket_belajar` WHERE `Kategori`=%s"""
            data = self.kategori()
            self.db.selectValuepretty(query, (data, ))

        elif pilih == 3 :
            query = """SELECT * FROM paket_belajar"""
            self.db.selectValuepretty(query, data=None)
        else : 
            print("Pilihan tidak tersedia")

    def read_kategori(self) :
        print("=== Lihat Paket Belajar ===")
        paket = self.kategori()
        x = PrettyTable()
        if paket == "Premium" :
            x.field_names = ["Fasilitas", "Premium"]
            x.add_row(["Pertemuan", "6x seminggu"])
            x.add_row(["TO", "24x Online (Sesuaikan jam siswa)"])
            x.add_row(["Modul", "Digital & Cetak"])   
            x.add_row(["Sharing Soal", "Ya"])   
            x.add_row(["Kelas Pengembangan diri Online", "Ya"])   
            x.add_row(["Wifi", "Ya"])   
            print(x)
        elif paket == "Reguler" :
            x.field_names = ["Fasilitas", "Reguler"]
            x.add_row(["Pertemuan", "4x seminggu"])
            x.add_row(["TO", "12x Online (Sesuaikan jam siswa)"])
            x.add_row(["Modul", "Digital"])   
            x.add_row(["Sharing Soal", "Ya"])   
            x.add_row(["Kelas Pengembangan diri Online", "Tidak"])   
            x.add_row(["Wifi", "Ya"])   
            print(x)
        else :
            print("Pilihan tidak tersedia")
