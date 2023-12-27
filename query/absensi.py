from datetime import datetime
import locale

# set bahasa waktu lokal indonesia
locale.setlocale(locale.LC_TIME, 'id_ID')

class absen_pegawai :
    def __init__(self, db):
        self.db = db

    def absen_datang(self, Id_pegawai) :
        try :
            tanggal = datetime.now().date()
            query = """SELECT * FROM `absen_pegawai` WHERE `Id_pegawai`=%s"""
            result = self.db.selectValue(query, (Id_pegawai,))
            i = 0 
            for i in range(len(result)) :
                test = result[i][2]
                if tanggal == test :
                    raise ValueError("Anda telah absen datang hari ini")
            jam_datang = datetime.now().time()
            Jam_selesai = None
            Absen = "Alpha"
            query = """INSERT INTO `absen_pegawai`(`Id_pegawai`, `Tanggal`, `Jam_datang`, `Jam_selesai`, `Absen`) 
                    VALUES 
                    (%s,%s,%s,%s,%s)"""
            data = (Id_pegawai, tanggal, jam_datang, Jam_selesai, Absen)
            self.db.insertValue(query,data)
            print(f"Anda Berhasil Absen Datang pada {tanggal}")
        except Exception as e :
            print(e)

    def absen_pulang(self, Id_pegawai) :
        try :
            tanggal = datetime.now().date()
            Jam_selesai = datetime.now().time()
            result = self.db.selectValue(query, (Id_pegawai,))
            i = 0 
            for i in range(len(result)) :
                test = result[i][3]
                if test is None :
                    raise ValueError("Anda belum absen datang hari ini")
            if not result :
                raise ValueError("Anda belum absen datang hari ini")
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
            print(f"Anda Berhasil Absen Pulang pada {tanggal}")
        except Exception as e :
            print(e)

    
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
        try :
            tanggal = datetime.now().date()
            query = """SELECT * FROM `absen_pegawai` WHERE `Id_pegawai`=%s"""
            result = self.db.selectValue(query, (Id_pegawai,))
            i = 0 
            for i in range(len(result)) :
                test = result[i][2]
                if tanggal == test :
                    raise ValueError("Anda telah absen hari ini")
            jam_datang = None
            Jam_selesai = None
            Absen = self.absen()
            query = """INSERT INTO `absen_pegawai`(`Id_pegawai`, `Tanggal`, `Jam_datang`, `Jam_selesai`, `Absen`) 
                    VALUES 
                    (%s,%s,%s,%s,%s)"""
            data = (Id_pegawai, tanggal, jam_datang, Jam_selesai, Absen)
            self.db.insertValue(query,data)
            print(f"Anda Berhasil Absen pada {tanggal}")
        except Exception as e :
            print(e)

class absen_guru :
    def __init__(self, db):
        self.db = db

    def absen_datang(self, Id_guru) :
        try :
            tanggal = datetime.now().date()
            query = """SELECT * FROM `absen_guru` WHERE `Id_guru`=%s"""
            result = self.db.selectValue(query, (Id_guru,))
            i = 0 
            for i in range(len(result)) :
                test = result[i][2]
                if tanggal == test :
                    raise ValueError("Anda telah absen datang hari ini")
            jam_datang = datetime.now().time()
            Jam_selesai = None
            Absen = "Alpha"
            query = """INSERT INTO `absen_guru`(`Id_guru`, `Tanggal`, `Jam_datang`, `Jam_selesai`, `Absen`) 
                    VALUES 
                    (%s,%s,%s,%s,%s)"""
            data = (Id_guru, tanggal, jam_datang, Jam_selesai, Absen)
            self.db.insertValue(query,data)
            print(f"Anda Berhasil Absen Datang pada {tanggal}")

        except Exception as e :
            print(e)

    def absen_pulang(self, Id_guru) :
        try :
            tanggal = datetime.now().date()
            Jam_selesai = datetime.now().time()
            query = """SELECT * FROM `absen_guru` WHERE `Id_guru`=%s"""
            result = self.db.selectValue(query, (Id_guru,))
            i = 0 
            for i in range(len(result)) :
                test = result[i][3]
                if test is None :
                    raise ValueError("Anda belum absen datang hari ini")
            if not result :
                raise ValueError("Anda belum absen datang hari ini")
                
            Absen = "Hadir"
            query = """
                UPDATE `absen_guru` 
                SET
                `Jam_selesai` = %s,
                `Absen` = %s 
                WHERE `Tanggal` = %s AND `Id_guru` = %s
            """
            data = (Jam_selesai, Absen, tanggal, Id_guru)
            self.db.insertValue(query, data)
            print(f"Anda Berhasil Absen Pulang pada {tanggal}")
        except Exception as e :
            print(e)

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
        try :
            tanggal = datetime.now().date()
            query = """SELECT * FROM `absen_pegawai` WHERE `Id_pegawai`=%s"""
            result = self.db.selectValue(query, (Id_pegawai,))
            i = 0 
            for i in range(len(result)) :
                test = result[i][2]
                if tanggal == test :
                    raise ValueError("Anda telah absen hari ini")
            jam_datang = None
            Jam_selesai = None
            Absen = self.absen()
            query = """INSERT INTO `absen_pegawai`(`Id_pegawai`, `Tanggal`, `Jam_datang`, `Jam_selesai`, `Absen`) 
                    VALUES 
                    (%s,%s,%s,%s,%s)"""
            data = (Id_pegawai, tanggal, jam_datang, Jam_selesai, Absen)
            self.db.insertValue(query,data)
            print(f"Anda Berhasil Absen pada {tanggal}")

        except Exception as e :
            print(e)
    
    def absen_s(self) :
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
    def absen_siswa(self,Id_guru) :
        while True :
            try :
                tanggal = datetime.now().date()
                id_siswa = int(input("Id siswa : "))
                id_jadwal = int(input("Id jadwal : "))
                query = """SELECT * FROM `absen_siswa` WHERE `Id_jadwal`=%s"""
                result = self.db.selectValue(query, (Id_guru,))
                i = 0 
                absen = self.absen_s()
                for i in range(len(result)) :
                    id_siswa_tes = result[i][2]
                    id_jadwal_tes = result[i][3]
                    if (id_siswa == id_siswa_tes) and (id_jadwal == id_jadwal_tes):
                        raise ValueError("Anda telah absen hari ini")
                    
                query = """INSERT INTO `absen_siswa`(`Id_guru`, `Id_siswa`, `Id_jadwal`, `Tanggal`, `Absen`) 
                VALUES (%s,%s,%s,%s,%s)"""
                data = (Id_guru,id_siswa,id_jadwal,tanggal,absen)
                self.db.insertValue(query, data)
                print(f"Siswa dengan {id_siswa} berhasil absen")
                tambah = str(input("Ingin Absen lagi (y/n) ? "))
                if tambah.lower() == "y" :
                    continue
                else :
                    break

            except Exception as e :
                print(e)
class absen_siswa :
    def __init__(self, db):
        self.db = db

    def lihat_absen(self, Id_siswa) :
        query = """SELECT * FROM `absen_siswa` WHERE Id_siswa=%s AND Id_jadwal=%s"""
        Id_jadwal = int(input("Masukan Id jadwal : "))
        data = (Id_siswa, Id_jadwal)
        self.db.selectValuepretty(query, data)
